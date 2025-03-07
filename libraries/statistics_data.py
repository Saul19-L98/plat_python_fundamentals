import statistics
import csv

#Read all montyly sales data from a csv file
monthly_sales = {}
with open('monthly_sales.csv', mode = 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

#Find the mean
mean_sales = statistics.mean(sales)
print(f"The media is: {mean_sales}")

#Find the median
median_sales = statistics.median(sales)
print(f"The median is: {mean_sales}")

#Find the mode
mode_sales = statistics.mode(sales)
print(f"The mode is: {mean_sales}")

#Standard desviation
stdev_sales = statistics.stdev(sales)
print(f"The standard desviation is: {stdev_sales}")

#Find the variance
variance_sales = statistics.variance(sales)
print(f"The variance is: {variance_sales}")

max_sales = max(sales)
min_sales = min(sales)
range_sales = max_sales - min_sales
print(f"Range of sales: {range_sales}")
