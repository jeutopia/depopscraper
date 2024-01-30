from bs4 import BeautifulSoup
import os
from PIL import Image
import requests
from io import BytesIO



url = f"https://webapi.depop.com/api/v1/shop/42803449/products/?limit=200"
data = requests.get(url).json()
print("fetching 200 items...")
#index products dictionary: description, price, 
#national_shipping_cost, sizes, sold, brandId, categoryId
x = 0
for item in data['products']:
    desc = str(item['description']).split("\n")[0]
    price = str(item['price']['price_amount'])
    shipping = str(item['price']['national_shipping_cost'])
    sizes = item['sizes']
    if sizes:
        size = sizes[0]
    else:
        size = 'x'
    
    if(item['sold']):
        sold = "sold"
    else:
        sold = "available"
    brandId = str(item['brandId'])
    categoryId = str(item['categoryId'])
    if categoryId == categoryId:
        print(desc + "\n" + price + "\n" + shipping + "\n" + size + "\n" + sold + "\n" + brandId + "\n" + categoryId)
        print("\n")
