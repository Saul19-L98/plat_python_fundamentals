def log_transaction(func):
    def wrapper():
        print("1 logging transaction...")
        func()
        print('Process terminated...')
    return wrapper

@log_transaction
def process_payment():
    print("2 Payment process...")
    
process_payment()