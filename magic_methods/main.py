def add(a:int, b:int)->int:
    return a + b

def substract(a:int, b:int)->int:
    return a - b

def devide(a:int, b:int)->int:
    if b == 0:
        raise ValueError("The devisro can not be 0.")
    return a / b

def multiply(a:int, b:int)->int:
    return a * b

if __name__ == "__main__":
    print("Operations")
    res_1 = add(2,4)
    print(f"Add: {res_1}")