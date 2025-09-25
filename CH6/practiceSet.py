# 1. Write a program to find the greatest of four numbers entered by the user
a = int(input("Enter the number 1 .."))
b = int(input("Enter the numbert 2 .."))
c = int(input("Enter the numer 3 "))
d = int(input("Enter the  number 4 ..  "))
if(a >= b and a >= c and a >= d):
    print("The greatest number is ", a)
elif(b>=-a and b >= c and b >= d):
    print("The greatest number is ", b)
elif(c >= a and c >= b and c >= d):
    print("The greatest number is ", c)
else:
    print("The greatest number is ", d)
print("Done")

# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user
sub1 = int(input("Enter the marks of subject 1: "))
sub2 = int(input("Enter the marks of subject 2: "))
sub3 = int(input("Enter the marks of subject 3: "))
total = (sub1 + sub2 + sub3) / 3
if(total >= 40 and total >= 33):
    print("yes student is passesd")
else:
    print("Student is failed")

# 4. Write a program to find whether a given username contains less than 10 characters or not.
username = input("Enter the username: ")
if(len(username)<10):
    print ("Username is valid   ")
else:
    print("Username is not valid")

    # 5. Write a program which finds out whether a given name is present in a list or not.
name = ["sameer" , "sahil" , "subhan"]
if("subhan" in name    ):
    print("Name is present in the list")
else:
    print("Name is not present in the list")

# 7. Write a program to find out whether a given post is talking about “Harry” or not.
post = input("Enter the post: ")
if("Harry" in post):
    print("Yes, Harry is present in the post")
else:
    print("No, Harry is not present in the post")