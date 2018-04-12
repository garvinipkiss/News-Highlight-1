class News:
    def __init__(self,name,description,url,category,language,country):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
class Articles:
    def __init__(self,name=None,author=None,title=None,description=None,url=None,urlToImage=None,publishedAt=None):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt =publishedAt
