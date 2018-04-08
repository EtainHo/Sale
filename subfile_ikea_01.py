import urllib.request
from bs4 import BeautifulSoup


url = "https://www.ikea.com/hk/zh/catalog/categories/departments/bedroom/10731/?sorting=price"
html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")
ProductNames = soup.find_all('span', {'class': 'productTitle floatLeft'})
ProductPrices = soup.find_all('span', {'class': 'price regularPrice'})

for ProductName in ProductNames:
    Name = ProductName.text

for ProductPrice in ProductPrices:
    Price = ProductPrice.text

print (Name + Price)
