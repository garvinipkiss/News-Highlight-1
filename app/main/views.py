from flask import render_template
from app import app

#views
@app.route('/')
def index():
    title = 'Home - Welcome to the Greatest News Articles and Everything News Related Website Online'
    return render_template('index.html', title = title)

@app.route('/news/<news_everything>')
def news(news_everything):
    return render_template('news.html', everything = news_everything)
