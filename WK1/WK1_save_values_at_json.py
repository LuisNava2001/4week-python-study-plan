"""
    WEEK 1: Python Fundamentals & Clean Code
    Focus: Core Python, clean code habits, functions, error handling, and OOP basics.
"""
"""
    Thursday | Exercise 4
    File I/O & JSON
    Save a Python dict to JSON, reload it, and print.
"""
import json

def save_values_at_json():
    data = {}
    while True:
        answer = input("Please, select and option; \n1. Write your own dictionary. \n2. Use an example. \n")
        if answer == "1" or answer == "2":
            if answer == "1":
                for x in range(3):
                    category = input(f"Please write the {x+1} Category.\n ")
                    value = input(f"Please write the {x+1} Value.\n ")
                    data[category] = value
            if answer == "2":
                data = {
                    "Fruits" : ["Apple, Orange, Grape, Watermelon, Bannana"],
                    "Vegetables" : ["Tomatoe, Onion, Potatoe"],
                    "Milk and Cheese" : ["Milk, Cheese, Buttermilk, Yougurth"],
                    "Groceries" : ["Soap, Detergent"]
                }
            break
        else:
            print("Invalid option! Please input just 1 or 2...")

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print("We already saved the dictionary in a JSON file:")

    with open('data.json', 'r') as json_file:
        loaded_data = json.load(json_file)
    
    print(f"We loaded the data from the json file and printed: {loaded_data}")