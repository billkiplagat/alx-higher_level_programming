# MySQLdb

# How to install MySQLdb
1. Install pkg-config and the development libraries for MySQL
 
`sudo apt-get install pkg-config libmysqlclient-dev`
2. Install mysqlclient
 
`pip3 install mysqlclient`

MySQLdb, also known as mysqlclient, is a Python library used to connect to and interact with MySQL databases.
Here's an example of how you can use MySQLdb to connect to a MySQL database and retrieve data:
* Import the MySQLdb library

 `import MySQLdb`

* Connect to the MySQL database

` db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="mydatabase") `

* Create a cursor object to interact with the database

 `cursor = db.cursor()`

* Execute a SQL query to retrieve data

` cursor.execute("SELECT * FROM employees")`

* Fetch the result

` result = cursor.fetchall()`

* Print the data

`for row in result:
    print(row)`

* Close the database connection

` db.close()`

# SQLAlchemy:

SQLAlchemy is another Python library for working with databases, but it's more like a toolset that can work with various database systems, not just MySQL

Here's a simplified example of how you can use SQLAlchemy to create a simple SQLite database and add data to it:

* Import SQLAlchemy

` from sqlalchemy import create_engine, Column, Integer, String`

` from sqlalchemy.orm import sessionmaker`

`from sqlalchemy.ext.declarative import declarative_base`

* Create a PostgreSQL database
* Replace 'username', 'password', 'host', and 'dbname' with your PostgreSQL credentials

`db_url = "postgresql://username:password@host/dbname"`

`engine = create_engine(db_url)`

* Create a base class for defining database models
Base = declarative_base()

* Define a database model (a table)

`class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)`

* Create the database tables

`Base.metadata.create_all(engine)`

* Create a session to interact with the database

`Session = sessionmaker(bind=engine)`

`session = Session()`

* Add data to the database

` new_employee = Employee(name="Alice", age=30)`

`session.add(new_employee)`

`session.commit()`

* Query data from the database

`employee = session.query(Employee).filter_by(name="Alice").first()`

`print(employee.name, employee.age)`

* Close the session

`session.close()`

# What ORM means:

ORM stands for Object-Relational Mapping. It's a programming technique that allows you to work with relational databases using object-oriented programming languages like Python. 
It helps bridge the gap between the database and the application code by mapping database tables to Python classes and database rows to objects. This makes it easier to interact with databases in a more Pythonic way.

