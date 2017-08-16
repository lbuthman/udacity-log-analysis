# Log Analysis Project

The Log Analysis project aims to simplify the process of answering the following
questions from the news database (provided).

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Required Setup

While the Log Analysis Tool is easy to use, there is a bit of setup
required to get going. Nothing too complicated though.

1. <a href="https://www.virtualbox.org/wiki/Downloads">Virtual Box (download here)</a> 
    - "VirtualBox is a general-purpose full virtualizer for x86 hardware, targeted 
    at server, desktop and embedded use."
    - Translation: Think virtual computer.
    VirtualBox gives you a virtual computer you can play with, break, and rebuild
    without damaging your actual computer. Nifty! :bowtie:
    - Instructions: Simply install the correct platform package for your Operating
    System. Once installed, you don't even need to open it.

2. <a href="https://www.vagrantup.com/downloads.html">Vagrant (download here)</a>
    - "Vagrant 
    is a tool for building and managing virtual machine environments in a single 
    workflow."
    - Translation: Think helper for VirtualBox.
    - Instructions: Simply install the correct version for your Operating System.
    - Warning for Windows users: The Installer may ask you to grant network 
    permissions to Vagrant or make a firewall exception. Be sure to allow this.
    - Verify: To verify the installation setup, open your Terminal and type
    `vagrant --version`. If successful, you will see your Vagrant version.

3. <a href="https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip">FSND-Virtual-Machine (download here)</a>
    - What? You don't know how to setup VirtualBox and Vagrant? No worries, 
    the good folks at Udacity have created one for you! Sweet!
    - Even if you already know how to use VirtualBox and Vagrant, you still need
    to download and use this Vagrant build. It is preconfigured with necessary
    applications, plugins, and databases required for this tool.
    - Instructions: 
        1) Unzip the folder and (optionally) move it into the directory
    you want it to live in (I use Documents).
        2) Use the terminal to cd into the directory `cd Documents/FSND-Virtual-Machine`
        3) Run the command `vagrant up` to start your Virtual Machine.
        4) Wait for a while :) -- this will take some time since it is installing 
        an entire computer on your computer. Think about that! (\**mind explodes**)
        5) Once completed, your shell will return the prompt you are used to
        seeing. From here, you can log in to your new computer by typing
        `vagrant ssh` into the shell.
        6) Run the command `cd /vagrant`

4. <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">News Data SQL (download here)</a>
    - This will download the newsdatabase.sql file, which will create the
    database the program will run against. The database will be discuss more
    below, but for now, let's just get it ready.
    - Instructions: 
        1) After unzipping the download, move newsdatabase.sql to your
        vagrant directory. Ex. Documents/FSND-Virtual-Machine/vagrant
        2) Run the command `psql -d news -f newsdata.sql`
    
5. <a href="/create_views.sql">Create Views (download here)</a>
    - This will download the create_views.sql file, which will create the views
    needed for the application's database queries.
    - Instructions:
        1) Just like before, unzip the download and move create_views.sql to
        your vagrant direction. Ex. Documents/FSND-Virtual-Machine/vagrant
        2) Run the command `psql -d news -f create_views.sql`

## Running the Application

Phew! That was a little work getting everything setup. Good job! You are now
ready to run the application. Don't worry, this part is easy. :relieved:

1. Start the application from your terminal `python3 log_analysis.py`
2. The application will print a menu. Enter the number of the question you
would like to answer and press Enter.
3. The result output will display once the query completes! Easy!
4. Press 0 and Enter to quit at any time.

## The News Database

The 'news' database is a PostgreSQL database filled with logs for a pretend,
nameless news paper company. (Although, we could call it Fake News Inc.) The
database is filled with 'logs' from 'user requests'.

The database contains three tables: 'authors', 'articles', and 'log'. I would
encourage you to explore the databases if you are familiar with PostgreSQL, but
you don't need to know much about them to run the application. 

## Advanced Usage

Note: This log analysis tools relies on a few Views. When you went through the
setup above, you actually installed each of these views already. However, it
might be nice to know a bit more about them. You can find each below.

```sql
CREATE VIEW author_article AS
SELECT name, slug
FROM authors, articles
WHERE authors.id = articles.author;
```

```sql
CREATE VIEW view_errors AS
SELECT log.time::date AS day, COUNT(*)
FROM log 
WHERE status = '404 NOT FOUND'
GROUP BY day;
```

```sql
CREATE VIEW view_total AS 
SELECT log.time::date AS day, COUNT(*) 
FROM log 
GROUP BY day;
```

```sql
CREATE VIEW error_percentage AS 
SELECT view_total.day, (view_errors.count::decimal / view_total.count) * 100 AS percentage 
FROM view_total, view_errors 
WHERE view_total.day = view_errors.day;
```
