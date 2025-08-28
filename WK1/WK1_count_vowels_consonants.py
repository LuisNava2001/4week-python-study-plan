"""
    WEEK 1: Python Fundamentals & Clean Code
    Focus: Core Python, clean code habits, functions, error handling, and OOP basics.
"""
"""
    Monday | Exercise 1
    Python syntax, loops, conditionals, functions
    Write a function that takes a string and counts vowels/consonants.
"""
def count_vowels_consonants():
    while True:
        answer = input("Please, select and option; \n1. Write your sentence. \n2. Use an example. \n")
        if answer == '1' or answer == '2':
            if answer == '1':
                string = input("Please type a word or a sentence: \n\n")
            elif answer == '2':
                string = 'Hello, this is a string for example, thank you.'
            break
        else:
            print("Invalid option! Please input just 1 or 2...\n")
    vowels_set  = set('aeiouAEIOU')
    vowels_num = 0
    vowels_found = ""
    consonants_num = 0
    consonants_found = ""
    for char in string:
        if char.isalpha():
            if char in vowels_set:
                vowels_found += char
                vowels_num += 1
            else:
                consonants_found += char
                consonants_num += 1
    print(f"Vowels found: {vowels_found} and number of vowels: {vowels_num}")
    print(f"Consonants found: {consonants_found} and number of consonants: {consonants_num}")