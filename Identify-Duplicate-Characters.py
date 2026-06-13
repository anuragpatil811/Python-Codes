def find_duplicates(s):
    seen = set()
    duplicates = []
    for i in s:
        if i in seen:
            if i not in duplicates:
                duplicates.append(i)
        else:
            seen.add(i)
    return duplicates 
s = input("Enter a string:")
print(find_duplicates(s))