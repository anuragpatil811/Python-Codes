my_dictionary = { }
#insertion
my_dictionary["a"] = "apple"
my_dictionary["b"] = "bat"
my_dictionary["c"] = "cat"
my_dictionary["d"] = "dog"
#print(my_dictionary) 

#search
print("value is:", my_dictionary["a"])
print("value is:", my_dictionary["c"])
print("value is:", my_dictionary["d"])
#print(my_dictionary)

#delete
del my_dictionary["a"]
del my_dictionary["d"]
print(my_dictionary)