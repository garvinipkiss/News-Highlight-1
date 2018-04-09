import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News()
