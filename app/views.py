from flask import render_template
from app import app

#views
@app.route('/')
def index():
    message = 'News Highlight'
    return render_template('index.html', message = message)

@app.route('/news/<news_everything>')
def news(news_everything):
    return render_template('news.html', everything = news_everything)
