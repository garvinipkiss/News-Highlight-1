from flask import render_template
from app import app
from app import views
from ..request import get_news
#views
@app.route('/')
def index():
    # Getting news sources
    news_sources = get_news('sources')
    title = 'Home - Welcome to the Greatest News Articles and Everything News Related Website Online'
    return render_template('index.html', title = title,sources = news_sources)

@app.route('/news/<news_everything>')
def news(news_everything):
    return render_template('news.html', everything = news_everything)
