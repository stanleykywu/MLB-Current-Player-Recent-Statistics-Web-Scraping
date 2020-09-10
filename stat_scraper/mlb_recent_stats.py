from stat_scraper.scraper import scrape

def pitcher_data():
    stats = ['name', 'Position', 'Duration','W', 'L', 'ERA', 'G', 'GS', 'SV', 'IP', 'H', 'ER', 'BB', 'SO', 'WHIP']
    filename = 'recent_mlb_pitcher_stats.csv'
    scrape('P', stats, filename)
def hitter_data():
    stats = ['name', 'Position', 'Duration', 'AB', 'R', 'H', 'HR', 'RBI', 'BB', 'SO', 'SB', 'AVG', 'OBP', 'SLG']
    filename = 'recent_mlb_hitter_stats.csv'
    scrape('H', stats, filename)
