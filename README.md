# MLB Statistics App
An app designed to help fantasy baseball player and general baseball fanatics satisfy their inner data scientist! Complete with some machine learning models to explore.

## Installation
- clone this repository: `git clone https://github.com/stanleykywu/MLB-Current-Player-Recent-Statistics-Web-Scraping.git`
- install bs4: `pip install bs4`
- install flask: `pip install flask`

# MLB Team Data
## Generate CSV Spreadsheets
- open python environment: `python`
- import scripts: `from stat_scraper.team_scraper import scrape_hitting, scrape_pitching`
- run scripts: `scrape_hitting(list: years of data to scrape)` or `scrape_pitching(list: years of data to scrape)`

## Example Output
### Team Hitting Data
![Alt text](resources/team_hitting_example.PNG?raw=true)

### Team Pitching Data
![Alt text](resources/team_pitching_example.PNG?raw=true)

# MLB Recent Hitting Statistics Generation
## Generate CSV Spreadsheets
- open python environment: `python`
- import scripts: `from stat_scraper.mlb_recent_stats import pitcher_data, hitter_data`
- run scripts: `pitcher_data()` or `hitter_data()`

## Example Output
### Recent Player Hitting Data
![Alt text](resources/hitter_example.PNG?raw=true)

### Recent Player Pitching Data
![Alt text](resources/pitcher_example.PNG?raw=true)
