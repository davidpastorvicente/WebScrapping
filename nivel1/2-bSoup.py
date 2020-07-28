import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

url = "https://www.stackoverflow.com/questions"

resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, features='lxml')

quests = soup.find_all('div', class_="question-summary")
for quest in quests:
    print(quest.find('h3').text, "\n")
    print(quest.find(class_='excerpt').text.strip())
    print("\n")