def even_numbers(limit):
    a = 0
    while a <= limit:
        if a % 2 == 0:
            yield a
        a = a + 1

def uneven_numbers(limit):
    a = 0
    while a <= limit:
        if a % 2 != 0:
            yield a
        a = a + 1

print("Even numbers generator")
for num in even_numbers(12):
    print(num)

print("Even numbers generator")
for num in uneven_numbers(12):
    print(num)
