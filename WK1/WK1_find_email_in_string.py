"""
    WEEK 1: Python Fundamentals & Clean Code
    Focus: Core Python, clean code habits, functions, error handling, and OOP basics.
"""
"""
    Wednesday | Exercise 3
    String manipulation, f-strings, regex basics
    Parse an email from a messy string using regex.
"""
import re

def find_email_in_string():
    while True:
        answer = input("Please, select and option; \n1. Write your own input (email). \n2. Use an example. \n")
        if answer == "1" or answer == "2":
            if answer == "1":
                messy_string = input("Please input a brief description about yourself and your email please.\n")
            elif answer == "2":
                messy_string = "Hello, my name is Luis Nava and my email is Example_email@qmmcmx.com if you want to contact me\n"
                print(messy_string)
            pattern = r'\S+@\S+'
            break
        else:
            print("Invalid option! Please input just 1 or 2...\n")
    match = re.search(pattern, messy_string)
    if match:
        email_address = match.group(0)
        print(f"Email Address: {email_address}")
    else:
        print("Not email found. ")