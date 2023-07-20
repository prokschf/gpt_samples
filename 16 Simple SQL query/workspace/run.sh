python3 -m venv env
source env/bin/activate
pip install pysqlite3

sqlite3 database.db < query.sql
