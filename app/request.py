import urllib.request,json
from .models import News

#News = news.News
api_key = None
headlines_url = None
source_url = None
everything_url = None

def configure_request(app):
    global api_key,headlines_url,everything_url,source_url
    api_key = app.config['NEWS_API_KEY']
    headlines_url = app.config['NEWS_HEADLINES_URL']
    source_url = app.config['NEWS_SOURCE_URL']
    everything_url = app.config['NEWS_EVERYTHING_URL']



def get_news(sources):
    get_news_url = sources_url.format(sources,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results)
            return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        status = news_item.get('status')
        sources = news_item.get('sources')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        news_object = News(status,sources,name,description,url,category,language,country)
        news_results.append(news_object)

    return news_results
