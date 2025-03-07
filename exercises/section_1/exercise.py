#Exercise 1
print("---Exercie 1---")
list=[1,2,3,4,5]
double_list=[x*2 for x in list] 
print("List 1: ",list)
print("Result 1:", double_list)

#Exercie 2
print("---Exercie 2---")
words=["sol","mar","montaña","rio","estrella"]
words_validation=[ len(word) == 3 for word in words]
words_result=[word for word in words if len(word) == 3]
print("Words: ",words)
print("Words validation: ", words_validation)
print("Word with 3 letters: ",words_result)

#Exercie 3
print("---Exercie 3---")
keys=["nombre","edad","ocupacion"]
values=["Juan",30,"Ingeniero"]
dictionary={ keys[key]:values[key] for key in range(len(keys))}
print(dictionary)

#Exercie 5
print("---Exercie 5---")
persons  = [
    {"name": "Juan", "age": 25, "city": "Madrid"},
    {"name": "Ana", "age": 32, "city": "Madrid"},
    {"name": "Pedro", "age": 35, "city": "Barcelona"},
    {"name": "Laura", "age": 40, "city": "Madrid"}
]
persons_filtered=[ person for person in persons if person["city"] == "Madrid" and person["age"] > 30]
print(persons_filtered)

#Exercie 6
print("---Exercie 6---")
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers_calculation=[ number * 2 if number % 2 == 0 else number for number in numbers]
print(even_numbers_calculation)
