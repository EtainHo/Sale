import urllib.request
from bs4 import BeautifulSoup


url = "https://www.grana.com/choose-your-country/"
html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")
countries = soup.find_all('span', {'class': 'pull-left'})

#you need a for loop to access the list
def func():
    for country in countries:
    #convert the html object to string
       countryName = country.text

       if countryName == 'Hong Kong':
           return ('Found it, '+ countryName)

#print (func())
