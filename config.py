class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/'
    NEWS_SOURCE_URL='https://newsapi.org/v2/sources?category={}&country={}&language={}&apiKey={}'

    NEWS_HEADLINES_URL='https://newsapi.org/v2/top-headlines?category={}&q={}&country={}&apiKey={}'
    NEWS_EVERYTHING_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
config_options  = {
'development':DevConfig,
'production':ProdConfig
}
