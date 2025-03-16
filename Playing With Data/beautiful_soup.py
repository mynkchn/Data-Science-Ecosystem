import requests
from bs4 import BeautifulSoup

# ----------------- Basic Web Scraping -----------------
URL = 'https://example.com/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting Titles
print("Page Title:", soup.title.text)

# Extracting all links
for link in soup.find_all('a'):
    print("Link:", link.get('href'))

# Extracting text from paragraphs
for para in soup.find_all('p'):
    print("Paragraph:", para.text)

# ----------------- Advanced Features -----------------

# 1️⃣ Extracting Data from Specific Tags with Conditions
for div in soup.find_all('div', class_='content-box'):
    print("Div Content:", div.text.strip())

# 2️⃣ CSS Selectors (Powerful for complex websites)
for item in soup.select('div.article h2'):  # Finds all <h2> inside <div class='article'>
    print("Article Heading:", item.text)

# 3️⃣ Navigating the DOM Tree
first_div = soup.find('div')
print("First div content:", first_div.text.strip())
print("Parent of div:", first_div.parent)
print("Next Sibling:", first_div.next_sibling)
print("Previous Sibling:", first_div.previous_sibling)

# 4️⃣ Extracting Table Data
for table in soup.find_all('table'):
    for row in table.find_all('tr'):
        cells = row.find_all(['td', 'th'])
        print([cell.text.strip() for cell in cells])

# 5️⃣ Extracting Images
for img in soup.find_all('img'):
    print("Image Source:", img['src'])

# 6️⃣ Handling Dynamic Content (Requires Selenium for JavaScript-rendered data)
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get(URL)
# page_source = driver.page_source
# soup = BeautifulSoup(page_source, 'html.parser')

# 7️⃣ Extracting Metadata
for meta in soup.find_all('meta'):
    print("Meta Tag:", meta)

# 8️⃣ Cleaning HTML Tags Using .get_text()
cleaned_text = soup.get_text(separator=' ', strip=True)
print("Cleaned Text:", cleaned_text)

# 9️⃣ Extracting Attributes
for tag in soup.find_all('a'):
    print("Link Text:", tag.text, "| Href:", tag.get('href'))

# 🔟 Saving Extracted Data to CSV
import pandas as pd

df = pd.DataFrame({
    'Link Text': [tag.text for tag in soup.find_all('a')],
    'Href': [tag.get('href') for tag in soup.find_all('a')]
})

df.to_csv('scraped_data.csv', index=False)
print("Data saved successfully to 'scraped_data.csv'")
