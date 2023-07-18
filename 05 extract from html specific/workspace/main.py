from html_parser import HTMLParser
from sql_query_generator import generate_sql_query

def main():
    # Read the HTML file
    with open('test.html', 'r') as file:
        data = file.read()

    # Parse the HTML file and extract the articles
    parser = HTMLParser()
    parser.feed(data)
    articles = parser.get_articles()

    # Generate the SQL query
    query = generate_sql_query(articles)

    # Print the SQL query
    print(query)

if __name__ == "__main__":
    main()
