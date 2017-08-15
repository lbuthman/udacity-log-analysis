import psycopg2

DBNAME = 'news'


def get_top_three_articles():
    """"Return the three most popular articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("""SELECT title, COUNT(*) AS total FROM log
        JOIN articles ON log.path ILIKE '%' || articles.slug
        WHERE status != '404 NOT FOUND' AND path != '/'
        GROUP BY title ORDER BY total DESC LIMIT 3;""")
    articles = cursor.fetchall()
    db.close()
    return articles


def get_top_authors():
    """"Return the most popular authors of all time."""
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("""SELECT name, COUNT(*) as total FROM log
        JOIN author_article ON log.path ILIKE '%' || author_article.slug
        GROUP BY name ORDER BY total DESC;""")
    authors = cursor.fetchall()
    db.close()
    return authors


def get_top_error_days():
    """Returns days >= 1 Percent error requests."""
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("""SELECT date_part('month', day) as month,
        date_part('day', day) as day, date_part('year', day) as year,
        CAST (round(percentage, 2) AS real) as percentage
        FROM error_percentage WHERE percentage >= 1;""")
    days = cursor.fetchall()
    db.close()
    return days
