import os
import sys
import numpy as np
from Place import Place
from Item import Item
from Quest import QUEST_FarmerHouse
from Npc import Npc


#
#0 = Fields # EMPTY
#1 = Forest
#2 = Forest Clearing
#3 = City
#4 = Forest Entrance
#5 = Lake
#6 = Grain Field
#7 = House
#8 = Wind Mill
#9 = Path
#10 = Forest Path


class DungeonGame:

    #map_locations
    player_x = 17
    player_y = 11

    #Quest reference
    #0 - Farmers house
    quests = [None]

    npcs = []

    inventory = [30]
    map_locations = np.zeros((20, 20), dtype=np.object);
    temp_map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,5,5,5,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0],
                [0,5,5,5,5,5,0,0,0,0,3,3,0,0,0,5,5,5,0,0],
                [0,5,5,5,5,9,9,9,9,3,3,3,3,0,0,0,5,5,5,0],
                [0,5,5,5,5,0,0,0,9,3,3,3,3,0,9,9,5,5,5,0],
                [0,0,5,5,0,0,0,0,9,3,3,3,0,0,9,0,0,5,0,0],
                [0,0,0,0,0,1,1,0,9,0,3,3,0,0,9,0,0,0,0,0],
                [0,0,0,0,1,1,4,9,9,0,0,0,9,9,9,0,0,0,0,0],
                [0,0,0,1,1,1,1,1,9,0,0,0,9,6,6,6,6,6,0,0],
                [0,0,0,1,1,1,1,1,9,9,8,9,9,6,6,6,6,6,0,0],
                [0,0,0,0,1,1,4,9,9,0,0,0,9,6,6,6,6,6,0,0],
                [0,0,0,0,0,1,1,0,0,0,0,0,9,6,6,6,6,7,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,9,9,9,9,9,9,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


    def __init__(self):
        self.quests[0] = QUEST_FarmerHouse(17, 11, self)
        self.inventory[0] = Item("hands", 1)
        self.print_hello_screen()
        self.generate_map()
        self.generate_npcs()

        while(True):
            self.draw_screen(self.player_x, self.player_y)
            self.print_map()
            self.print_npcs()
            self.print_quest_texts()
            self.parse_input(input(">"))

    def print_quest_texts(self):
        for quest in self.get_quests_in_curr_tile():
            quest.print_place_status_text()

    def print_npcs(self):
        for npc in self.get_npcs_in_curr_tile():
            print(npc.get_npc_context_text())

    def print_map(self):
        for locations_x in self.map_locations:
            text_line = ""
            for location in locations_x:
                type = location

                if (type == 0):
                    text_line += "."
                if (type == 1):
                    text_line += "."
                if (type == 2):
                    text_line += "."
                if (type == 3):
                    text_line += "."
                if (type == 4):
                    text_line += "."
                if (type == 5):
                    text_line += "."
                if (type == 6):
                    text_line += "."
                if (type == 7):
                    text_line += "."
                if (type == 8):
                    text_line += "."
                if (type == 9):
                    text_line += "."
                if (type == 10):
                    text_line += "-"
            print(text_line)

    def generate_npcs(self):
        for quest in self.quests:
            quest.spawn_quest_npcs()

    def parse_input(self, player_input):
        os.system('cls' if os.name == 'nt' else 'clear')


        player_input = player_input.split()

        try:
            verb = player_input[0].lower()
        except:
            verb = ""

        try:
            object = player_input[1].lower()
        except:
            object = ""

        try:
            adjective = player_input[2].lower()
        except:
            adjective = ""

        try:
            adjective_object = player_input[3].lower()
        except:
            adjective_object = ""

        if (verb == "n"):
            self.move(0, -1)
            return
        if (verb == "s"):
            self.move(0, 1)
            return
        if (verb == "w"):
            self.move(-1, 0)
            return
        if (verb == "e"):
            self.move(1, 0)
            return

        if(verb == "go"):
            if (object == "up" or object == "north" or object == "n"):
                self.move(0, 1)
                return
            if (object == "down" or object == "south" or object == "s"):
                self.move(0, -1)
                return
            if (object == "right" or object == "east" or object == "e"):
                self.move(1, 0)
                return
            if (object == "left" or object == "west" or object == "w"):
                self.move(-1, 0)
                return
            print("Are you a moron?")
            return

        if(verb == "kill"):
            if(object == ""):
                print("Who do you want to kill?")
                return
            if(adjective != "with" or adjective_object == ""):
                print("With what?")
                return


            for npc in self.get_npcs_in_curr_tile():
                if(npc.npc_name.lower() == object):
                    for item in self.inventory:
                        if(item.item_name.lower() == adjective_object):
                            if(not item.is_weapon()):
                                print("How the hell are you going to kill a " + npc.npc_name + "\033[1;m with a \033[1;32m" + item.item_name + "\033[1;m")
                            else:
                                self.kill_npc(npc, item)
                            return
                    print("You don't have a \033[1;32m" + adjective_object + "\033[1;m")
                    return
            print("There isn't a \033[1;36m" + object + "\033[1;m near you.")
            return

        if(verb == "inventory" or verb == "inv"):
            self.show_inventory()
            return

        if(verb == "drop"):
            for item in self.inventory:
                if (item.item_name.lower() == object):
                    self.inventory.remove(item)
                    self.map_locations[self.player_x][self.player_y].ground_items.append(item)

                    print("You drop \033[1;32m" + item.item_name + "\033[1;m on the ground.")
                    return
            print("You don't have \033[1;32m" + object + "\033[1;m in your inventory.")
            return

        if(verb == "search" and object == "ground"):
            self.map_locations[self.player_x][self.player_y].print_ground_items()
            return

        if(verb == "search"):
            print("Search what?")
            return

        if(verb == "pick" and object == "up"):
            for item in self.map_locations[self.player_x][self.player_y].ground_items:
                if (item.item_name.lower() == adjective):
                    self.map_locations[self.player_x][self.player_y].ground_items.remove(item)
                    self.inventory.append(item)

                    print("You pick up \033[1;32m" + item.item_name + "\033[1;m from the ground.")
                    return
            print("There isn't a \033[1;32m" + adjective + "\033[1;m on the ground.")
            return

        if(verb == "look" and object == "up" and (self.map_locations[self.player_x][self.player_y].place_type == 0 or self.map_locations[self.player_x][self.player_y].place_type == 1)):
            print("You see the sky above you.")
            return

        if ((verb == "look" and object == "down") or ((verb == "look" and object == "at") and (adjective == "ground" or adjective == "floor"))):


            for item in self.map_locations[self.player_x][self.player_y].ground_items:
                print("You see some items on the ground")
                return

            print("You look down and see the ground.")
            return

        if(verb == "look"):
            print("Look at what?")
            return

        if(verb == "talk"):
            if(object == ""):
                print("Who do you want to talk to?")
                return

            for npc in self.get_npcs_in_curr_tile():
                if(npc.npc_name.lower() == object):
                    for quest in self.quests:
                        for quest_npc in quest.quest_npcs:
                            if(npc == quest_npc):
                                quest.talk(npc)
                                return
                    print("He doesn't want to talk to you.")
                    return
            print("There isn't a \033[1;36m" + object + "\033[1;m near you.")
            return

        if(player_input == "stgame"):
            sys.exit()
            print("Exiting game.")

        print("I don't understand what you are saying.")
        return

    def show_inventory(self):
        for item in self.inventory:
            print(str(item.amount) + "x " + item.item_name)

    def move(self, x_dir, y_dir):
        if(self.player_x + x_dir > 18 or self.player_y + y_dir > 12 or self.player_x + x_dir < 0 or self.player_y + y_dir < 0):
            print("There is a steep cliff there.")
            return
        self.player_x += x_dir
        self.player_y += y_dir

    def generate_map(self):
        #for x in range(0, 20):
        #    for y in range(0, 20):
        #        if(x == 1 and y == 1):
        #            self.map_locations[x][y] = Place(1)
        #        else:
        #            self.map_locations[x][y] = Place(0)
        for x in range(0, 19):
            for y in range(0, 13):
                self.map_locations[x][y] = Place(self.temp_map[y][x], self, x, y)

    def draw_screen(self, x, y):
        print("(" + str(x) + "; " + str(y) + ") -- " + self.map_locations[x][y].get_place_context_text())

    def print_hello_screen(self):
        print("Hello and welcome to the Mega Procedural Dungeon Game(tm).")

    def spawn_npc(self, npc, x, y):
        self.npcs.append(npc)

    def kill_npc(self, npc, with_what):
        print("-------------------------------------------")
        print("You kill \033[1;32m" + npc.npc_name + "\033[1;m with \033[1;36m" + with_what.item_name + "\033[1;m")

        for item in npc.has_items:
            self.map_locations[npc.npc_x][npc.npc_y].append(item)

        self.npcs.remove(npc)

    def print_npc_context_text(self):
        for npc in self.get_npcs_in_curr_tile():
            print(npc.get_npc_context_text())

    def get_npcs_in_curr_tile(self):
        return_npcs = []
        for npc in self.npcs:
            if(npc.npc_x == self.player_x and npc.npc_y == self.player_y):
                return_npcs.append(npc)
        return return_npcs

    def get_quests_in_curr_tile(self):
        return_quests = []
        for quest in self.quests:
            if (quest.quest_x == self.player_x and quest.quest_y == self.player_y):
                return_quests.append(quest)
        return return_quests
a = DungeonGame()