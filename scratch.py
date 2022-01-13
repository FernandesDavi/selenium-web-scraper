
import requests
from bs4 import BeautifulSoup
YOUTUBE_TRENDING_URL =  'https://www.youtube.com/feed/trending'

# não executa JS
response = requests.get(YOUTUBE_TRENDING_URL)

print('status code', response.status_code)

doc = BeautifulSoup(response.text,'html.parser')
print(doc.title.Text)

#find all video divs
video_divs = doc.find_all('div', class_='style-scope ytd-video-renderer')
print(f'found {len(video_divs)} videos')