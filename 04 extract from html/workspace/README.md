The core classes, functions, and methods that will be necessary are:

1. `HTMLExtractor`: A class that will handle the extraction of text from the HTML file. It will have the following methods:
   - `__init__(self, file_path)`: Initializes the HTMLExtractor with the path to the HTML file.
   - `extract_text(self)`: Extracts the text from the "h", "div", and "p" tags in the HTML file.

2. `SQLQueryBuilder`: A class that will handle the creation of the SQL query. It will have the following methods:
   - `__init__(self, table_name)`: Initializes the SQLQueryBuilder with the name of the table to insert into.
   - `insert(self, headline, content)`: Creates an SQL query to insert the given headline and content into the table.

3. `main`: A function that will serve as the entry point for the program. It will create an instance of `HTMLExtractor`, extract the text from the HTML file, create an instance of `SQLQueryBuilder`, and create the SQL query.

Now, let's write the code for each of these components.

requirements.txt
