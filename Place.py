from Npc import  Npc
from Item import Item

class Place:
    ##
    # PLACE IDS SEE MAIN FOR UPDATED ONES
    # 0 = Fields # EMPTY
    # 1 = Forest
    # 2 = Forest Clearing
    # 3 = City
    # 4 = Forest Entrance
    # 5 = Lake
    # 6 = Grain Field
    # 7 = House
    # 8 = Wind Mill
    # 9 = Path
    ##10 = Forest Path

    main_class = None
    x = None
    y = None
    place_type = 0 #Forest
    ground_items = []



    def __init__(self, place_type, main_class, x, y):
        self.place_type = place_type
        self.main_class = main_class

    def generate_npcs(self):
        pass
        #return [Npc("Mike"), Npc("Jane")]

    def get_place_context_text(self):
        text = ""

        if (self.place_type == 0):  # Forest
            text += "You are in a field of green. "

        if (self.place_type == 1):  # Forest clearing
            text += "You are standing in the middle of a dense forest, there are all kinds of trees around you. "

        if(self.place_type == 2):
            text += "You are in a clearing of the forest, you see forest in all directions. "
        if (self.place_type == 3):
            text += "You are in the middle of a large city. The market district around you is filled with loud people trying to sell and buy everything from boots to drugs. "
        if (self.place_type == 4):
            text += "You are standing in fields next to a forest. There is a mystical entrance to what definitely isn't a classic cave maze puzzle. "
        if (self.place_type == 5):
            text += "You aren't standing here. If you were, you would surely be dead soon. "
        if (self.place_type == 6):
            text += "You are right in the middle of a large grain field. "
        if (self.place_type == 7):
            add_to_text = "You are in a farmstead. "
            for quest in self.main_class.quests:
                if(quest.quest_x == self.x and quest.quest_y == self.y):
                    add_to_text = quest.get_house_status_text()
            text += add_to_text

        if (self.place_type == 8):
            text += ""
        if (self.place_type == 9):
            text += ""
        if (self.place_type == 10):
            text += ""

        return text

    def kill_npc(self, npc, with_what):
        print("-------------------------------------------")
        print("You kill \033[1;32m" + npc.npc_name + "\033[1;m with \033[1;36m" + with_what.item_name + "\033[1;m")

        for item in npc.has_items:
            self.ground_items.append(item)

        self.npcs.remove(npc)

    def print_ground_items(self):
        print("-------------------------------------------")
        print("You see the following items on the ground.")
        found_items = False
        for item in self.ground_items:
            print("\033[1;36m" + item.item_name + "\033[1;m")
            found_items = True

        if(not found_items):
            print("You don't see anything noteworthy on the ground.")