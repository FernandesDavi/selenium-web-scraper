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

if __name__ == "__main__":
  driver = get_driver()
  videos = get_videos(driver)

  print(f'found {len(videos)} videos')
  print('Parse videos')
  # title, url, thumbnail_url,vies, uploaded
  video = videos[0]
  title = video.find_element(By.ID, 'videos-title').text
  print(title)
