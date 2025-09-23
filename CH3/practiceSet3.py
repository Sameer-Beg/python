# Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name :")
print("Good Afternoon " + name)



# 2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|'''
namereplace = letter.replace("<|Name|>" , "Sameer")
print(namereplace)

# 3. Write a program to detect double space in a string.
st = "This is a string with  double spaces"
doublespace = st.find("  ")
print(doublespace)

# 4. Replace the double space from problem 3 with single spaces
st = "This is a string with  double spaces"
replcespace = st.replace("  " , "_____")
print(replcespace)