from bs4 import BeautifulSoup
import os
from PIL import Image
import requests
from io import BytesIO

url = url = f"https://webapi.depop.com/api/v1/shop/halfugly/"
print(url)
data = requests.get(url).json()

print(str(data['id'])) #gives actual user ID for shop!
print(str(data['last_seen'])) #last_seen 
str(data['bio']).encode("UTF-8") #bio 
str(data['followers']) #followers 
str(data['following']) #following
print(str(data['items_sold'])) #items_sold 
print(str(data['last_name']).encode("UTF-8")) #last_name
print(str(data['first_name']).encode("UTF-8")) #first_name
print(str(data['reviews_rating'])) #reviews_rating 
print(str(data['reviews_total'])) #reviews_total
print(str(data['username'])) #username
print(str(data['bio'])) #bio
print(str(data['verified'])) #verified
print(str(data['website'])) #website
if len(data['picture']) > 0:
    photo = data['picture']['450'][:-6] + "U0.jpg"
else:
    print('File already exists, skipped.')
response = requests.get(photo)
img = Image.open(BytesIO(response.content))
img.show()
#https://webapi.depop.com/api/v1/shop/42803449/products/?limit=10
#then, we can input the id into this url, and receive a limit of 10 items.