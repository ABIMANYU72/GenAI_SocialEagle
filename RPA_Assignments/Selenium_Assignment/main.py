from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os

# Create folders
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

if not os.path.exists("data"):
    os.makedirs("data")

# Setup Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open website
driver.get("https://quotes.toscrape.com/")

# Maximize browser
driver.maximize_window()

# Wait for page load
time.sleep(2)

# Find all quote blocks
quotes = driver.find_elements(By.CLASS_NAME, "quote")

# Store data
all_quotes = []

# Loop through quotes
for quote in quotes:
    
    # Extract quote text
    text = quote.find_element(By.CLASS_NAME, "text").text
    
    # Extract author
    author = quote.find_element(By.CLASS_NAME, "author").text
    
    # Save into dictionary
    all_quotes.append({
        "Quote": text,
        "Author": author
    })

# Convert to DataFrame
df = pd.DataFrame(all_quotes)

# Save CSV
csv_path = "data/quotes.csv"
df.to_csv(csv_path, index=False)

# Take screenshot
screenshot_path = "screenshots/quotes_page.png"
driver.save_screenshot(screenshot_path)

print("Data saved successfully!")
print(f"CSV File: {csv_path}")
print(f"Screenshot: {screenshot_path}")

# Close browser
driver.quit()