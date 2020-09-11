from urllib.request import urlopen as urequest
from bs4 import BeautifulSoup as soup
from bs4 import Comment
import os


def scrape_both(years):
    # scrape_hitting(years)
    scrape_pitching(years)


def scrape_hitting(years):
    my_url = 'https://www.baseball-reference.com/leagues/MLB/'

    f = open('stat_scraper/generated_stats/team_hitting_statistics.csv', "w")
    hitting_columns = ['Team', '#Bat', 'BatAge', 'R/G', 'G', 'PA', 'AB', 'R', 'R','H', '2B', '3B', 
        'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'OPS+', 'TB', 'GDP', 'HBP', 'SH', 'SF', 'IBB', 'LOB', 'Postseason']
    f.write(",".join(hitting_columns) + '\n')

    for year in years:
        link = my_url + str(year) + '.shtml'
        client = urequest(link)
        page_html = client.read()
        client.close()

        page_soup = soup(page_html, "html.parser")
        standard_batting_html = page_soup.find("div", {'id': 'all_teams_standard_batting'}).find('div', {'id': 'div_teams_standard_batting'})

        postseason_html = page_soup.find("div", {'id': 'all_postseason'})
        new_page_soup = soup(str(postseason_html), 'lxml')
        comments = new_page_soup.findAll(text=lambda text:isinstance(text, Comment))[0]
        commentsoup = soup(comments, 'lxml')
        postseason_table = commentsoup.find('div', {'id': 'div_postseason'}).table.tbody
        postseason_rows = postseason_table.findChildren(['tr'])

        postseason_teams = []
        for row in postseason_rows:
            td_list = row.find_all('td')
            look_at_td = td_list[2]
            teams = look_at_td.findAll('a')
            if not teams[0].text in postseason_teams:
                postseason_teams.append(teams[0].text)
            if not teams[1].text in postseason_teams:
                postseason_teams.append(teams[1].text)

        batting_table = standard_batting_html.table.tbody
        batting_rows = batting_table.findChildren(['tr'])
        batting_rows = batting_rows[:len(batting_rows)-1]

        for row in batting_rows:
            team_name = row.th.a['title']
            cells = row.findChildren('td')
            row_values = [cell.text for cell in cells]
            row_values = [team_name] + row_values
            if team_name in postseason_teams:
                row_values.append('1')
            else:
                row_values.append('0')
            f.write(",".join(row_values) + '\n')

    f.close()


def scrape_pitching(years):
    my_url = 'https://www.baseball-reference.com/leagues/MLB/'

    f = open('stat_scraper/generated_stats/team_pitching_statistics.csv', "w")
    pitching_columns = ['Team','#P','PAge','RA/G','W','L','W-L%','ERA','G','GS','GF','CG','tSho','cSho','SV','IP','H','R','ER','HR','BB',
        'IBB','SO','HBP','BK','WP','BF','ERA+','FIP','WHIP','H9','HR9','BB9','SO9','SO/W','LOB', 'Postseason']
    f.write(",".join(pitching_columns) + '\n')

    for year in years:
        link = my_url + str(year) + '.shtml'
        client = urequest(link)
        page_html = client.read()
        client.close()

        page_soup = soup(page_html, "html.parser")
        standard_pitching_html = page_soup.find("div", {'id': 'all_teams_standard_pitching'})
        new_page_soup = soup(str(standard_pitching_html), 'lxml')
        pitching_comments = new_page_soup.findAll(text=lambda text:isinstance(text, Comment))[0]
        pitching_soup = soup(pitching_comments, 'lxml')

        standard_pitching_html = pitching_soup.find('div', {'id': 'div_teams_standard_pitching'})
        pitching_table = standard_pitching_html.table.tbody
        pitching_rows = pitching_table.findChildren(['tr'])
        pitching_rows = pitching_rows[:len(pitching_rows)-1]

        postseason_html = page_soup.find("div", {'id': 'all_postseason'})
        new_page_soup = soup(str(postseason_html), 'lxml')
        comments = new_page_soup.findAll(text=lambda text:isinstance(text, Comment))[0]
        commentsoup = soup(comments, 'lxml')
        postseason_table = commentsoup.find('div', {'id': 'div_postseason'}).table.tbody
        postseason_rows = postseason_table.findChildren(['tr'])

        postseason_teams = []
        for row in postseason_rows:
            td_list = row.find_all('td')
            look_at_td = td_list[2]
            teams = look_at_td.findAll('a')
            if not teams[0].text in postseason_teams:
                postseason_teams.append(teams[0].text)
            if not teams[1].text in postseason_teams:
                postseason_teams.append(teams[1].text)

        for row in pitching_rows:
            team_name = row.th.a['title']
            cells = row.findChildren('td')
            row_values = [cell.text for cell in cells]
            row_values = [team_name] + row_values
            if team_name in postseason_teams:
                row_values.append('1')
            else:
                row_values.append('0')
            f.write(",".join(row_values) + '\n')

    f.close()