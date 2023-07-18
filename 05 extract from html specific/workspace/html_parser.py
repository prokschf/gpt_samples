from html.parser import HTMLParser as BaseHTMLParser

class HTMLParser(BaseHTMLParser):
    def __init__(self):
        super().__init__()
        self.articles = []
        self.current_tag = None
        self.current_article = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'article':
            self.current_tag = tag

    def handle_endtag(self, tag):
        if tag == 'article':
            self.articles.append(self.current_article)
            self.current_article = {}
            self.current_tag = None

    def handle_data(self, data):
        if self.current_tag == 'article':
            if 'headline' not in self.current_article:
                self.current_article['headline'] = data.strip()
            else:
                self.current_article['content'] = data.strip()

    def get_articles(self):
        return self.articles
