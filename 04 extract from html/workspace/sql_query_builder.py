class SQLQueryBuilder:
    def __init__(self, table_name):
        self.table_name = table_name

    def insert(self, headline, content):
        query = f"INSERT INTO {self.table_name} (headline, content) VALUES ('{headline}', '{content}');"
        return query
