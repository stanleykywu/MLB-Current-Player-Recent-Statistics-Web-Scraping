from urllib.request import urlopen as urequest
from bs4 import BeautifulSoup as soup
import os

def scrape(player_type, stats, filename):
    my_url = 'https://www.mlb.com'

    client = urequest(my_url + '/players')
    page_html = client.read()
    client.close()

    page_soup = soup(page_html, "html.parser")
    player_list = page_soup.findAll("li", {"class": "p-related-links__item"})

    f = open(filename, "w")
    f.write(", ".join(['name'] + stats) + '\n')

    for player in player_list:
        player_url = my_url + player.a['href']
        try:
            client = urequest(player_url)
            page_html = client.read()
            client.close()
        except:
            continue

        page_soup = soup(page_html, "html.parser")
        player_recent_html = page_soup.findAll("div", {'class': 'player-splits--last player-splits--last-x'})
        
        if player_recent_html:
            position_html = page_soup.find("div", {'class': 'player-header--vitals'})

            if player_type == 'P' and not position_html.ul.li.text == player_type:
                continue
            elif player_type == 'H' and position_html.ul.li.text == 'P':
                continue

            name = page_soup.find("span", {'class': 'player-header--vitals-name'}).text
            table = player_recent_html[0].div.div.div.div.table.tbody
            rows = table.findChildren(['th', 'tr'])
            for row in rows:
                cells = row.findChildren('td')
                row_values = [cell.span.text for cell in cells]
                row_values = [name] + row_values
                f.write(", ".join(row_values) + '\n') 

    f.close()