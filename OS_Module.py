import os
#print(os) #Program to print OS module

#Display current working directory
#cwd = os.getcwd()
#print(cwd)

#Change the directory
#os.chdir("D:/")
#print(os.getcwd())

#Check the list of available files in another directory
#print(os.listdir(cwd))
#print(os.listdir("D:/"))

#Create a Directory
#path = os.path.join(cwd, "Temp")
#os.mkdir(path)
#os.chdir("D:/Python Tutorial/Temp")
#print(os.getcwd())
#open("New.txt", "w")

#Renaming a file
#os.rename("New.txt", "My.txt")

#Get the size of file
#open("My.txt", "w")
#print(os.path.getsize("My.txt"))

#Remove directory
os.chdir("D:/Python Tutorial")
print(os.getcwd())

#Remove Temp folder
path = os.path.join(print(os.getcwd()), "Temp")
os.rmdir(path) #We cannot remove any non-empty directory
