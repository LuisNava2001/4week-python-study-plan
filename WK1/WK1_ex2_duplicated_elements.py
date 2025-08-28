"""
    WEEK 1: Python Fundamentals & Clean Code
    Focus: Core Python, clean code habits, functions, error handling, and OOP basics.
"""
"""
    Tuesday | Exercise 2
    Lists, dicts, sets, tuples
    Implement a function that finds duplicate elements in a list.
"""
def duplicated_elements():
    wall = []
    total_words_count = 0
    total_words_duplicated = 0
    seen = set()
    duplicated_words = []
    while True:
        answer = input("Please, select and option; \n1. Write your own list. \n2. Use an example. \n")
        if answer == '1' or answer == '2':
            if answer == '1':
                print("Write 5 objects for the list (Example: Fruits)")
                for x in range(5):
                    block = input(f"Write Object num {x}: ")
                    wall += [block]
                    print(f"Current list {wall}")
            if answer == '2':
                wall = ['Apple', 'Bannana', 'Grape', 'Orange', 'apple', 'Watermelon', 'Orange', 'bannana']
            break
        else:
            print("Invalid option! Please input just 1 or 2...\n")
    for sentence in wall:
        if sentence.casefold() in seen:
            duplicated_words += sentence.casefold()
            total_words_duplicated += 1
        seen.add(sentence.casefold())
        words = sentence.split()
        total_words_count += len(words)
    print(f"Total of words: {total_words_count}\nTotal of words duplicated: {total_words_duplicated}\nWords duplicated: {duplicated_words}")