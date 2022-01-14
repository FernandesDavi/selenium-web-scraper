import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL =  'https://www.youtube.com/feed/trending'

def get_videos(driver):
  VIDEOS_DIV_TAG= 'ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  videos_tag = driver.find_elements(By.TAG_NAME,VIDEOS_DIV_TAG)
  return videos_tag


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def parse_video(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  
  thumbnail_url = video.find_element(By.TAG_NAME,'img').get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name').text

  description = video.find_element(By.ID, 'description-text').text
  return{
    'title': title,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'channel': channel_div,
    'description': description
  }
if __name__ == "__main__":
  driver = get_driver()
  videos = get_videos(driver)

  print(f'found {len(videos)} videos')
  print('Parsing top 10 videos')

  videos_data = [parse_video(video) for video in videos[:10]]
 
  print('save the data a csv')
  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('trending.csv', index=None)

