# tuple, is a immutable data type
a = (1,2,3,"sameer", "beg")
print(a)
print(type(a))

# a[0] = "SAMEER"  #this will give error as tuple is immutable
# print(a) # this gives error bcz tuple is immutable

c = (1,2,3,4)
repeated = c*2
print(repeated)

# unpacking 
sam = (1,2,3)
x,y,z = sam
print(x,y,z)