from urllib.request import urlopen as urequest
from bs4 import BeautifulSoup as soup

my_url = 'https://www.mlb.com'

client = urequest(my_url + '/players')
page_html = client.read()
client.close()

page_soup = soup(page_html, "html.parser")
player_list = page_soup.findAll("li", {"class": "p-related-links__item"})

def scrape(player_type, stats, filename):
    f = open(filename, "w")
    f.write(", ".join(['name'] + stats) + '\n')

    for player in player_list:
        player_url = my_url + player.a['href']

        client = urequest(player_url)
        page_html = client.read()
        client.close()

        page_soup = soup(page_html, "html.parser")
        player_recent_html = page_soup.findAll("div", {'class': 'player-splits--last player-splits--last-x'})
        
        if player_recent_html:
            position_html = page_soup.find("div", {'class': 'player-header--vitals'})

            if not position_html.ul.li.text == player_type:
                continue

            name = page_soup.find("img", {'class': 'player-headshot'})['alt']
            table = player_recent_html[0].div.div.div.div.table.tbody
            rows = table.findChildren(['th', 'tr'])
            for row in rows:
                cells = row.findChildren('td')
                row_values = [cell.span.text for cell in cells]
                row_values = [name] + row_values
                f.write(", ".join(row_values) + '\n') 

    f.close()