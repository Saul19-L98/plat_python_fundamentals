from collections import Counter

def count_sales(products: list[str]) -> Counter:
    #Use counter to count how many products are of each type have been sold.
    return Counter(products)

sales = ["laptop","smarthphone","laptop","smarthphone","tablet"]
result = count_sales(sales)
print(result)