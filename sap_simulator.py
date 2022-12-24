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
    sap_data = read_most_recent_json("./data")

    # get list of animals based on pack used
    animals = [p for p in sap_data["pets"].values()]


    turn = 1
    hearts = 10
    trophy = 0
    frozen_shop_slots = []
    while hearts > 0 and trophy < 10:
        # TODO: separate out shop/battle logic from UI specific
        shop_cmdline(sap_data, turn)
        battle_cmdline()
        turn += 1



def shop_cmdline(game_data, turn):
    turn_data = data["turns"]["turn-11"] if turn > 11 else data["turns"]["turn-" + str(turn)]
    animal_list = [p for p in game_data["pets"].values() if p["tier"] == turn_data["tiersAvailable"]]

    # turn_data["animalShopSlots"]
    # turn_data["foodShopSlots"]
    # turn_data["tiersAvailable"]
    # turn_data["levelUpTier"]

    # Display shop pets and food


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

    data = read_most_recent_json("./data")
    pets = [p for p in data["pets"].values()]
    print(data)
