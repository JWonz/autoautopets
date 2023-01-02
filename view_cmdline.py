from view_interface import View


class SuperAutoCommandline(View):
    def __init__(self):
        pass

    def display_shop(self, state, pets_shop, food_shop):
        print("Shop")

        print("Team:")
        print(state['team'])
        print("Shop:", [p["image"]["unicodeCodePoint"] for p in state['frozen_pets']],
              [p["image"]["unicodeCodePoint"] for p in pets_shop])
        print("Food:", [f["image"]["unicodeCodePoint"] for f in state['frozen_food']],
              [f["image"]["unicodeCodePoint"] for f in food_shop])

    def display_battle(self, data):
        print("Battle")

    def get_input_shop(self):
        user_input = input("Roll, Buy X Y, Sell X, Move X Y, Freeze X, End")
        return user_input
