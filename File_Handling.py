#f = open("data.txt")
#print(f)
#print(f.read(15))
#print(f.readline())
#print(f.readline(10))

#f1 = open("datanew.txt", "w")
#f1.write("This is File Handling")
#f1.write("XYZ")

#f2 = open("datanew.txt", "a")
#f2.write("Queen")

#data = open("data.txt", "r+")
#data.write("Hello King")

file = open("data.txt", "r")
data = open("datanew.txt", "a")
#print(file.read())
for i in file:
    #print(i, end="")
    data.write(i)
#f1.close()
#f2.close()
file.close()
data.close()