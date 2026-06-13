group1 = [1, 2, 3, 4, 5]
search = int(input("Enter element to search:"))
for element in group1:
    if search == element:
        print("Element found in group 1")
        break
else:
    print("Element not found in group1")