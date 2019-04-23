# Webscrapping causes unnecasary traffic on websites. Somewebsites owner may find it 
# offensive enough to put charges on you.
# So use wisely and at YOUR OWN RISK.

# ONLY FOR EDUCATIONAL PURPOSE

from os import system
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup 
print("Import Successful!")
system("clear")


my_url = 'https://www.newegg.com/desktop-graphics-cards/subcategory/id-48' #test url of newegg.
uClient = urlopen(my_url) #creates connection and gets webpage.
page_html = uClient.read()
uClient.close()


f = open('./scrapped.csv','r+') #opening file to write.
headers = "item_brand, item_title\n"
f.write(headers) #writing headers to file.


page_soup = soup(page_html, "html.parser") #html parsing.
#page_soup.findAll('a',{'class' : "item-title"})
products = page_soup.findAll('div', {'class' : "item-container"})
for i in products:
	item_title = i.find('a',{'class' : "item-title"}).text.strip().replace(',' , '|') #finding item title from the soup.
	item_brand = i.find('div', {'class' : 'item-branding'}).img['title'].strip()
	#product_data[len(product_data.keys())] = {'item-title' : item_title, 'item_brand' : item_brand}
	f.write(item_brand+","+item_title+"\n")
f.close()
	