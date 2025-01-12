import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

try:
    # Check if SSL module is available
    import ssl
except ModuleNotFoundError:
    raise ImportError("The 'ssl' module is required but is not available in your environment. Please ensure it is installed.")

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening a browser window
chrome_options.add_argument("--disable-gpu")  # Disable GPU for compatibility
chrome_options.add_argument("--no-sandbox")  # Required for running in some environments (e.g., Docker)
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent potential resource-related crashes

try:
    # Set up the WebDriver
    service = Service('/path/to/chromedriver')  # Specify the path to the ChromeDriver executable
    print("Initializing WebDriver...")
    driver = webdriver.Chrome(service=service, options=chrome_options)  # Initialize the WebDriver with the specified options

    # Q1: URL to scrape
    url = "https://www.youtube.com/@PW-Foundation/videos"
    print(f"Navigating to URL: {url}")
    driver.get(url)  # Open the specified URL in the browser

    time.sleep(5)  # Allow the page to load fully before interacting with it
    print("Page loaded. Performing initial setup...")

    # Scroll down to ensure content is loaded
    body = driver.find_element(By.TAG_NAME, 'body')  # Locate the body element to simulate scrolling
    print("Scrolling to load more content...")
    for _ in range(3):  # Scroll multiple times to load dynamic content
        body.send_keys(Keys.END)  # Simulate pressing the END key
        time.sleep(2)  # Pause to allow content to load
    print("Scrolling complete.")

    # Locate video elements
    print("Locating video elements...")
    videos = driver.find_elements(By.ID, 'dismissible')[:5]  # Select the first 5 videos on the page
    print(f"Found {len(videos)} videos.")

    # Lists to store data
    video_urls = []  # List to store video URLs
    thumbnail_urls = []  # List to store thumbnail URLs
    titles = []  # List to store video titles
    views = []  # List to store view counts
    post_times = []  # List to store posting times

    # Extract data from each video
    for idx, video in enumerate(videos, start=1):
        print(f"Extracting data for video {idx}...")
        # Q1: Video URL
        url_element = video.find_element(By.XPATH, ".//a[@id='thumbnail']")  # Locate the thumbnail link
        video_url = url_element.get_attribute('href')  # Extract the href attribute (video URL)
        video_urls.append(video_url)  # Add to the list of video URLs
        print(f"Video URL: {video_url}")

        # Q2: Thumbnail URL
        thumbnail_url = url_element.find_element(By.TAG_NAME, 'img').get_attribute('src')  # Extract the src attribute of the thumbnail image
        thumbnail_urls.append(thumbnail_url)  # Add to the list of thumbnail URLs
        print(f"Thumbnail URL: {thumbnail_url}")

        # Q3: Title
        title = video.find_element(By.XPATH, ".//a[@id='video-title']").text  # Extract the text of the video title
        titles.append(title)  # Add to the list of titles
        print(f"Title: {title}")

        # Q4: Views
        view = video.find_element(By.XPATH, ".//span[contains(text(),'views')]").text  # Extract the text showing the number of views
        views.append(view)  # Add to the list of view counts
        print(f"Views: {view}")

        # Q5: Posting time
        post_time = video.find_element(By.XPATH, ".//div[@id='metadata-line']/span[2]").text  # Extract the posting time text
        post_times.append(post_time)  # Add to the list of posting times
        print(f"Posted Time: {post_time}")

    # Save data to CSV
    csv_file = 'youtube_videos.csv'
    print(f"Saving data to CSV file: {csv_file}")
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)  # Create a CSV writer object
        writer.writerow(["Video URL", "Thumbnail URL", "Title", "Views", "Posted Time"])  # Write the header row
        for i in range(len(video_urls)):
            writer.writerow([video_urls[i], thumbnail_urls[i], titles[i], views[i], post_times[i]])  # Write each video's data

    print(f"Data successfully scraped and saved to {csv_file}")

except OSError as e:
    if "Errno 138" in str(e):
        print("Error: OSError [Errno 138] indicates that the current environment does not support certain WebDriver operations. Please ensure your environment allows WebDriver execution.")
    else:
        print(f"Unexpected OSError: {e}")

finally:
    # Close the driver
    print("Closing WebDriver...")
    try:
        driver.quit()  # Terminate the WebDriver session
        print("WebDriver closed. Program finished.")
    except NameError:
        print("WebDriver was not initialized, skipping close operation.")
