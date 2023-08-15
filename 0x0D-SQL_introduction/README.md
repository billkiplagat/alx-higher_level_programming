# SQL - Introduction
Welcome to the SQL Introduction guide! In this guide, you will learn the basics of SQL, a powerful language used to manage and manipulate data in relational databases.

# Lessons Learned
What's a Database?
A database is like a digital storage room for organizing information. It's a structured collection of data, organized into tables that hold different types of related information.

# What's a Relational Database?
A relational database is a type of database where data is stored in tables with rows and columns. The tables are connected by relationships, allowing us to retrieve and manipulate data efficiently.

# What Does SQL Stand For?
SQL stands for Structured Query Language. It's a language used to communicate with databases, allowing you to retrieve, insert, update, and delete data.

# What's MySQL?
MySQL is a popular open-source relational database management system. It uses SQL to manage and interact with data. It's widely used for various applications, from small websites to large-scale systems.

# How to Create a Database in MySQL
To create a database in MySQL, you can use the following SQL command:

`CREATE DATABASE DatabaseName;`
Replace DatabaseName with the name you want for your database.

# What Does DDL and DML Stand For?
DDL: Data Definition Language. It's used to define and manage the structure of the database, including creating and altering tables.
DML: Data Manipulation Language. It's used to manipulate the data within the database, including inserting, updating, and deleting data.
How to CREATE or ALTER a Table
To create a table in MySQL, you can use the following syntax:

`CREATE TABLE TableName (
    column1 datatype,
    column2 datatype,
    ...
);`
* To alter a table, you can use the ALTER TABLE command:

`ALTER TABLE TableName`
`ADD COLUMN newColumn datatype;`

# How to SELECT Data from a Table
* To retrieve data from a table, use the SELECT statement:

`SELECT column1, column2
FROM TableName
WHERE condition;`

# How to INSERT, UPDATE, or DELETE Data
* To insert new data:

`INSERT INTO TableName (column1, column2)
VALUES (value1, value2);`

* To update existing data:

`UPDATE TableName
SET column1 = newValue
WHERE condition;`

* To delete data:

`DELETE FROM TableName
WHERE condition;`

# What Are Subqueries?
Subqueries are like questions within questions. They allow you to perform queries inside other queries. For example, you can use a subquery to find the maximum value in a subset of data.

* How to Use MySQL Functions
MySQL functions perform calculations on data. For example, you can use the COUNT function to count the number of rows in a table:

`SELECT COUNT(*) FROM TableName;`