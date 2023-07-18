from html_extractor import HTMLExtractor
from sql_query_builder import SQLQueryBuilder

def main():
    extractor = HTMLExtractor('test.html')
    text = extractor.extract_text()

    builder = SQLQueryBuilder('articles')
    query = builder.insert('Your Headline', text)

    print(query)

if __name__ == "__main__":
    main()
