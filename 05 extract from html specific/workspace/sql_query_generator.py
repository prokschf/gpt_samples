def generate_sql_query(articles):
    query = "INSERT INTO articles (headline, content) VALUES "
    values = []

    for article in articles:
        headline = article['headline'].replace("'", "\\'")
        content = article['content'].replace("'", "\\'")
        values.append(f"('{headline}', '{content}')")

    query += ', '.join(values) + ';'

    return query
