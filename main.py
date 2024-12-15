import os
import time
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SITES = {
    'main': 'https://devb.io/sunithvs'
    # 'Me': 'https://www.sunithvs.com/about',
    
}


def take_full_screenshot(url, output_path):
    """
    Take a full screenshot of a webpage using Selenium WebDriver.

    :param url: URL of the webpage to screenshot
    :param output_path: Path where screenshot will be saved
    """
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')

    try:
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)

        # Load the page
        driver.get(url)

        # Wait for page to load completely
        time.sleep(3)  # Basic wait
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Get page dimensions
        total_height = driver.execute_script("return document.body.scrollHeight")
        viewport_height = driver.execute_script("return window.innerHeight")

        # Set viewport width and height
        driver.set_window_size(1200, viewport_height)

        # If page is longer than viewport, take full page screenshot
        if total_height > viewport_height:
            driver.set_window_size(1200, int(total_height * 1.05))
            time.sleep(1)  # Wait for page to adjust

        # Take screenshot
        driver.save_screenshot(output_path)
        print(f"Screenshot saved to {output_path}")

    except Exception as e:
        print(f"Error taking screenshot for {url}: {str(e)}")

    finally:
        driver.quit()


def generate_screenshots_and_markdown(sites=SITES, output_dir='images', markdown_file='README.md'):
    """
    Generate screenshots for websites and create a markdown file.

    :param sites: Dictionary of site names and URLs
    :param output_dir: Directory to save screenshots
    :param markdown_file: Name of the output Markdown file
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Prepare markdown content
    markdown_lines = []

    # Take screenshots
    for name, url in sites.items():
        # Create filename for screenshot
        screenshot_filename = f"{name.lower().replace(' ', '_')}_screenshot.png"
        screenshot_path = os.path.join(output_dir, screenshot_filename)

        # Take screenshot
        take_full_screenshot(url, screenshot_path)

        # Add markdown entry using relative path
        markdown_entry = f"[![{name} Screenshot](images/{screenshot_filename})]({url})\n"
        markdown_lines.append(markdown_entry)

    # Write markdown file
    with open(markdown_file, 'w') as f:
        f.writelines(markdown_lines)

    print(f"Markdown file '{markdown_file}' generated successfully!")


if __name__ == '__main__':
    generate_screenshots_and_markdown()
