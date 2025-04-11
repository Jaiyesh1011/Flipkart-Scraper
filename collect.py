from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'price': [], 'link': []}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")
        t = soup.find("div", class_="KzDlHZ")
        p = soup.find("div", class_="Nx9bqj _4b5DiR")
        title = t.get_text()
        price = p.get_text()
        l = soup.find("a")
        link = "https://flipkart.com"+l.get("href")
        
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
        
        
    except Exception as e:
        print(e)
    

df = pd.DataFrame(data=d)
df.to_csv("data.csv")