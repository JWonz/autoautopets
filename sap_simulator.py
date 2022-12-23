from sap_metadata_cacher import read_most_recent_json


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
    print(data)
