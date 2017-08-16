CREATE VIEW author_article AS SELECT name, slug FROM authors, articles
WHERE authors.id = articles.author;

CREATE VIEW view_errors AS SELECT log.time::date AS day, COUNT(*)
FROM log WHERE status = '404 NOT FOUND' GROUP BY day;

CREATE VIEW view_total AS SELECT log.time::date AS day, COUNT(*)
FROM log GROUP BY day;

CREATE VIEW error_percentage AS SELECT view_total.day,
(view_errors.count::decimal / view_total.count) * 100 AS percentage
FROM view_total, view_errors WHERE view_total.day = view_errors.day;
