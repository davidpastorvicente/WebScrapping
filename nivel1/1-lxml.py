import requests
from lxml import html

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

url = "https://www.wikipedia.org"

resp = requests.get(url, headers=headers)

parser = html.fromstring(resp.text)

langs = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
for lang in langs:
    print(lang)