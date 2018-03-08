class Item:
    item_name = "ERR"
    amount = 0
    #Item uses

    weapon_items = ["axe", "hands"]
    food_items = ["bread", "sausage", "potato", "milk"]
    quest_items = [["window", "nails", "bundle of planks", "bundle of rotten planks"], []]

    def __init__(self, item_name, amount):
        self.item_name = item_name
        self.amount = amount

    def is_weapon(self):
        for name in self.weapon_items:
            if(self.item_name.lower() == name):
                return True
        return False

    def is_food(self):
        for name in self.food_items:
            if(self.item_name.lower() == name):
                return True
        return False

