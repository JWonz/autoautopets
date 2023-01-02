import random

from model_interface import Model
from view_interface import View


class GameController:
    def __init__(self, model=Model("StandardPack"), view=View(), seed=1):
        self.model = model
        self.view = view

        random.seed(seed)
        self.is_shopping = False
        self.state = {
            'turn': 1,
            'hearts': 10,
            'trophy': 0,
            'team': [],  # {name, level, attack, health, status}
            'frozen_pets': [],  # list of names
            'frozen_food': []  # list of names
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
        gold = 10

        # Randomly select animals/food (from available lists)
        animal_list = self.model.get_animal_list(self.state['turn'])
        food_list = self.model.get_food_list(self.state['turn'])

        num_pet_slots = self.model.get_pet_shop_slots(self.state['turn'])
        num_food_slots = self.model.get_food_shop_slots(self.state['turn'])

        pets_shop = random.sample(animal_list, num_pet_slots - len(self.state['frozen_pets']))
        food_shop = random.sample(food_list, num_food_slots - len(self.state['frozen_food']))

        # Display/Interaction loop
        self.is_shopping = True

        # Apply StartOfTurn effects from existing team (e.g. gold gains)
        # TODO

        while self.is_shopping:
            self.view.display_shop(self.state, pets_shop, food_shop)
            user_input = self.view.get_input_shop()
            print(f"User input was: {user_input}")

            action, *args = user_input.lower().split(" ")
            self.handle_action(action, *args)

        return

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
        # Freeze/thaw shop animals or food
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

    def default(self, *args):
        return

    def battle(self):
        # code to run the battle loop
        self.state['hearts'] -= 3
        pass


if __name__ == '__main__':

    from model_api import ModelApi
    from view_cmdline import SuperAutoCommandline

    game = GameController(ModelApi("StandardPack"), SuperAutoCommandline())
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