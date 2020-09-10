from flask import Flask, render_template, url_for, request, redirect
import pandas as pd

app = Flask(__name__)

pitching_data = pd.read_csv('recent_mlb_pitcher_stats.csv', encoding = "ISO-8859-1")
pitching_data.columns = pitching_data.columns.str.replace(' ', '')

hitting_data = pd.read_csv('recent_mlb_hitter_stats.csv', encoding = "ISO-8859-1")
hitting_data.columns = hitting_data.columns.str.replace(' ', '')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Pitching Statistics':
            return render_template('index.html', current_selection='You have selected pitching statistics', options=['Pitching Last 7 Games', 'Pitching Last 15 Games', 'Pitching Last 30 Games'])

        elif request.form['submit_button'] == 'Hitting Statistics':
            return render_template('index.html', current_selection='You have selected hitting statistics',  options=['Hitting Last 7 Games', 'Hitting Last 15 Games', 'Hitting Last 30 Games'])

        elif 'Last 7 Games' in request.form['submit_button']:
            if 'Pitching' in request.form['submit_button']:
                data = pitching_data[pitching_data['Duration'] == ' Last 7 Games']
                data = data.sort_values('ERA')
            elif 'Hitting' in request.form['submit_button']:
                data = hitting_data[hitting_data['Duration'] == ' Last 7 Games']
                data = data.sort_values('AVG', ascending=False)
            else:
                return 'There was an issue determing the type of statistic to filter'

            return render_template('index.html', data=data.to_html())

        elif 'Last 15 Games' in request.form['submit_button']:
            if 'Pitching' in request.form['submit_button']:
                data = pitching_data[pitching_data['Duration'] == ' Last 15 Games']
                data = data.sort_values('ERA')
            elif 'Hitting' in request.form['submit_button']:
                data = hitting_data[hitting_data['Duration'] == ' Last 15 Games']
                data = data.sort_values('AVG', ascending=False)
            else:
                return 'There was an issue determing the type of statistic to filter'

            return render_template('index.html', data=data.to_html())

        elif 'Last 30 Games' in request.form['submit_button']:
            if 'Pitching' in request.form['submit_button']:
                data = pitching_data[pitching_data['Duration'] == ' Last 30 Games']
                data = data.sort_values('ERA')
            elif 'Hitting' in request.form['submit_button']:
                data = hitting_data[hitting_data['Duration'] == ' Last 30 Games']
                data = data.sort_values('AVG', ascending=False)
            else:
                return 'There was an issue determing the type of statistic to filter'

            return render_template('index.html', data=data.to_html())

        else:
            return 'There was an issue selecting the type of statistic'
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)