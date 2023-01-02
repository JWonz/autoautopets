class Model:
    def __init__(self, pack):
        self.data = []
        self.pack = pack

    def get_animal_list(self, turn=0):
        """Return list of all animal ids, or for specific turn"""
        pass

    def get_food_list(self, turn=0):
        """Return list of all food ids, or for specific turn"""
        pass

    def get_current_tier(self, turn):
        """Return tier for given turn"""
        pass

    def get_pet_shop_slots(self, turn):
        """Return number of pet slots for given turn"""
        pass

    def get_food_shop_slots(self, turn):
        """Return number of food slots for given turn"""
        pass

    def get_emoji(self, uid, kind="pets"):
        """Return emoji for given uid, and select for pets or food"""
        pass