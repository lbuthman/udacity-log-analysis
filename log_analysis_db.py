import psycopg2

DBNAME = 'news'


def execute_query(query):
    """Helper function that connects to database and executes
    passed query. Returns a list of tuples containing query results."""
    try:
        db = psycopg2.connect(database=DBNAME)
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        db.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def get_top_three_articles():
    """"Return the three most popular articles of all time."""
    query = """SELECT title, COUNT(*) AS total FROM log
        JOIN articles ON log.path = '/article/' || articles.slug
        WHERE status != '404 NOT FOUND' AND path != '/'
        GROUP BY title ORDER BY total DESC LIMIT 3;"""
    articles = execute_query(query)
    return articles


def get_top_authors():
    """"Return the most popular authors of all time."""
    query = """SELECT name, COUNT(*) as total FROM log
        JOIN author_article ON log.path = '/article/' || author_article.slug
        GROUP BY name ORDER BY total DESC;"""
    authors = execute_query(query)
    return authors


def get_top_error_days():
    """Returns days >= 1 Percent error requests."""
    query = """SELECT day, CAST (round(percentage, 2) AS real)
        AS percentage FROM error_percentage WHERE percentage >= 1;"""
    days = execute_query(query)
    return days
