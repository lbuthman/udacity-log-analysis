# Log Analysis Tool for News Database

## Quickstart

1. Start the application from the command line `python3 log_analysis.py`
2. The application will print a menu. Enter the number of the question you
would like to answer and press Enter.
3. The result output will display once the query completes! Easy :)
4. Press 0 and Enter to quit at any time.


## Purpose of Application

The Log Analysis project aims to simplify the process to answer the following
questions from a news database.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Advanced Usage

Note: This log analysis tools relies on a few Views. You can recreate, retool,
or refactor these views easily. Find the views created below.

1. `CREATE VIEW author_article AS SELECT name, slug FROM authors, articles 
WHERE authors.id = articles.author;`

2. `CREATE VIEW view_errors AS SELECT date_trunc('day', log.time) AS day, COUNT(*) 
FROM log WHERE status = '404 NOT FOUND' GROUP BY day;`

3. `CREATE VIEW view_total AS SELECT date_trunc('day', log.time) AS day, COUNT(*) 
FROM log GROUP BY day;`

4. `CREATE VIEW error_percentage AS SELECT view_total.day, 
(view_errors.count::decimal / view_total.count) * 100 AS percentage 
FROM view_total, view_errors WHERE view_total.day = view_errors.day;`
