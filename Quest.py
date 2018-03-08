from Npc import Npc

class QUEST_FarmerHouse:
    quest_name = "Farmers house"
    quest_npcs = None
    main_class = None
    quest_x = 0
    quest_y = 0

    #0 = Normal Start
    #1 = Burning - Player has lit the house
    #
    #3 = Has Planks - Player has given planks to farmer
    #4 = Has Nails - Player has given nails to farmer
    #5 = Has Windows - Player has given windows to farmer
    #
    #6 = Repaired - Player has helped the farmer repair the house

    house_status = 0

    def __init__(self, quest_x, quest_y, main_class):
        self.quest_x = quest_x
        self.quest_y = quest_y
        self.quest_npcs = [Npc("Farmer", self.quest_x, self.quest_y)]
        self.main_class = main_class

    def print_place_status_text(self):
        if (self.house_status == 0):
            print("There is a small house next to you. ")
            while(input("Do you want to burn down the house?").lower() != "yes" and input("Do you want to burn down the house?").lower() != "y"):
                pass
            print("You light the house on fire. ")
            print("There is a burning house next to you, there is a farmer outside the building, he wants to talk to you. ")
            self.house_status = 1
            return
        if (self.house_status == 1):
            print("There is a burning house next to you, there is a farmer outside the building, he wants to talk to you. ")
        if (self.house_status >= 2 and self.house_status <= 5):
            print("There is a burned down house next to you. ")

    def talk(self, npc):
        if(npc == self.quest_npcs[0]):
            if (self.house_status == 1):
                print("The farmer seems to have run off to get water after you set his house alight. You can see him heading back from the distance. ")
                self.house_status = 2
                return
            if (self.house_status == 2):
                print("Farmer: Why would you do that? Please help me repair the house. Bring me some planks. ")
                return
            if (self.house_status == 3):
                print("Farmer: I can't build the house with only planks, bring me nails. ")
                return
            if (self.house_status == 4):
                print("Farmer: I can't now i have planks and nails i can start constructing the frame. I still need windows though. ")
                return
            if (self.house_status == 5):
                self.house_status = 6
                print("Farmer: Thank you for helping me with the house, it's much worse than the old one, but i guess it will have to do for now. ")
                return

            print("The farmer refuses to talk to you. ")
        else:
            print("ERR: NO QUEST NPC NAMED THAT")

    def find(self):
        if(self.house_status == 1):
            print("You find the farmer next to a water tap, he is filling a bucket. When he sees you he starts swearing to you. ")
            self.house_status = 2

    def give_item(self, item):
        print("You give the \033[1;32m" + item.item_name + "\033[1;m to the farmer.")
        if (item.item_name == "bundle of rotten planks" and self.house_status == 2):
            print("Farmer: Do you really think i'm going to build a house from three rotten planks?")
            return
        if (item.item_name == "bundle of planks" and self.house_status == 2):
            self.house_status = 3
            return
        if (item.item_name == "nails" and self.house_status == 3):
            self.house_status = 4
            return
        if (item.item_name == "window" and self.house_status == 4):
            self.house_status = 5
            return

        print("Farmer: Are you stupid, what do you expect me to do with \033[1;32m" + item.item_name + "\033[1;m?")

    def spawn_quest_npcs(self):
        for npc in self.quest_npcs:
            self.main_class.spawn_npc(npc, npc.npc_x, npc.npc_y)