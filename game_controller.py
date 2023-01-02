import random

from model_interface import Model
from view_interface import View


class GameController:
    def __init__(self, model=Model("StandardPack"), view=None, seed=1):
        self.model = model
        self.view = view or View(self.model)

        random.seed(seed)
        self.is_shopping = False
        self.state = {
            'turn': 1,
            'hearts': 10,
            'trophy': 0,
            'team': [],  # {name, level, attack, health, status}
            'shop_pets': [],  # {id, is_frozen}
            'shop_food': [],  # {id, is_frozen}
            'gold': 10
        }

    def run(self):
        while self.is_running():
            self.shop()
            self.battle()
            self.state['turn'] += 1

    def is_running(self):
        return self.state['hearts'] > 0 and self.state['trophy'] < 10

    def shop(self):
        # code to run the shop loop
        # Set gold to 10, track for buys/sells
        self.state['gold'] = 10
        self.randomize_shop()

        # Display/Interaction loop
        self.is_shopping = True

        # Apply StartOfTurn effects from existing team (e.g. gold gains)
        # TODO

        while self.is_shopping:
            self.view.display_shop(self.state)
            user_input = self.view.get_input_shop()
            print(f"User input was: {user_input}")

            action, *args = user_input.lower().split(" ")
            self.handle_action(action, *args)

        return

    def randomize_shop(self):
        """Keeps all frozen items to left, randomizes the rest"""
        f_pets = [p for p in self.state['shop_pets'] if p['is_frozen']]
        f_food = [f for f in self.state['shop_food'] if f['is_frozen']]

        # Randomly select animals/food (from available lists)
        animal_list = self.model.get_animal_list(self.state['turn'])
        food_list = self.model.get_food_list(self.state['turn'])

        r_pets = random.sample(animal_list, self.model.get_pet_shop_slots(self.state['turn']) - len(f_pets))
        r_food = random.sample(food_list, self.model.get_food_shop_slots(self.state['turn']) - len(f_food))

        self.state['shop_pets'] = f_pets + [{'id': p, 'is_frozen': False} for p in r_pets]
        self.state['shop_food'] = f_food + [{'id': f, 'is_frozen': False} for f in r_food]

    def handle_action(self, action, *args):
        actions = {
            'roll': self.roll,
            'buy': self.buy,
            'freeze': self.freeze,
            'sell': self.sell,
            'move': self.move,
            'end': self.end_turn
        }
        return actions.get(action, self.default)(*args)

    def roll(self, *args):
        # Roll - randomly repopulates unfrozen shop slots for 1 gold
        self.state['gold'] -= 1
        self.randomize_shop()
        return

    def buy(self, x, y):
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

    def freeze(self, x):
        # Freeze/thaw shop animals or food - 1 to 7
        int_x = int(x) - 1
        self.state['shop_pets'][int_x]['is_frozen'] = not self.state['shop_pets'][int_x]['is_frozen']

    def sell(self, x):
        # Sell team animals
        return

    def move(self, x, y):
        # Combine team animals # turn_data["levelUpTier"]
        return

    def end_turn(self, *args):
        self.is_shopping = False
        return

    def default(self, *args):
        return

    def battle(self):
        # code to run the battle loop
        self.state['hearts'] -= 3
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