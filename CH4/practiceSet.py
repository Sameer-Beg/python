# 1. Write a program to store seven fruits in a list entered by the user.
fruits = []
f1 = input("Enter the name of fruit 1: ")
fruits.append(f1)
f2 = input("Enter the name of fruit 2: ")      
fruits.append(f2)
f3 = input("Enter the name of fruit 3: ")   
fruits.append(f3)
f4 = input("Enter the name of fruit 4: ")   
fruits.append(f4)
print(fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner
marks = []
m1 = int(input("Enter the marks of student 1: "))
marks.append(m1)
m2 = int(input("Enter the marks of student 2: "))
marks.append(m2)
m3 = int(input("Enter the marks of student 3: "))
marks.append(m3)
m4 = int(input("Enter the marks of student 4: "))
marks.append(m4)
print("Marks of students in unsorted manner: ", marks)
marks.sort()    
print("Marks of students in sorted manner: ", marks)

# 4. Write a program to sum a list with 4 numbers.
# numbers = []
# n1 = int(input("Enter number 1: ")) 
# numbers.append(n1)
# n2 = int(input("Enter number 2: "))
# numbers.append(n2)
# n3 = int(input("Enter number 3: "))
# numbers.append(n3)
# n4 = int(input("Enter number 4: "))
# numbers.append(n4)
# print(sum(numbers))


# 5. Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)
a = (7, 0, 8, 0, 0, 9)
a.count(0)  #count method returns the count of the given element in the tuple
print(a.count(0 ))