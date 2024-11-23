def scrape():
    today = date.today()
    file = open("camera_scrape.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["Date", "Condition Rank", "Price"])
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
        writer.writerow([today, rank.text, price.text])
    file.close()

sched.every().day.at("10:30").do(scrape)
