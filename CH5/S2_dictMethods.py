marks ={
    "Maths":90,
    "Science":80,  
    "English":85

}
print(marks.items())  # it will give all the items of dictionary in form of tuples
print(marks.keys())  # it will give all the keys of dictionary
print(marks.update({"Hindi":88}))  # it will update the dictionary by adding new key value pair
print(marks)
print(marks.get("Science"))  # it will give the value of the key mentioned  
print(marks.pop("English"))  # it will remove the key value pair of the key mentioned
print(marks)
print(marks.clear())  # it will clear the dictionary and make it empty
print(marks)
print(type(marks))