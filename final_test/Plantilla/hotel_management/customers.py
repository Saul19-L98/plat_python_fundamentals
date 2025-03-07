class Customer:
    def __init__(self, customer_id, customer_name, email):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email

class CustomerManagement:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        """Agrega un nuevo cliente al sistema."""
        self.customers[customer.customer_id] = customer
        print(f"Cliente {customer.customer_name} añadido al sistema.")

    def get_customer(self, customer_id):
        """Obtiene la información de un cliente por ID."""
        if customer_id in self.customers:
                return self.customers[customer_id]
        else:
            print(f"Cliente {customer_id} no existe.")
            return None