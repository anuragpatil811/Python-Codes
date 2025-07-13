import requests
from bs4 import BeautifulSoup
#query = input("Enter Search:")
#URL = "https://www.google.com/search?q="+query
#header = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
#"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#}
#response = requests.get(URL, headers=header)
#print(response.text) #Returns HTML text as output
#soup = BeautifulSoup(response.content, "html.parser")
#result = soup.find(class_ ="dodTBe").getText()
#print(result)
#result = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
#if result:
#    print(result.get_text())
#else:
#    print("No search result found.")
def search(task):
    URL = "https://www.google.com/search?q="+task
    header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
#"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
    response = requests.get(URL, headers=header)
    #print(response.text) #Returns HTML text as output
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find(class_ ="Z0LcW t2b5Cf").getText()
    return result
    
#print(result)
#result = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
#if result:
#    print(result.get_text())
#else:
#    print("No search result found.")
