import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

# Some webpages don't like scripts sometimes, so adding a header allows the script to impersonate a web browser. 

c = r.content
#print(str(c))

soup = BeautifulSoup(c, "html.parser")

# print(soup.prettify())   this is the same as looking at the inspect page of a webpage

body = soup.find_all("div", {"class" : "cities"})
#print(body)

city_headers = body[0].find_all("h2")
#print(city_headers[0].text)

# text will only work with individual items - find_all creates a list therefore you must specify the index before applying the text attribute. if you use find you dont need to specify index

for item in body:
    print(item.find_all("h2")[0].text)
# returns the header for each element

for item in body:
    print(item.find_all("p")[0].text)
# returns the paragraph for each element