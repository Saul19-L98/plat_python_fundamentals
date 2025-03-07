import csv

#Read a file
"""with open("products.csv",mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

#Show information by columns
"""with open("products.csv",mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Prodcut: {row['name']}, Price: {row['price']}")"""

#Add new data to a file
new_product = {
    'name':"Wireless charger",
    'price':"75",
    'quantity': 100,
    'brand':'ChargerMaster',
    'category':'Accesories',
    'entry_date': '2024-07-01'
}

with open('products.csv',mode='a',newline='') as file:
    file.write('')
    csv_write = csv.DictWriter(file,fieldnames = new_product.keys())
    csv_write.writerow(new_product)
