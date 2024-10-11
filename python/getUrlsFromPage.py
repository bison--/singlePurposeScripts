from rich.console import Console
from rich.table import Table
import requests
from bs4 import BeautifulSoup

PAGE_URL = input('Enter the URL (default: "https://spielmannspiel.com"): ').strip()
if not PAGE_URL:
    PAGE_URL = 'https://spielmannspiel.com'


def get_colored_bool_external(is_external):
    if is_external:
        return '[red]True[/red]'
    else:
        return '[green]False[/green]'


def get_url_from_href(href):
    new_url = ''
    if ' ' in href:
        href = href.replace(' ', '%20')

    if href.startswith('http'):
        new_url = href
    elif href.startswith('/'):
        new_url = PAGE_URL + href
    else:
        new_url = PAGE_URL + '/' + href

    return new_url


found_links = set()

page = requests.get(PAGE_URL)
soup = BeautifulSoup(page.content, 'html.parser')
for anchor in soup.find_all('a', href=True):
    url = get_url_from_href(anchor['href'])
    if url:
        found_links.add(url)


table = Table(title=str(len(found_links)) + " Links on " + PAGE_URL)

table.add_column("URL", justify="left", no_wrap=True)
table.add_column("External", justify="left", no_wrap=True)

for link in found_links:
    table.add_row(
        link,
        get_colored_bool_external(not link.startswith(PAGE_URL))
    )

console = Console()
console.print(table)
