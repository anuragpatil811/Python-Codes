table_size = 10
hash_table = [None] * table_size
DELETED = object()
def hashing(key):
    return hash(key)%table_size
def insert(key, value):
    index = hashing(key)
    original_index = index
    while hash_table[index] is not None and hash_table[index] is not DELETED:
         if hash_table[index][0]==key:
             hash_table[index][1] = value
             return
         index = (index+1)%table_size
         if index == original_index:
#             raise Exception("HashTable is FULL")
              print("HashTable is FULL")
              return             
    hash_table[index] = (key, value)
def search(key):
    index = hashing(key)
    original_index = index
    while hash_table[index] is not None:
        if hash_table[index] is not DELETED and hash_table[index][0]==key:
            return hash_table[index][1]
        index = (index+1)%table_size
        if index == original_index:
            break
    return None
def display():
    for i, item in enumerate(hash_table):
        if item is DELETED:
            print("index", i, ":DELETED")
        else:
            print("index", i, ":", item)
def delete(key):
    index = hashing(key)
    original_index = index
    while hash_table[index] is not None:
        if hash_table[index] is not DELETED and hash_table[index][0]==key:
             hash_table[index] = DELETED
             return True
        index = (index+1)%table_size
        if index == original_index:
            break
    return False 
print("****beginning****")
display()
print("-----------------")
insert("a", "apple")
insert("b", "bat")
insert("c", "cat")
print("after insertion:")
display()
print("-----------------")

print("Search Operation:")
print("value of key a:", search("a"))
print("-----------------")

delete("a")
print("after deletion:")
display()