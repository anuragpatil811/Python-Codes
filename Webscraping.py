import requests
webpage = requests.get('https://www.geeksforgeeks.org/courses?source=google&medium=cpc&device=c&keyword=geeksforgeeks&matchtype=p&campaignid=20039445781&adgroup=147845288105&gad_source=1&gad_campaignid=20039445781&gbraid=0AAAAAC9yBkDIZOOwkMdlfx7NPggxjYkul&gclid=CjwKCAiAkvDMBhBMEiwAnUA9BTShltprTVm1JaGZkH3ZW3hk9lWnd50F-dq3VQZ0nPdBN3lUZT0dYhoC29YQAvD_BwE')
print(webpage)

#BEAUTIFULSOUP
from bs4 import BeautifulSoup
soup = BeautifulSoup(webpage.text, 'lxml')
print(soup.find('h2').text)
for i in soup.findAll('h2'):
    print(i.text)
