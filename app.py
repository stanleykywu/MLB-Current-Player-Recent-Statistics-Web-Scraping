from flask import Flask, render_template, url_for, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Pitching Statistics':
            data = pd.read_csv('stat_scraper/generated_stats/recent_mlb_pitching_stats.csv')
            return render_template('index.html', data=data.to_html())
        elif request.form['submit_button'] == 'Hitting Statistics':
            data = pd.read_csv('stat_scraper/generated_stats/recent_mlb_hitting_stats.csv')
            return render_template('index.html', data=data.to_html())
        else:
            return 'There was an issue selecting the type of statistic'
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)