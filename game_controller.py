import random

import sap_effects
from model_interface import Model
from view_interface import View


class GameController:

    max_team_slots = 5
    max_shop_slots = 7
    default_cost = 3

    def __init__(self, model=Model("StandardPack"), view=None, seed=1):
        self.model = model
        self.view = view or View(self.model)

        random.seed(seed)
        self.is_running = True
        self.is_shopping = False
        self.state = {
            'turn': 1,
            'hearts': 10,
            'trophy': 0,
            # {id, level, xp, baseAttack, baseHealth, tempAttack, tempHealth, ability}
            'team': [None, None, None, None, None],
            'shop_pets': [],  # {id, cost, baseAttack, baseHealth, is_frozen, ability}
            'shop_food': [],  # {id, cost, is_frozen, ability}
            'gold': 10
        }

    def run(self):
        while self.is_running:
            self.shop()
            self.battle()
            self.state['turn'] += 1

    def check_gameover(self):
        if self.state['hearts'] > 0 and self.state['trophy'] < 10:
            self.is_running = False

    def shop(self):
        # Set gold to 10, track for buys/sells
        self.state['gold'] = 10
        self.randomize_shop()

        # Display/Interaction loop
        self.is_shopping = True

        # Apply StartOfTurn effects from existing team (e.g. gold gains)
        # TODO

        while self.is_shopping and self.is_running:
            self.view.display_shop(self.state)
            user_input = self.view.get_input_shop()

            action, *args = user_input.lower().split(" ")
            self.handle_action(action, *args)
        return

    def randomize_shop(self):
        """Keeps all frozen items to left, randomizes the rest"""
        f_pets = [p for p in self.state['shop_pets'] if p is not None and p['is_frozen']]
        f_food = [f for f in self.state['shop_food'] if f is not None and f['is_frozen']]

        # Randomly select animals/food (from available lists)
        animal_list = self.model.get_animal_list(self.state['turn'])
        food_list = self.model.get_food_list(self.state['turn'])

        r_pets = random.sample(animal_list, self.model.get_pet_shop_slots(self.state['turn']) - len(f_pets))
        r_food = random.sample(food_list, self.model.get_food_shop_slots(self.state['turn']) - len(f_food))

        # {id, cost, baseAttack, baseHealth, is_frozen, ability}
        self.state['shop_pets'] = f_pets + [{'id': p['id'],
                                             'cost': getattr(p, 'cost', self.default_cost),
                                             'baseAttack': p['baseAttack'],
                                             'baseHealth': p['baseHealth'],
                                             'is_frozen': False,
                                             'ability': p['level1Ability'],
                                             'is_pet': True
                                             } for p in r_pets]
        # {id, cost, is_frozen, ability}
        self.state['shop_food'] = f_food + [{'id': f['id'],
                                             'cost': getattr(f, 'cost', self.default_cost),
                                             'is_frozen': False,
                                             'ability': f['ability'],
                                             'is_pet': False
                                             } for f in r_food]

    def get_shop_item(self, x):
        """# Returns the shop item at position x; or None if invalid"""
        # x is 1 to max_shop_slots
        # N + M <= max_shop_slots
        # if = max_shop_slots, then pets stack is 1 to N, foods stack is max_shop_slots - N
        # if < max_shop_slots, then pets stack is 1 to N, foods stack is max_shop_slots - M
        p_i = int(x) - 1
        f_i = self.max_shop_slots - int(x)
        if len(self.state['shop_pets']) > p_i > -1 and self.state['shop_pets'][p_i] is not None:
            return self.state['shop_pets'][p_i]
        elif len(self.state['shop_food']) > f_i > -1 and self.state['shop_food'][f_i] is not None:
            return self.state['shop_food'][f_i]
        else:
            return None

    def handle_action(self, action, *args):
        actions = {
            'roll': self.roll,
            'buy': self.buy,
            'freeze': self.freeze,
            'sell': self.sell,
            'move': self.move,
            'end': self.end_turn,
            'quit': self.quit
        }
        return actions.get(action, self.default)(*args)

    def roll(self, *args):
        # Roll - randomly repopulates unfrozen shop slots for 1 gold
        if self.state['gold'] > 0:
            self.state['gold'] -= 1
            self.randomize_shop()
        return

    def freeze(self, x):
        # Freeze/thaw shop animals or food - 1 to 7
        item = self.get_shop_item(x)
        if item is not None:
            item['is_frozen'] = not item['is_frozen']

    def buy(self, x, y):
        # TODO - validate input
        item = self.get_shop_item(x)
        y_i = int(y) - 1

        if self.state['gold'] < item['cost']:
            # Not enough gold!
            return

        if item['is_pet']:

            # {id, level, baseAttack, baseHealth, tempAttack, tempHealth, ability}
            if self.state['team'][y_i] is None:
                self.state['gold'] -= item['cost']
                self.state['team'][y_i] = {
                    'id': item['id'],
                    'level': 1,
                    'xp': 0,
                    'baseAttack': item['baseAttack'],
                    'baseHealth': item['baseHealth'],
                    'tempAttack': 0,
                    'tempHealth': 0,
                    'ability': item['ability']
                }
            else:
                if self.state['team'][y_i]['id'] == item['id']:
                    self.state['gold'] -= item['cost']

                    self.state['team'][y_i]['xp'] += 1
                    self.state['team'][y_i]['baseAttack'] += 1
                    self.state['team'][y_i]['baseHealth'] += 1

                    if self.state['team'][y_i]['xp'] == self.state['team'][y_i]['level'] + 1:
                        self.state['team'][y_i]['level'] += 1
                        self.state['team'][y_i]['xp'] = 0
                else:
                    return  # Cannot buy animal onto different one -- TODO: replace with error message

            # Remove from shop
            self.state['shop_pets'][self.state['shop_pets'].index(item)] = None
            # TODO - improve control logic - this can easily get confusing when the item was successful or not

        else:

            # Bad input cases:
            # - tries applying to empty team slot
            # - tries applying generic effect to specific animal
            # TODO

            # Food always triggers from "Buy" and is triggeredBy "self"
            # Food effects: 'ModifyStats', 'ApplyStatus', 'Faint', 'GainExperience'
            # Food effect targets: 'PurchaseTarget', 'RandomFriend', 'EachShopAnimal'

            # Food applied to specific pet
            if self.state['team'][y_i] is not None:
                self.state['gold'] -= item['cost']
                context = {'PurchaseTarget': y_i}
                sap_effects.sap_effect_map[item['ability']['effect']['kind']](self.state, item, context)
            else:
                return  # Cannot apply food to empty team slot

            # Food used with general effect (apply to random pets or shop)

            # Remove from shop
            self.state['shop_food'][self.state['shop_food'].index(item)] = None
            return

        # Buy shop animals or food
        # Buy shop animal, combining into team animal

        # Buy X Y - buys X position pet or food, places on Y team slot
        #       - Combines animal if possible
        #       - Slides un-combinable animals to right, last slot left
        #       - Fails if team is full
        #       - General food items ignore Y input value
        #       - Fails if food cannot be applied
        #       - Fails if not enough gold
        return

    def sell(self, x):
        # Sell team animals
        return

    def move(self, x, y):
        # Combine team animals # turn_data["levelUpTier"]
        return

    def end_turn(self, *args):
        self.is_shopping = False
        return

    def quit(self, *args):
        self.is_running = False
        return

    def default(self, *args):
        return

    def battle(self):
        # code to run the battle loop
        self.state['hearts'] -= 1
        pass


