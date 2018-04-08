import urllib.request
from bs4 import BeautifulSoup


url = "https://www.ikea.com/hk/zh/catalog/categories/departments/bedroom/10731/?sorting=price"
html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")
products = soup.find_all('div', {'class': 'productDetails'})

for product in products:
    productName = soup.find('span', {'class': 'productTitle floatLeft'})
    productPrice = soup.find('span', {'class': 'price regularPrice'}
       print (productName + productPrice)
