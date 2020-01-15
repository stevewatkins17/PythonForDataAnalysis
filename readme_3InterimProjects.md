# Overview - Interim Projects - Python for Data Analysis 

This course requires the submission of three small interim Python projects, each of which builds off the previous one (conceptually & technically). 

You may think of these interim projects as "stair steps" leading to a larger data analytics project. 

That said, no project deliverable is "locked in" to the previous one. Your next project may shift directions, methods, topics, data sources etc from that which you produced for the previous deliverable. 

Just realize that when you do switch directions, you will end up re-working that which you did before, for the new direction that you've chosen.


## Install Requirements

- Anaconda distribution of Python (https://www.anaconda.com/distribution/)
- git desktop client (https://git-scm.com/downloads)


## Standard Tools

So that we can technically discuss and demonstrate from a common toolset, we will be using & demoing the following:

- Python Version: 3.6 & up (from Anaconda)
- IDE: Jupyter Notebook (from Anaconda)
- Database: SQLite (part of the standard Python 3x library)

Special Packages: none outside of Anaconda
 
Simply installing the full Anaconda distribution installs everything Python you need to deliver your interim projects.

Note that we will be instructing and demoing using the Standard Tools, and we assume you have Anaconda installed. 

We strongly discourage you from using versions of Python not supported by Anaconda, or using IDEs or DBMSes not installed with Anaconda. 

**Occasionally students ignore the above advice and work outside of Anaconda. It almost always leads to problems and failed deliveries.**


# Summary Description of 3 Interim Projects

Each are detailed further below.

1. Import a data source into a Python object, and then view the data source in Python. Note that for this first interim project, we will provide a simple sample data source for those who do not choose their own data source. 

2. Perform #1 above, plus create a Sqlite database and store your imported datasource into the Sqlite database; query the Sqlite database and return the dataset to Python and display the output.

3. Perform 1 & 2 above, plus transform the data -- in either Sqlite or Python -- into a 2nd, aggregated data table or object. Display the aggregated dataset.


## Project delivery requirements

The following are Interim Project delivery requirements:

- git repo -- your interim project deliverable should be stored in your git repo. 

- executable Python script -- QA (the 3rd party who tests your project) will clone your repo & execute your Python. It will succeed or fail. 

- readme.md -- instructions/help for the QA tester. 

Keep in mind that the above is the bare minimum; you are more than welcome to over-deliver on the minimum requirements.


## Delivery dates

An interim project will be due every two weeks, the counter beginning with the 2nd class meeting (Week 7 would be the 3rd delivery date).

Think of these as two-week dev sprints, where you incrementally deliver working code to QA every two weeks.


# Detailed Description of Each Interim Project


## 1. Import a data source

In Python:

1. Import any datasource or use the data source that we will provide (a [csv](https://en.wikipedia.org/wiki/Comma-separated_values) file):

The datasource can be:
- flat txt files (ascii, csv)
- docs (xml, json, yml)
- Excel spreadsheets
- database query results (relational/nosql)
- api calls

2. Imported into any Python object
The Python object could be:
- pandas data frame
- tuple of lists
- dictionary

3. Print output the data source
Display the datasource, within reason, for visual confirmation. This may require iterating through a dataset, or a custom pandas call.


## 2. Write to DB; Read from DB

In Python:

1. Perform #1 above
2. create a Sqlite database
3. Create staging table in sqlite DB (if your Python write method does not create a table as part of its method)
3. write the Python datasource object data to the SQLite staging table
4. Query the table and display the results in Python
5. Close DB conn.


## 3. Transform the data

In Python:

1. Perform 1 & 2 above
2. In Python or SQL:
-- query the data from the SQLite staging table
-- in the query, transform the data and store into a 2nd database table or python object. 
-- transform must include at least 1 aggregation, and 1 value manipulation or datatype redefinition
3. Display the new dataset.

# 8-Week Schedule

## Week 1 - Introduction
**Student Challenge 1.1** - Anaconda installed; open Jupyter Notebook, create any Python3 Notebook file.

**Student Challenge 1.2** - Git installed; Github online account complete; clone your git repo to your local machine.

## Week 2 - Choose & Import a datasource into Python
**Student Challenge 2.1** - Choose a datasource

**Student Challenge 2.2** - import datasource into Python3 object (Pandas dataframe or Python list of tuples)

**Student Challenge 2.3** - display imported datasource (print to screen)

## Week 3 - Interim Project 1 due
Students will choose a partner to perform code review; partner will clone student's repo & execute project code successfully.

## Week 4 - Read/Write to relational DB
**Student Challenge 4.1** - create a DB and a table inside the DB. Can be any relational, ACID-compliant DBMS (SQLite, Oracle, MSSQL, Mysql, postgresql, DB2 etc.) but we will focus on SQLite which is already implemented as part of Python3.

**Student Challenge 4.2** - use SQL language to manipulate/clean/reformat data inside a DBMS table.

**Student Challenge 4.3** - Using Python or SQL, recast a data column or element from 1 data type to another.

## Week 5 - Interim Project 2 due
Students will choose a partner to perform code review; partner will clone student's repo & execute project code successfully.

## Week 6 - Data Transform/Aggregation

**Student Challenge 6.1** - Using Python or SQL, cast or convert data values from one state to another ("case" or "switch") 

**Student Challenge 6.2** - Using Python or SQL, transform your imported data set by aggregating it in some way.

## Week 7 - Interim Project 3 due
Students will choose a partner to perform code review; partner will clone student's repo & execute project code successfully.

## Week 8 - Final class
Final wrap-up & reviews


