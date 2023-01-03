import json
import requests
from datetime import datetime
import os
import glob
from model_interface import Model


def read_most_recent_json(directory):
    # Get a list of all the files in the directory
    file_list = glob.glob(os.path.join(directory, '*.json'))

    # Sort the list of files by modification time
    file_list.sort(key=os.path.getmtime)

    # Get the most recent file
    most_recent_file = file_list[-1]

    # Open the most recent file in read mode
    with open(most_recent_file, 'r') as f:
        # Read the contents of the file
        contents = json.load(f)

    # Return the contents of the file
    return contents


class ModelApi(Model):

    def __init__(self, pack):
        super().__init__(pack)
        self.data = read_most_recent_json("./data")
        if self.data is None:
            self.get_superautopet_com()
        self.reformat_data()

    def save_locally(self):
        # Get the current timestamp
        datestamp = datetime.now().strftime('%Y%m%d')

        # Construct the file name using the timestamp
        file_name = f"./data/sap_{datestamp}.json"

        # Open the file in write mode
        with open(file_name, 'w') as f:
            # Write the data to the file as JSON
            json.dump(self.data, f)

    def reformat_data(self):
        # TODO - put all pets and foods into an items list with "kind" attribute
        # Allow fetching pet/food more efficiently
        pass

    def get_superautopet_com(self):
        response = requests.get('https://superauto.pet/api.json')

        if response.status_code == 200:
            # Load the JSON data from the response
            self.data = response.json()

    def get_animal_list(self, turn=0):
        """Return list of all animal ids, or for specific turn"""
        if self.pack == 'All':
            return [p['id'] for p in self.data['pets'].values()
                    if "EasterEgg" not in p["packs"]]
        elif turn == 0:
            return [p['id'] for p in self.data['pets'].values()
                    if self.pack in p['packs']
                    and "EasterEgg" not in p["packs"]]
        else:
            turn_data = self.get_turn_data(turn)
            return [p["id"] for p in self.data["pets"].values()
                    if p["tier"] == turn_data["tiersAvailable"]
                    and self.pack in p["packs"]
                    and "EasterEgg" not in p["packs"]]

    def get_food_list(self, turn=0):
        """Return list of all food names, or for specific turn"""
        if self.pack == 'All':
            return [f['id'] for f in self.data['foods'].values()]
        elif turn == 0:
            return [f['id'] for f in self.data['foods'].values() if self.pack in f['packs']]
        else:
            turn_data = self.get_turn_data(turn)
            return [f['id'] for f in self.data["foods"].values()
                    if f["tier"] == turn_data["tiersAvailable"]
                    and self.pack in f["packs"]]

    def get_turn_data(self, turn):
        return self.data["turns"]["turn-11"] if turn > 11 else self.data["turns"]["turn-" + str(turn)]

    def get_current_tier(self, turn):
        """Return tier for given turn"""
        pass

    def get_pet_shop_slots(self, turn):
        """Return number of pet slots for given turn"""
        turn_data = self.get_turn_data(turn)
        return turn_data["animalShopSlots"]

    def get_food_shop_slots(self, turn):
        """Return number of food slots for given turn"""
        turn_data = self.get_turn_data(turn)
        return turn_data["foodShopSlots"]

    def get_emoji(self, uid, kind="pets"):
        return self.data[kind][uid]["image"]["unicodeCodePoint"]


if __name__ == '__main__':
    myModel = ModelApi("All")
    myModel.get_superautopet_com()
    myModel.save_locally()
