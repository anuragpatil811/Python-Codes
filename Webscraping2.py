import requests
webpage = requests.get('https://www.w3schools.com/')
print(webpage)
from bs4 import BeautifulSoup
soup = BeautifulSoup(webpage.text, 'lxml')
print(soup.find('h1').text)
for i in soup.findAll('h1'):  
    print(i.text)