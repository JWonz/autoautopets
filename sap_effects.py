def modify_stats(state, item, context):
    target = item['ability']['effect']['target']
    targets = sap_target_map[target['kind']](state, item, context)

    for t in targets:
        if item['ability']['effect']['untilEndOfBattle']:
            t['tempAttack'] += item['ability']['effect']['attackAmount']
            t['tempHealth'] += item['ability']['effect']['healthAmount']
        else:
            t['baseAttack'] += item['ability']['effect']['attackAmount']
            t['baseHealth'] += item['ability']['effect']['healthAmount']


def apply_status(item):
    pass


def faint(item):
    pass


def gain_experience(item):
    pass


def modify_damage(item):
    pass


def summon_pet(item):
    pass


def splash_damage(item):
    pass


def respawn_pet(item):
    pass


def deal_damage(item):
    pass


def gain_gold(item):
    pass


def transfer_stats(item):
    pass


def one_of(item):
    pass


def summon_random_pet(item):
    pass


def all_of(item):
    pass


def swallow(item):
    pass


def reduce_health(item):
    pass


def discount_food(item):
    pass


def refill_shops(item):
    pass


def transfer_ability(item):
    pass


def food_multiplier(item):
    pass


def repeat_ability(item):
    pass


def evolve(item):
    pass


sap_effect_map = {
    "ModifyStats": modify_stats,
    "ApplyStatus": apply_status,
    "Faint": faint,
    "GainExperience": gain_experience,
    "ModifyDamage": modify_damage,
    "SummonPet": summon_pet,
    "SplashDamage": splash_damage,
    "RespawnPet": respawn_pet,
    "DealDamage": deal_damage,
    "GainGold": gain_gold,
    "TransferStats": transfer_stats,
    "OneOf": one_of,
    "SummonRandomPet": summon_random_pet,
    "AllOf": all_of,
    "Swallow": swallow,
    "ReduceHealth": reduce_health,
    "DiscountFood": discount_food,
    "RefillShops": refill_shops,
    "TransferAbility": transfer_ability,
    "FoodMultiplier": food_multiplier,
    "RepeatAbility": repeat_ability,
    "Evolve": evolve
}


def purchase_target(state, item, context):
    return [state['team'][context['PurchaseTarget']]]


def random_friend(state, item):
    pass


def each_shop_animal(state, item):
    pass


def left_most_friend(state, item):
    pass


def each_friend(state, item):
    pass


def triggering_entity(state, item):
    pass


def self(state, item):
    pass


def random_enemy(state, item):
    pass


def friend_behind(state, item):
    pass


def all(state, item):
    pass


def adjacent_animals(state, item):
    pass


def friend_ahead(state, item):
    pass


def adjacent_friends(state, item):
    pass


def lowest_health_enemy(state, item):
    pass


def right_most_friend(state, item):
    pass


def level_2_and_3_friends(state, item):
    pass


def different_tier_animals(state, item):
    pass


def highest_health_enemy(state, item):
    pass


def last_enemy(state, item):
    pass


def first_enemy(state, item):
    pass


def each_enemy(state, item):
    pass


sap_target_map = {
    "PurchaseTarget": purchase_target,
    "RandomFriend": random_friend,
    "EachShopAnimal": each_shop_animal,
    "LeftMostFriend": left_most_friend,
    "EachFriend": each_friend,
    "TriggeringEntity": triggering_entity,
    "Self": self,
    "RandomEnemy": random_enemy,
    "FriendBehind": friend_behind,
    "All": all,
    "AdjacentAnimals": adjacent_animals,
    "FriendAhead": friend_ahead,
    "AdjacentFriends": adjacent_friends,
    "LowestHealthEnemy": lowest_health_enemy,
    "RightMostFriend": right_most_friend,
    "Level2And3Friends": level_2_and_3_friends,
    "DifferentTierAnimals": different_tier_animals,
    "HighestHealthEnemy": highest_health_enemy,
    "LastEnemy": last_enemy,
    "FirstEnemy": first_enemy,
    "EachEnemy": each_enemy
}
