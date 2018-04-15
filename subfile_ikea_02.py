#import urllib.request
import urllib2
import re
from bs4 import BeautifulSoup

regex = re.compile(r'[\n\r\t]')

url = "https://www.ikea.com/hk/zh/catalog/categories/departments/bedroom/10731/?sorting=price"
#html = urllib.request.urlopen(url)
req = urllib2.Request(url)
page = urllib2.urlopen(req)
html = page.read()

soup = BeautifulSoup(html, "html.parser")
#products = soup.find_all('div', {'class': 'productDetails'})
nameTags = soup.find_all('span', {'class': 'productTitle floatLeft'})
priceTags = soup.find_all('span', {'class': 'price regularPrice'})

priceList = []
productList = []

for tag in priceTags:
	tag.find('span', {'class': 'comparisonContainer'}).decompose()
	price = tag.text
	price = str(regex.sub("", price)).encode('utf-8')
	priceList.append(price)

for count, tag in enumerate(nameTags):
	productInfo = []
	name = tag.string.encode('utf-8')
	productInfo.append(name)
	price = priceList[count]
	productInfo.append(price)
	productList.append(productInfo)

print productList


#for product in products:
#    productName = soup.find('span', {'class': 'productTitle floatLeft'})
#    productPrice = soup.find('span', {'class': 'price regularPrice'})
#    print (productName.text + productPrice.text)
