from bs4 import BeautifulSoup
import requests
import os

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
print(str(data['verified'])) #verified
print(str(data['website'])) #website
filepath = None
if len(data['picture']) > 0:
    photo = data['picture']['300'][:-6] + "U0.jpg"
    print(photo)
    try:
        os.mkdir(f"downloads/Avatars/")
    except OSError:
        print("Creation of the directory failed or the folder already exists ")
    req = requests.get(photo)
    filepath = f'downloads/Avatars/42803449.jpeg'
    if not os.path.isfile(filepath):
        with open(filepath, 'wb') as f:
            f.write(req.content)
        print(f"Avatar saved to {filepath}")
else:
    print('File already exists, skipped.')

#https://webapi.depop.com/api/v1/shop/42803449/products/?limit=10
#then, we can input the id into this url, and receive a limit of 10 items.