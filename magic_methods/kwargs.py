def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Karla",age=30,city="California")
