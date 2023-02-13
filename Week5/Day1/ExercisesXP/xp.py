class Door:
    def __init__(self) -> None:
        self.is_opened = False

    def open_door(self): 
        self.is_opened = True

    def close_door(self):
        self.is_opened = False

class BlockedDoor(Door):
    pass
   
    def open_door(self): 
        

    def close_door(self):
        Door.is_opened = "a blocked door cannot be opened or closed"


