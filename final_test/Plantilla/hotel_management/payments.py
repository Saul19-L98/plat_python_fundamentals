import asyncio
import random

async def process_payment(customer_name, amount):
    """Simula el procesamiento de un pago."""
    print(f"Procesando pago de {customer_name} por {amount}...")
    await asyncio.sleep(1)
    print(f"¡Pago de {amount} de {customer_name} procesado!")
    return True


