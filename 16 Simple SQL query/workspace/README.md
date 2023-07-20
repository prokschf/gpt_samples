Since the task is to write an SQL query, there is no need for multiple files, classes, functions, or methods. The SQL query will be a standalone piece of code that can be executed in any SQL environment that has access to the 'employees' and 'projects' tables.

The SQL query will join the 'employees' and 'projects' tables on the 'ID' and 'fk_employee_id' fields, respectively. It will then filter out employees who are not associated with any project or who are associated with multiple projects. The query will also handle duplicate names in the 'employees' table by outputting all of them, and handle duplicate project names in the 'projects' table by outputting the one with the highest 'id'. The results will be ordered alphabetically by employee name.

Here is the SQL query:

query.sql
