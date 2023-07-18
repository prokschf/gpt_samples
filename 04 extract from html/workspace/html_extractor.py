from bs4 import BeautifulSoup

class HTMLExtractor:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.soup = BeautifulSoup(file.read(), 'html.parser')

    def extract_text(self):
        text = ''
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'p']:
            elements = self.soup.find_all(tag)
            for element in elements:
                text += ' ' + element.get_text()
        return text.strip()
