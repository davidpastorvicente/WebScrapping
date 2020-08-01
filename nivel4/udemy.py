import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.149 Safari/537.36",
    "referer": "https://www.udemy.com/courses/search/?q=",
    "accept-language": "es-ES,es;q=0.9"
}

print('Introducir búsqueda: ')
txt = input().replace(' ', '%20')

for i in range(3):
    resp = requests.get("https://www.udemy.com/api-2.0/search-courses/?q=" + txt + "&skip_price=true&p=" + str(i),
                        headers=headers)

    data = resp.json()

    courses = data['courses']

    for course in courses:
        print()
        print("Título:", course['title'])
        print("Rating:", course['rating'])
