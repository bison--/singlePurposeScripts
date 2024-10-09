import requests
from bs4 import BeautifulSoup

url = 'https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html#keywords'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

keywords = []
table = soup.find('table', {'class': 'docutils align-default'})
for row in table.find('tbody').find_all('tr'):
    keyword = row.find('td').get_text(strip=True)
    keywords.append(keyword)

print(keywords)

print('[')
for keyword in keywords:
    print(f"    '{keyword}',")
print(']')
