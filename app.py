from flask import Flask, render_template, url_for, request, redirect
import pandas as pd

app = Flask(__name__)

pitching_data = pd.read_csv('stat_scraper/generated_stats/recent_mlb_pitcher_stats.csv', encoding = "ISO-8859-1", error_bad_lines=False)
pitching_data.columns = pitching_data.columns.str.replace(' ', '')

hitting_data = pd.read_csv('stat_scraper/generated_stats/recent_mlb_hitter_stats.csv', encoding = "ISO-8859-1", error_bad_lines=False)
hitting_data.columns = hitting_data.columns.str.replace(' ', '')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Pitching Statistics':
            return redirect('/pitching-statistics')

        elif request.form['submit_button'] == 'Hitting Statistics':
            return redirect('/hitting-statistics')

        else:
            return 'There was an issue selecting the type of statistic'
    return render_template('index.html')

@app.route('/hitting-statistics', methods=['POST', 'GET'])
def hitting_statistics():
    options = ['Last 7 Games', 'Last 15 Games', 'Last 30 Games']
    positions = ['C', '1B', '2B', 'SS', '3B', 'RF', 'CF', 'LF']
    stats = ['AB', 'R', 'H', 'HR', 'RBI', 'BB', 'SO', 'SB', 'AVG', 'OBP', 'SLG']
    return render_template('hitting.html', options=options, positions=positions, stats=stats)

@app.route('/pitching-statistics', methods=['POST', 'GET'])
def pitching_statistics():
    options = ['Last 7 Games', 'Last 15 Games', 'Last 30 Games']
    stats = ['W', 'L', 'ERA', 'G', 'GS', 'SV', 'IP', 'H', 'ER', 'BB', 'SO', 'WHIP']
    return render_template('pitching.html', options=options, stats=stats)

if __name__ == "__main__":
    app.run(debug=True)