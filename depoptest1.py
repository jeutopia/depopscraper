from bs4 import BeautifulSoup
import requests
URL = "https://www.depop.com/halfugly/"
response = requests.get(URL).json()
response.raise_for_status()  # raises exception when not a 2xx response
if response.status_code != 204:
    print(response.json()) 
soup = BeautifulSoup(response, "html.parser")
exit
for tag in soup.find_all(class_="styles__ProductImageContainer-sc-9691b5f-3 TlTNt"):
    print(tag.text)