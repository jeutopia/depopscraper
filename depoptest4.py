from bs4 import BeautifulSoup
import os
from PIL import Image
import requests
from io import BytesIO
import random

pants = ['3', '36', '107', '35', '10']
tops = ['43', '2', '48', '87']
sweaters = ['47', '46', '96', '44', '93', '94', '88']
jackets = ['5', '13', '80']
accessories = ['61', '146', '194', '151']

xs = 4.45       #4oz
small = 5.45    #8oz   
medium = 7.45   #16oz   
large = 12.40   #32oz
xlarge = 16.40  #10lb

def scrape():
    url = f"https://webapi.depop.com/api/v1/shop/42803449/products/?limit=200"
    data = requests.get(url).json()
    print("fetching 200 items...")
    #index products dictionary: description, price, 
    #national_shipping_cost, sizes, sold, brandId, categoryId


    itemsList = []
    for item in data['products']:
        newDict = {}
        newDict['desc'] = str(item['description']).split("\n")[0]
        newDict['price'] = str(item['price']['price_amount'])
        newDict['shipping'] = str(item['price']['national_shipping_cost'])

        sizes = item['sizes']
        if sizes:
            newDict['size'] = sizes[0]
        else:
            newDict['size'] = 'x'
        

        if(item['sold']):
            newDict['sold'] = "sold"
        else:
            newDict['sold'] = "available"

        newDict['brandId']  = str(item['brandId'])
        newDict['categoryId']  = str(item['categoryId'])
    
        if len(item['preview']) > 0:
            newDict['img'] = item['preview']['1280']
        else:
            print('File already exists, skipped.')
        

        itemsList.append(newDict)
    return itemsList


def getRandomItem(items, num, categoryIds=None, size=None):
    if num == 0:
        return
    if categoryIds == None:
        item = items[random.randint(0, 199)]
        response = requests.get(item['img'])
        Image.open(BytesIO(response.content)).show()
        print("Item {}: {} {} {} {} {}".format(
        num, item["desc"], item["size"], item["price"], item["shipping"], item["categoryId"]))
        num -= 1
        getRandomItem(items, num, categoryIds)
    elif categoryIds != None and size == None:
        item = items[random.randint(0, 199)]
        while item['categoryId'] not in categoryIds:
            item = items[random.randint(0, 199)]
        response = requests.get(item['img'])
        Image.open(BytesIO(response.content)).show()
        print("Item {}: {} {} {} {} {}".format(
        num, item["desc"], item["size"], item["price"], item["shipping"], item["categoryId"]))
        num -= 1
        getRandomItem(items, num, categoryIds)
    elif availableSize(items, categoryIds, size):
        item = items[random.randint(0, 199)]
        while item['categoryId'] not in categoryIds or item['size'] != size:
            
            item = items[random.randint(0, 199)]
        
        response = requests.get(item['img'])
        Image.open(BytesIO(response.content)).show()
        print("Item: {} {} {} {} {}".format(
        item["desc"], item["size"], item["price"], item["shipping"], item["categoryId"]))
        num -= 1
        getRandomItem(items, num, categoryIds, size)
    else:
        print("Size not available.")
        return 
        
    

def availableSize(item, category, size):
    catInventory = categorize(item, 'size')
    print(size)
    print(category)
    for cat in category:
        if size in catInventory[cat]:
            return True
    return False

    

def categorize(itemsList, param):
    categorizedDict = {}
    for item in itemsList:
        if item['categoryId'] in categorizedDict:
            categorizedDict[item['categoryId']].append(item[param])
        else:
            categorizedDict[item['categoryId']] = [item[param]]
    
    return categorizedDict



def shippingDisparity(itemsList, parcelSize):
    with open("disparity.txt", "w", encoding="utf-8") as file:
        for item in itemsList:
            if float(item['shipping']) > parcelSize:
                file.write(' '.join([item['desc'],item['shipping'],'\n']))



def main():

    '''
    newDict = categorize(itemsList, 'desc')
    for category in newDict:
        print("-----------------------------------------------------")
        print(category + ": " + str(newDict[category]))
    '''
    """
    getRandomItem(itemsList, 1, sweaters)
    getRandomItem(itemsList, 1, tops)
    getRandomItem(itemsList, 1, pants)
    getRandomItem(itemsList, 1, jackets)
    getRandomItem(itemsList, 1, accessories)

    """
    itemsList = scrape()
    shippingDisparity(itemsList, medium)
main()
