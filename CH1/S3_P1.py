import os
# print the story of the python 
print (
    """
    The Python programming language was created by Dutch programmer Guido van Rossum in the late 1980s as a hobby project at the Centrum Wiskunde & Informatica (CWI) in the Netherlands

"""
)

# print the table os 5 
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# download any external module and run the code 
import pyttsx3
engine = pyttsx3.init()
# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"
engine.say("I will speak this text .  sameer is a good developer and he have a good developer skills ")
engine.runAndWait()

# write a program where u can see all the folders in your dicrectory 


# Use raw string to avoid escape errors
dp = r'C:\Users\Sameer Beg\OneDrive\Desktop'
content = os.listdir(dp)
for item in content:
    print(item)

