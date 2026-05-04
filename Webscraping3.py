import requests
#Search my user agent on browser
headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}
webpage = requests.get('https://www.sarvam.ai/', headers = headers)
print(webpage)
from bs4 import BeautifulSoup
soup = BeautifulSoup(webpage.text, "lxml")
print(soup.find('h1').text)
for i in soup.find_all('h1'):
    print(i.text)