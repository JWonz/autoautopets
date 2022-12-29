import random
random.seed(1)

from sap_metadata_cacher import read_most_recent_json


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


def commandline_ui():
    """
    Starts a commandline version of the game.
    :return:
    """
    # TODO: refactor to read sap data into interface data structure; then JSON change only impacts that file
    sap_data = read_most_recent_json("./data")

    # get list of animals based on pack used
    animals = [p for p in sap_data["pets"].values()]
    # animals = list(filter(lambda p: "StandardPack" in p["packs"], animals))

    turn = 1
    hearts = 10
    trophy = 0
    team = []
    frozen_pets = []
    frozen_food = []
    while hearts > 0 and trophy < 10:
        # TODO: separate out shop/battle logic from UI specific
        shop_cmdline(sap_data, "StandardPack", turn, team, frozen_pets, frozen_food)
        battle_cmdline()
        turn += 1


def shop_cmdline(game_data, pack, turn, team, pets_frozen, food_frozen):
    turn_data = game_data["turns"]["turn-11"] if turn > 11 else game_data["turns"]["turn-" + str(turn)]
    animal_list = [p for p in game_data["pets"].values()
                   if p["tier"] == turn_data["tiersAvailable"]
                   and pack in p["packs"]]
    food_list = [f for f in game_data["foods"].values()
                 if f["tier"] == turn_data["tiersAvailable"]
                 and pack in f["packs"]]

    # Set gold to 10, track for buys/sells
    gold = 10

    # Randomly select animals/food (from available lists)
    pets_shop = random.sample(animal_list, turn_data["animalShopSlots"] - len(pets_frozen))
    food_shop = random.sample(food_list, turn_data["foodShopSlots"] - len(food_frozen))

    # Display/Interaction loop
    is_turn = True

    # Apply StartOfTurn effects from existing team (e.g. gold gains)
    # TODO

    while is_turn:
        # Display Shop Animals, Food, and Team
        print(team)
        print(pets_frozen, pets_shop)
        print(food_frozen, food_shop)

        action = input("Roll, BuyXY, MovePetXY, EndTurn")
        # Roll - randomly repopulates unfrozen shop slots for 1 gold
        # BuyXY - buys X position pet or food, places on Y team slot
        #       - Combines animal if possible
        #       - Slides un-combinable animals to right, last slot left
        #       - Fails if team is full
        #       - General food items ignore Y input value
        #       - Fails if food cannot be applied
        #       - Fails if not enough gold

        print(f"User input was: {action}")

        print("\u2764")  # prints a heart symbol
        print("\u1F99F")

        if action == "EndTurn":
            is_turn = False

        # User interactions:
        # Buy shop animals or food
        # Buy shop animal, combining into team animal
        # Freeze/thaw shop animals or food
        # Sell team animals
        # Combine team animals # turn_data["levelUpTier"]

    return


def battle_cmdline():

    return


def run_game():

    start_of_turn()
    end_of_turn()
    start_of_battle()

    return


def start_of_turn():

    return


def end_of_turn():

    return


def start_of_battle():

    return


def run_round(player1_state, player2_state):
    winner = 0
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



    return winner


def shop_round(health, wins, turn, team, frozen):

    return team, frozen


if __name__ == '__main__':

    commandline_ui()
