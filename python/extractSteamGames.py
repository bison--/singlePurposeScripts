# you need a steam account to extract the games from the account
# URL: https://steamcommunity.com/id/ACCOUNT_NAME/games/?tab=all
# use the inspect element tool to get the HTML code of the page
# paste in temp/steam_games.html

# JavaScript code to scroll the page to the bottom, paste it in the console for the page to load all date
"""
let scrollInterval = setInterval(() => {
    window.scrollBy(0, 1000); // Scrolls down by 1000px
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        clearInterval(scrollInterval); // Stops the scroll once you reach the bottom
    }
}, 50);
"""


import os
import csv
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

# Load the HTML content
html_file_path = 'temp/steam_games.html'
if not os.path.exists(html_file_path):
    print(f"File not found: {html_file_path}")
    exit(1)

with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract game titles and playtime
games = []
unplayed_count = 0
# you probably have to modify/adjust these classes to your needs/they seem autogenerated
for game_div in soup.find_all('div', class_='_2-pQFn1G7dZ7667rrakcU3'):
    title_tag = game_div.find('a', class_='_22awlPiAoaZjQMqxJhp-KP')
    playtime_tag = game_div.find('span', class_='_26nl3MClDebGDV7duYjZVn')

    if title_tag:
        title = title_tag.text.strip()
        playtime = playtime_tag.text.strip().replace('TOTAL PLAYED', '').strip() if playtime_tag else '0 hrs'
        if playtime == '0 hrs':
            unplayed_count += 1
        games.append((title, playtime))

# Create a table using rich
table = Table(title="Steam Games and Playtime")

table.add_column("Game Title", justify="left", no_wrap=True)
table.add_column("Total Playtime", justify="left", no_wrap=True)

for game in games:
    table.add_row(game[0], game[1])

# Print the table
console = Console()
console.print(table)

# Print the summary
total_games = len(games)
console.print(f"\nTotal games: {total_games}")
console.print(f"Unplayed games: {unplayed_count}")

# Save the data to a CSV file
output_csv_path = 'output/steam_games.csv'
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Game Title', 'Total Playtime'])
    csvwriter.writerows(games)

print(f"Data saved to {output_csv_path}")