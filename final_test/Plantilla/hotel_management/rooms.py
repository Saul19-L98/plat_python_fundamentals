class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.available = True

class RoomManagement:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        """Agrega una nueva habitación al sistema."""
        self.rooms[room.room_number] = room
        print(f"Habitación {room.room_number} añadida al sistema.")
        

    def check_availability(self, room_number):
        """Verifica si una habitación está disponible."""
        if room_number in self.rooms:
            if self.rooms[room_number].available:
                print(f"Habitación {room_number} está disponible.")
                return True
            else:
                print(f"Habitación {room_number} no está disponible.")
                return False
        else:
            print(f"Habitación {room_number} no existe.")
            return False