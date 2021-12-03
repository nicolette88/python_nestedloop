#1. Feladat
from typing import List

print('---1. Feladat---')

m = [[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3], [4, 4, 4, 3, 4]]

print("Matrix: " + str(len(m)) + "x" + str(len(m[0])))
print("m = " + str(m))
sum = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        sum += m[i][j]

print("\nAz eredmény: " + str(sum))

# 2. Feladat
print('---2. Feladat---')

cars = [
    {
        "price": 1549,
        "passengerQty": 4,
        "currency": "EUR",
        "type": "Kia",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 1954,
        "passengerQty": 5,
        "currency": "EUR",
        "type": "Suzuki",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 5,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 2,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
    {
        "price": 9542,
        "passengerQty": 4,
        "currency": "USD",
        "type": "Ford",
        "transmission": "automatic",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
]

# Első működő megoldás -> a sok warning miatt készült el az átirat
# for i in range(len(cars)):
#     if (cars[i]["passengerQty"] < len(cars[i]["passengers"])):
#         print("a(z) " + cars[i]["type"] + " típusú autóban túl sok az utas")

# Második megoldás (átirat)
for d_id, d_info in enumerate(cars):
    passengersLength = 0
    passengerQtyNum = 0
    tmpVal = d_info["passengers"]
    passengersLength = len(str(tmpVal).split(", "))
    passengerQtyNum = int(str(d_info["passengerQty"]))
    if (passengerQtyNum < passengersLength):
        print("a(z) " + str(d_info["type"]) +
              " típusú autóban túl sok az utas")

# 3. Feladat
print('---3. Feladat---')

# Első működő megoldás -> a sok warning miatt készült el az átirat
# exchangeRate = 1.16
# print("EUR-USD exchange rate 2021.11.02: " + str(exchangeRate))
# for i in range(len(cars)):
#     if(cars[i]["currency"] == "EUR"):
#         cars[i]["currency"] = "USD"
#         cars[i]["price"] = int(cars[i]["price"]*exchangeRate)
#         print(cars[i]["type"] + " " + str(cars[i]["price"]) + " " + cars[i]["currency"])

# Második megoldás (átirat)
exchangeRate = 1.16
print("EUR-USD exchange rate 2021.11.02: " + str(exchangeRate))
for k_id, k_info in enumerate(cars):
    if (str(k_info["currency"]) == "EUR"):
        k_info["currency"] = "USD"
        k_info["price"] = int(int(str(k_info["price"])) * exchangeRate)
        print(
            str(k_info["type"]) + " " + str(k_info["price"]) + " " +
            str(k_info["currency"]))

# 4. Feladat
print('---4. Feladat---')

persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

for i in range(len(persons)):
    for j in range(len(restaurants)):
        print(persons[i] + " eats " + restaurants[j])

# 5. Feladat
print('---5. Feladat---')

my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]
print("my_list = " + str(my_list))

for i in range(len(my_list)):
    sum = 0
    for j in range(len(my_list[i])):
        sum += my_list[i][j]
    my_list[i].append(sum)

print(my_list)
