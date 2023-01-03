import os
from view_interface import View
from model_interface import Model


class SuperAutoCommandline(View):
    def __init__(self, model):
        super().__init__(model)

    def display_shop(self, state):
        print()
        print("Team:")
        print(self.to_string_team(state['team']))
        print()
        print("Shop:")
        print(self.to_string_shop(state['shop_pets'], state['shop_food']))
        print("Gold:", state['gold'], "Turn:", state['turn'], "Hearts:", state['hearts'], "Trophies:", state['trophy'])

    def display_battle(self, data):
        print("Battle")

    def to_string_team(self, team):
        max_slots = 5
        output = f"|____|____|____|____|____|"
        output_labels = f"| 1  | 2  | 3  | 4  | 5  |"
        return output

    def to_string_shop(self, pets, food):
        max_slots = 7
        pet_pics = "|".join([f'❄️{self.model.get_emoji(p["id"], "pets")}❄️' if p['is_frozen']
                             else f' {self.model.get_emoji(p["id"], "pets")} '
                             for p in pets])
        food_pics = "|".join([f'❄️{self.model.get_emoji(f["id"], "foods")}❄️' if f['is_frozen']
                              else f' {self.model.get_emoji(f["id"], "foods")} '
                              for f in reversed(food)])

        # food_pics = "|".join([self.model.get_emoji(f['id'], "foods") for f in food])
        # pet_ice = " | ".join(["❄️" if p['is_frozen'] else "__" for p in pets])
        # food_ice = " | ".join(["❄️" if f['is_frozen'] else "__" for f in food])

        num_empty_slots = max_slots - len(pets) - len(food)
        empty_slots = "   ".join(["--" for _ in range(num_empty_slots)])

        output1 = f"|{pet_pics}| {empty_slots} |{food_pics}|"
        output_labels = f"| 1  | 2  | 3  | 4  | 5  | 6  | 7  |"
        # output2 = f"| {pet_ice} | {empty_slots} | {food_ice} |"
        # return output1 + "\n" + output2
        return output1 + "\n" + output_labels

    def get_input_shop(self):
        user_input = input("Roll, Freeze X, Buy X Y, Sell X, Move X Y, End")
        return user_input
