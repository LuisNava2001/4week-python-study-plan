"""
    WEEK 1: Python Fundamentals & Clean Code
    Focus: Core Python, clean code habits, functions, error handling, and OOP basics.
"""
"""
    Friday | Exercise 5
    Error handling & logging
    Write a script that reads a file, logs errors if not found.
"""
def read_file_with_error_handling():
    while True:
        answer = input("Please, select and option; \n1. Write the name of your file. \n2. Use an example. \n")
        if answer == "1" or answer == "2":
            if answer == "1":
                print("Please, write the full name of your file including the extension\nExample: example.txt")
                filename = input("Writhe the name:\n  ")
            if answer == '2':
                filename = 'Example.txt'
            break
        else:
            print("Invalid option! Please input just 1 or 2...")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Successfully read the file '{filename}'.")
            print("--- File Content ---")
            print(content)
            print("--------------------")
    except FileNotFoundError:
        print(f"ERROR! The file: {filename} was not found!!")
    except Exception as e:
        print(f"An unexpected error occurred {e}")