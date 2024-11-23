
from bs4 import BeautifulSoup
import requests
from datetime import date
import csv

# This is the old code I know works
# url = "https://kakaku.com/item/K0000347675/used/?page=1#tab"
# html = requests.get(url)

# soup = BeautifulSoup(html.content, "html.parser")

# rank = soup.find(id = "mainLeft")
# camera_rank = rank.find_all("td", class_="UshopRank")
# camera_price = rank.find_all("p", class_="fontPrice")

# today = date.today()
# print("Prices and ranks for Canon 5D Markii as of", today)

# for rank, price in zip(camera_rank, camera_price):
#     print(rank.text + " - " + price.text)

# This is the new code to test
today = date.today()
print("Prices and ranks for Canon 5D Markii as of", today)
for x in range(0,6):
    x +=1
    url = "https://kakaku.com/item/K0000903380/used/?page="+ str(x)
    # print(url)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    rank = soup.find(id = "mainLeft")
    camera_rank = rank.find_all("td", class_="UshopRank")
    camera_price = rank.find_all("p", class_="fontPrice")
    for rank, price in zip(camera_rank, camera_price):
            print(rank.text + " - " + price.text)
