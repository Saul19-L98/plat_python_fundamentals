import asyncio
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment
from datetime import datetime

async def main():
    # Inicializar sistemas
    room_mgmt = RoomManagement()
    customer_mgmt = CustomerManagement()
    reservation_sys = ReservationSystem(room_mgmt, customer_mgmt)
    # Crear habitaciones
    room1 = Room(1, "Sencilla", 100)
    room2 = Room(2, "Doble", 200)
    room3 = Room(3, "Suite", 300)
    room_mgmt.add_room(room1)
    room_mgmt.add_room(room2)
    room_mgmt.add_room(room3)

    # Agregar clientes
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer2 = Customer(2, "Bob", "bob@example.com")
    customer_mgmt.add_customer(customer1)
    customer_mgmt.add_customer(customer2)

    # Verificar disponibilidad de habitaciones
    if room_mgmt.check_availability(1):
        reservation = Reservation(1, "Alice", 1, datetime.now(), datetime.now())
        reservation_sys.add_reservation(reservation)
        # Procesar pago asincrónicamente
        await process_payment(1, 100)

if __name__ == "__main__":
    asyncio.run(main())

