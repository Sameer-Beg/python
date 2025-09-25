# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
words = {
    "aam":"mango",
    "kela":"banana",
    "seb":"apple",  
    "santra":"orange"
    }
word = input("Enter the woed u want to  search: ")
print(words[word])

# # 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
numbers = []
for i in range(8):
    n = int(input("Enter the number: "))
    numbers.append(n)   
unique_numbers = set(numbers)
print("The unique numbers are: ")
print(unique_numbers)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s = {18, '18'}
print(s)
print(type(s))


# 5. s = {} What is the type of 's'?
s = {}
print(s)
print(type(s))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
# favlang = {}

sam = input("Enter Sam's favorite language: ")
favlang["Sam"] = sam
jan = input("Enter Jan's favorite language: ")
favlang["Jan"] = jan
dan = input("Enter Dan's favorite language: ")
favlang["Dan"] = dan
van = input("Enter Van's favorite language: ")
favlang["Van"] = van
print(favlang)


# 9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
print(s)  # it will give an error because list is mutable and we cannot have mutable elements in set    