#Short trick to remove duplicates from a list while preserving order of the list
old = ['a', 'b', 'a', 'c', 'b', 'a']
new = list(dict.fromkeys(old).keys())
print(new)