if __name__ == '__main__':

    from model_api import ModelApi
    from view_cmdline import SuperAutoCommandline

    model = ModelApi("StandardPack")
    game = GameController(model, SuperAutoCommandline(model))
    game.run()

    """
    Pipeline:
        StartOfTurn
        EndOfTurn
            EndOfTurnWith3PlusGold
            EndOfTurnWithLvl3Friend
            EndOfTurnWith4OrLessAnimals
        StartOfBattle

        Anytime:
            WhenDamaged
            Hurt
            Faint
            Summoned
            CastsAbility

        Shop:
            Buy
            Sell
            BuyAfterLoss
            BuyTier1Animal
            BuyFood
            EatsShopFood
            LevelUp

        Battle:
            BeforeAttack
            WhenAttacking
            AfterAttack
            KnockOut
    """



    """
    Run through one SAP round:
    - Start of round effects:
        - Snipe attacks / range attacks
        - Health update effects; crab copy, skunk reduce
    - Order of effects: Highest attack then left to right
    - Then animals attack each other - subtract attack from health
        - Attack amount is summed from all effects
        - After attack special effects like "Peanut", hurt effects, faint effect
        - Summon effect: order of summons? enemy effect (dirty rat), honey, effect (ram)
        - FriendAheadAttacks effects

    - 



    """