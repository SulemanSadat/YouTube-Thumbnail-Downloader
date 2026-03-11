from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import os
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Replace the URL below with the target YouTube channel URL
channel_url = 'https://www.youtube.com/@username/videos'
driver.get(channel_url)


last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2) 
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


thumbnails = driver.find_elements(By.XPATH, '//a[@id="thumbnail"]')


if not os.path.exists('thumbnails'):
    os.makedirs('thumbnails')


unique_video_ids = set()


for index, thumbnail in enumerate(thumbnails):
    video_url = thumbnail.get_attribute('href')
    if video_url:
       
        video_id = video_url.split('=')[-1]
        if video_id not in unique_video_ids:
            unique_video_ids.add(video_id)
            # max resolution thumbnail URL
            thumbnail_url = f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg'

      
            img_data = requests.get(thumbnail_url).content
            print("Downloaded", img_data)
            with open(f'thumbnails/thumbnail_{index + 1}.jpg', 'wb') as handler:
                handler.write(img_data)

driver.quit()

print("High-quality, non-duplicate thumbnails downloaded successfully.")