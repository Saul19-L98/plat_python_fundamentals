from collections import defaultdict
from datetime import datetime

class Reservation:
    def __init__(self, reservation_id, room_number, customer_id, start_date, end_date):
        self.reservation_id = reservation_id
        self.room_number = room_number
        self.customer_id = customer_id
        self.start_date = start_date
        self.end_date = end_date
        self.cancelled = False

class ReservationSystem:
    def __init__(self, room_mgmt, customer_mgmt):
        self.reservations = {}
        self.room_mgmt = room_mgmt
        self.customer_mgmt = customer_mgmt
        

    def add_reservation(self, reservation):
        """Agrega una nueva reserva al sistema."""
        self.reservations[reservation.reservation_id] = reservation
        print(f"Reserva {reservation.reservation_id} añadida al sistema.")

    def cancel_reservation(self, reservation_id):
        """Cancela una reserva existente por ID."""
        if reservation_id in self.reservations:
            self.reservations[reservation_id].cancelled = True
            print(f"Reserva {reservation_id} cancelada.")
        else:
            print(f"Reserva {reservation_id} no existe.")


