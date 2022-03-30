

from bs4 import BeautifulSoup
import requests
# from csv import writer


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}


# ações JNJ Johnson & Johnson (JNJ)
url= "https://finance.yahoo.com/quote/JNJ/financials?p=JNJ"
page = requests.get(url, headers=header)
print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
list = soup.find_all('div', {'class': 'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)'})[0]
print(list)
print(list.text)








# ações Berkshire Hathaway Inc. (BRK-B)
url= ""
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
list = soup.find_all('div', {'class': 'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)'})
print(list)
list



# ações 3M Company (MMM)
url= "https://finance.yahoo.com/quote/MMM/financials?p=MMM"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
list = soup.find_all('div', {'class': 'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)'})
print(list)
list





