Daraz Product Scraper & EDA Dashboard

A Python project that scrapes product data from Daraz.pk, cleans and analyzes it using pandas, and visualizes insights with matplotlib, seaborn, and optional Streamlit.

Project Goals

Extract real-world product data from Daraz using Selenium
Store information like name, price, units sold, rating, and province
Perform EDA: find top brands, most sold products, pricing patterns
Visualize trends with charts (histograms, bar plots, scatter plots)
Build a dashboard or dataset suitable for portfolio or business use
Data Collected

    5 product categories: mobiles, earphones, chargers, power banks, charging cables

    Scraped data from multiple pages per category

    Fields extracted:

        Category

        ProductName

        Price

        Units Sold

        Brand

        Province

        Rating (calculated using star icons)

        Revenue (Price × Units Sold)

Technologies Used:

Tool	        Purpose
Python	        Core logic
Selenium	    Web scraping from Daraz UI
BeautifulSoup	HTML parsing
Pandas	        Data manipulation / cleaning
Matplotlib	    Visualizations
Seaborn	        Statistical plots
Streamlit 	    Interactive dashboard

Sample Visualizations

    Price distribution histogram

    Units sold vs. price (scatter plot)

    Top 10 most sold products

    Top brands by total revenue

    Units sold by province

Folder Structure:

Project/
│
├── scraper.py           # Web scraper using Selenium
├── products.csv         # Raw scraped data
├── eda.py               # Data cleaning & analysis
├── dashboard.py         # (Optional) Streamlit dashboard
├── README.md            # You're reading this

How to Run:
1. Install dependencies

pip install selenium pandas beautifulsoup4 matplotlib seaborn streamlit webdriver-manager

2. Run scraper

python scraper.py

This will generate products.csv.

3. Clean and analyze data

python eda.py

4. Launch dashboard (optional)

streamlit run dashboard.py

Sample Output

Category,ProductName,Price,Units Sold,Brand,Province,Rating,Revenue
mobiles,Infinix Smart 7,24999,624,Infinix,Punjab,4.0,15599376
earphones,Airpods Pro Wireless,698,7300,Airpods,Punjab,4.5,5095400

Future Improvements

    Add sentiment analysis from product reviews

    Track price changes over time

    Expand to other e-commerce sites (e.g. Amazon, OLX)

License:
This project is for educational and portfolio use.
All data is publicly available via Daraz frontend and used under fair use.

