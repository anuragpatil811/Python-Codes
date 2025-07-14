import json
import requests
#data = open("test.json", "r")
#print(data)
#print(data.read())
#print(type(data))

#Displaying contents of JSON
#myobj = json.load(data)
#print(myobj)
#print(type(myobj))

#Display index and the saary of the person
#print(myobj[1]["name"])

#Creating the json data
#obj = {
#    "Employee1": {"name": "Anurag", "skills": "AI Engineer"},
#    "Employee2": {"name": "Yash", "skills": "Django"}
#}

#print(type(obj))  # Output: <class 'dict'>

# Convert Python object to JSON string
#jsondata = json.dumps(obj, indent=4)  # Use indent for readability
#print(jsondata)

#convert file into string
#f = open("new.json", "w")
#f.write(jsondata)

#url = "https://jsonplaceholder.typicode.com/todos"
url = "https://jsonplaceholder.typicode.com/tod"
#response = requests.get(url)
#print(response)

#Content of data
#print(response.content)

#Text of data
#print(response.text)
#print(type(response.text))

#responseobj = json.loads(response.text)
#print(responseobj)

#Accessing the data in the dictionary and lists
#print(responseobj[0]["title"])

#POST request
response = requests.post(url, data={"userid": 1, "title": "My new Title"})

#Status code
print(response.status_code)

#Displaying data
print(response.text)
