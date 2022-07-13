import requests
from bs4 import BeautifulSoup


content = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/').text

soup = BeautifulSoup(content, 'html.parser')

movies = soup.find_all('h3', class_='title')

titles = [movie.text for movie in movies]
titles = titles[::-1]
with open('top_100_movies_of_all_time.txt','w+', encoding='utf-8') as f:
    for title in titles:
        f.write(title)
        f.write('\n')