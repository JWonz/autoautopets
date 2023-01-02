from view_interface import View
from model_interface import Model


class SuperAutoCommandline(View):
    def __init__(self, model):
        super().__init__(model)

    def display_shop(self, state):
        print("Team:")
        print(self.to_string_team(state['team']))
        print("Shop:")
        print(self.to_string_shop(state['shop_pets'], state['shop_food']))
        print("Gold:", state['gold'], "Turn:", state['turn'], "Hearts:", state['hearts'], "Trophies:", state['trophy'])

    def display_battle(self, data):
        print("Battle")

    def to_string_team(self, team):
        pass

    def to_string_shop(self, pets, food):
        max_slots = 7
        pet_pics = "".join([self.model.get_emoji(p['id'], "pets") for p in pets])
        food_pics = "".join([self.model.get_emoji(f['id'], "foods") for f in food])
        pet_ice = "".join(["❄️" if p['is_frozen'] else " " for p in pets])
        food_ice = "".join(["❄" if f['is_frozen'] else " " for f in food])

        return pet_pics + food_pics + "\r\n" + pet_ice + food_ice

    def get_input_shop(self):
        user_input = input("Roll, Buy X Y, Sell X, Move X Y, Freeze X, End")
        return user_input
