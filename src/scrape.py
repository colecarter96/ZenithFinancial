
import requests 
from bs4 import BeautifulSoup 
  
# Making a GET request 
r = requests.get('https://www.capitoltrades.com/trades') 
  
# print request object 
print(r.url) 
    
# print status code 
print(r.status_code)

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

s = soup.find('main', class_="site-main")
s1 = s.find('div', class_='container')
line = s1.find('tr', class_="q-tr")
line = line.find_all_next('tr', class_='q-tr')
# next = line.find_next('tr', class_='q-tr')

# type = s1.find('')
# line = s1.find('span', class_='q-field issuer-ticker')
# buy = line.find('th', class_='q-th q-column--issuer')
lol = s1.find_next
# next = buy.find('div', class_='q-cell cell--traded-issuer has-avatar')
print(line)
print(" ")
# print(next)

line = s.find('tr', class_="q-tr")
# print(line)
# while line != 'None':

# can you find_next() to loop through the trades, kind of lmao, cuz some of them are named super poorly



# s = soup.find('main', class_="site-main")
# tickers = s.find_all('span', class_="q-field issuer-ticker")
# types = s.find_all('span', class_="q-field tx-type tx-type--buy has-asterisk")


# for ticker in tickers: 
#     print(ticker.text)

# for type in types: 
#     print(type.text)

