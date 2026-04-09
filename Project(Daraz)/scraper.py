import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

fileName = "products.csv"
categories = ["mobiles", "earphones", "chargers", "powerbank", "charging cable"]

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

def safe_text(element, default=""):
    return element.text.strip() if element else default

with open(fileName, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Category", "ProductName", "Price", "Units Sold", "Brand", "Province", "Rating"])

    for cat in categories:
        for page in range(1, 6):
            url = f"https://www.daraz.pk/catalog/?q={cat}&page={page}"
            driver.get(url)

            # random delay (important)
            time.sleep(random.uniform(2, 4))

            soup = BeautifulSoup(driver.page_source, "html.parser")
            productBoxes = soup.find_all("div", class_="buTCk")

            print(f"[{cat}] Page {page} → {len(productBoxes)} products")

            for box in productBoxes:
                try:
                    # Product Name
                    a_tag = box.find("a", title=True)
                    productName = a_tag["title"].strip() if a_tag else "No Title"

                    # Price
                    price = safe_text(box.find("span", class_="ooOxS"), "No Price")

                    # Units Sold
                    unitsSold = safe_text(box.find("span", class_="_1cEkb"), "0 sold")

                    # Province
                    province_tag = box.find("span", class_="oa6ri")
                    province = province_tag["title"].strip() if province_tag and province_tag.has_attr("title") else "Unknown"

                    # Brand (basic extraction)
                    brand = productName.split()[0] if productName != "No Title" else "Unknown"

                    # Rating calculation
                    fullStars = len(box.find_all("i", class_="_9-ogB Dy1nx"))
                    halfStars = len(box.find_all("i", class_="_9-ogB B4Foa"))
                    rating = fullStars + 0.5 * halfStars

                    writer.writerow([cat, productName, price, unitsSold, brand, province, rating])

                except Exception as e:
                    print("Error parsing product:", e)

driver.quit()
print("Scraping completed. Data saved to products.csv")