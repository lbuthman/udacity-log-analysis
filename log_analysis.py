#!/usr/bin/env python3

import log_analysis_db

print("\n\tHi! And welcome to the Easy News database analysis tool.")

MENU = """
\tPlease enter the number of the query you would like to perform.\n
\t1 - Discover the three most popular articles of all time.
\t2 - See all authors ranked in popularity, most popular on top.
\t3 - Find the days with error requests 1% or more
\t0 - quit\n
\tEnter your choice here: """


def print_articles(articles):
    """Prints article name and total views for each article to standard out"""
    for article in articles:
        print("\tArticle Title: {} -- Total Views: {}".format(
            article[0], article[1]))


def print_authors(authors):
    """Prints author names and total views for all written articles to standard out"""
    for author in authors:
        print("\tAuthor Name: {} -- Total Views: {}".format(
            author[0], author[1]))


def print_days(days):
    """Prints each date with error response percentage"""
    for day in days:
        date = day[0].strftime('%B %d, %Y')
        percent = day[1]
        print("\tDay: {} -- Error Responses: {}%".format(
            date, percent))


while True:
    query = input(MENU)

    try:
        query = int(query)
    except ValueError:
        print()  # error message handled in else below

    if query == 0:
        print("\tHave a good day!\n")
        break

    elif query == 1:
        print("\tYou selected 1. Hang tight, looking now ...\n")
        print_articles(log_analysis_db.get_top_three_articles())

    elif query == 2:
        print("\tYou selected 2. Uno momento while I look ...\n")
        print_authors(log_analysis_db.get_top_authors())

    elif query == 3:
        print("\tYou selected 3. This shouldn't take long.\n")
        print_days(log_analysis_db.get_top_error_days())

    else:
        print("\tSorry, I don't recognize that input ...\n")
