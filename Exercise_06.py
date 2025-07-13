#Q.1)WAP: to read file content from a file and use error handling
"""""
try:
    file_loc = "sample.txt"
    with open(file_loc, "r") as file:
        content = file.read()
        print(content)
        file.close()
except FileNotFoundError:
    print("File not found on that location")
except Exception as e:
    print(f"An Error Occurred{e}")
    """
#Q.2)WAP: to count lines in file
"""""
try:
    file_loc = "sample.txt"
    with open(file_loc, "r") as file:
        content = file.read()
        #print(file.read())
        #print(file.read())
        print(content)
        file.seek(0)
        lines_count = 0
        for line in file:
            #print(line)
            lines_count += 1
        print(f"Total lines in file: {lines_count}")
        file.close()
except FileNotFoundError:
    print("File not found on that location")
except Exception as e:
    print(f"An Error Occurred{e}")
"""
#Q.3)WAP: to count word frequency in file
"""""
try:
    file_loc = "sample.txt"
    with open(file_loc, "r") as file:
        content = file.read()
        print(content)
        words = content.split()
        #print(words)
        print("Total Words in File:", len(words))
        word_count = {}
        for word in set(words):
            word_count[word] = words.count(word)
        for key, value in word_count.items():
            print(key, value)
        file.close()
except FileNotFoundError:
    print("File not found on that location")
except Exception as e:
    print(f"An Error Occurred{e}")"
    """
#Q.4)WAP: to write content in file and use error handling
try:
    file_loc = "sample1.txt"
    content = input("Enter file content:")
    with open(file_loc, "w") as file:
        file.write(content)
        file.close()
except Exception as e:
    print(f"An Error Occurred{e}")