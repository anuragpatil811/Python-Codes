img = open("Image.jpeg", "rb")
nimg = open("Image2.jpeg", "wb")
#for i in img:
#    nimg.write(i)
img.close()
nimg.close()
print(img.read()) #We canot read the file after closing