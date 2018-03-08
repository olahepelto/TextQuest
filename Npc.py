from Item import Item

class Npc:
    npc_name = "ERR"
    npc_x = 0
    npc_y = 0
    has_items = {}

    def __init__(self, npc_name, x, y):
        self.npc_name = npc_name
        self.has_items = self.generate_items()
        self.npc_x = x
        self.npc_y = y

    def generate_items(self):
        return {Item("Axe", 1)}

    def get_npc_context_text(self):
        return "\nThere is a \033[1;32m" + self.npc_name + "\033[1;m standing in front of you. "