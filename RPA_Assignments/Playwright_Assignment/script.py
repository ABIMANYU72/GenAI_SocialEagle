from playwright.sync_api import sync_playwright
from datetime import datetime
import time

OUTPUT_FILE = "website_data.txt"

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)

    # Open new page
    page = browser.new_page()

    # Website URL
    url = "https://www.socialeagle.in/"

    # Open website
    page.goto(url, timeout=60000)

    # Wait a few seconds manually
    time.sleep(5)

    # Extract metadata
    title = page.title()

    description = page.locator(
        "meta[name='description']"
    ).get_attribute("content")

    if not description:
        description = "No meta description found"

    # Extract page text
    body_text = page.locator("body").inner_text()

    # Prepare content
    data = f"""
Website URL : {url}
Scraped Time: {datetime.now()}

TITLE:
{title}

DESCRIPTION:
{description}

PAGE CONTENT:
{body_text}
"""

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(data)

    print(f"Data saved successfully to '{OUTPUT_FILE}'")

    # Close browser
    browser.close()