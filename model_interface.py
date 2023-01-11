class Model:
    def __init__(self, pack):
        self.data = []
        self.pack = pack

    def get_animal_list(self, turn=0):
        """Return list of all animals, or for specific turn"""
        pass

    def get_animal_list_tier(self, tier):
        """Return list of animals for given tier"""
        pass

    def get_food_list(self, turn=0):
        """Return list of all foods, or for specific turn"""
        pass

    def get_current_tier(self, turn):
        """Return tier for given turn"""
        pass

    def get_level_up_tier(self, turn):
        """Return level up tier"""
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

    def get_pet_ability(self, uid, level=1):
        """Return ability for given uid and level"""
        pass
