#List is used to represent hash table and chaining is used to handle collisions
table_size = 10
hash_table = [[] for _ in range(table_size)]  #list comprehension method. It is a variable, number of elements in the list depends on table size
#print(hash_table)
def hashing(key):
    return hash(key)%table_size
def insert(key, value):
    index = hashing(key)   
    for item in hash_table[index]:
        if item[0]== key:
            item[1] = value
            return 
    hash_table[index].append([key, value])
def display():
    for i, item in enumerate(hash_table):
        print("bucket", i, ":", item)
display()
insert("a", "apple")
insert("b", "bat")
insert("c", "cat")
print("After insertion:")
display()