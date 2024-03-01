class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    def describe(self):
        print(self.name + " is here!")
        print(self.description)
    def set_conversation(self, conversation):
        self.conversation = conversation
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print("Your " + combat_item + " is useless")
            print(self.name + " crushes you, puny adventurer")
            return False
    def bribe(self, item):
        if item == "gold":
            print(self.name + " has been bribed successfully with " + item + "! They let you pass.")
            return True
        else:
            print(self.name + " is not interested in " + item + ".")
            return False

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def hug(self):
        print(self.name + " smiles and hugs you back. It's nice to have friends.")
    def offer_gift(self, gift):
        if gift == "flower":
            print(self.name + " is delighted with the " + gift + "! Their happiness increases.")
            self.feeling = "happy"
        else:
            print(self.name + " appreciates the thought but doesn't seem interested in the " + gift + ".")
