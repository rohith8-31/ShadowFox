import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://quotes.toscrape.com/"

# Send request and get HTML content
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch page, status code: {response.status_code}")
    exit()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quotes and authors
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

# Open CSV file to save data
with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])  # Header row

    # Loop through all quotes and authors
    for i in range(len(quotes)):
        quote_text = quotes[i].text.strip()
        author_name = authors[i].text.strip()
        
        # Print in terminal (optional)
        print(f"Quote: {quote_text}")
        print(f"Author: {author_name}")
        print("-" * 50)
        
        # Write to CSV
        writer.writerow([quote_text, author_name])

print("✅ Scraping complete! Data saved to 'quotes.csv'")
