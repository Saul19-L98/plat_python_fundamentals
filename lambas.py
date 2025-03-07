add = lambda a,b: a + b
print(add(10,4))

multiply = lambda a,b: a * b
print(add(80,5))

numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)
