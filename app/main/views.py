from flask import render_template, redirect, url_for,request
from ..request import get_news
from . import main

import json

#views
@main.route('/')
def index():
    # Getting news sources
    news_sources = get_news('sources')
    title = 'Home - Welcome to the Greatest News Articles and Everything News Related Website Online'
    return render_template('index.html', title = title,sources = news_sources)

@main.route('/news/<news_everything>')
def news(news_everything):
    return render_template('news.html', everything = news_everything)
