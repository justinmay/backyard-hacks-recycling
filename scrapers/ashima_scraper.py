import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

r = requests.get('https://www.theahimsacollective.com/collections/all?page=1')

soup = BeautifulSoup(r.text, features="html.parser")

###   Finding the names ### good
product_names = soup.find_all("div", class_="h4 grid-view-item__title product-card__title")
names = []
for product in product_names:
   names.append(product.text)

##   Finding the links ### 
product_link = soup.find_all("div", class_="grid-view-item product-card")
links = []
for product in product_link:
   links.append("https://www.theahimsacollective.com/"+product.find("a")['href'])

###  Finding Prices ### 
product_price = soup.find_all("span", class_="money")
prices = []
for product in product_price:
    prices.append(product.text)

###  Finding image links ### 
product_image_link = soup.find_all("div", class_="grid-view-item product-card")
image_links = []
for product in product_image_link:
   image_links.append("https://www.theahimsacollective.com/"+product.find("a")['href'])

#print(len(names)) good

#print(len(prices)

#print(len(links)) good

#print(len(image_links)) good

### putting it all together ### 
d = {'names': names, 'prices': prices, 'links': links, 'image_links': image_links}
df = pd.DataFrame(data=d)
df.to_csv("timbuktu_data.csv")