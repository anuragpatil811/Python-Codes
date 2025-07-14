import os
import requests
import multiprocessing
# Create the 'files' directory if it doesn't exist
if not os.path.exists("files"):
    os.makedirs("files")

def downloadfile(URL, name):
    request = requests.get(URL)
    # Save the file in the 'files' directory
    with open(f"files/file{name}.jpg", "wb") as file:
        file.write(request.content)
    print("Finished Download")

URL = "https://picsum.photos/200/300"
#for i in range(10):
#    print("Starting download")
    #downloadfile(URL, i)
#    p = multiprocessing.Process(target=downloadfile, args=[URL, i])
#OR
if __name__ == "__main__":
    for i in range(10):
        print("Starting download")
        #downloadfile(URL, i)
        p = multiprocessing.Process(target=downloadfile, args=[URL, i])
