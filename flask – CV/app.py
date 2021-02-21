from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_home():
    return render_template('MainHTML.html', name="MainPage", title="MainPage")


@app.route('/recommend')
def recommend():
    return render_template('Recommendations.html', name="recommend", title="recommend")


@app.route('/Movies')
def movies():
    films = ['Comedy: The Big Lebowski', 'Action: The Matrix', 'Drama: Girl, Interrupted', 'Documentary: The Jinx',
             'Guilty Pleasure: Mean Girls ']
    return render_template('assignment8.html', films=films)


if __name__ == '__main__':
    app.run(debug=True)
