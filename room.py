class Room():  
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
    def set_description(self, new_description):
        self.description = new_description
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
    def get_details(self):
        print(self.name)
        print("-------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.name + " is " + direction)
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
    def set_character(self, new_character):
        self.character = new_character
    def get_character(self):
        return self.character
