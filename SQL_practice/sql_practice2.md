# SQL Database

### SQL CREATE DATABASE Statement
The CREATE DATABASE statement is used to create a new SQL database.
>CREATE DATABASE TempDB;

### SQL DROP DATABASE Statement
The DROP DATABASE statement is used to drop an existing SQL database.
>DROP DATABASE TempDB

### SQL BACKUP DATABASE Statement
The BACKUP DATABASE statement is used in SQL Server to create a full back up of an existing SQL database.
>BACKUP DATABASE databasename
TO DISK = 'filepath';

SQL BACKUP WITH DIFFERENTIAL Statement:
A differential back up only backs up the parts of the database that have changed since the last full database backup.
>BACKUP DATABASE databasename
TO DISK = 'filepath'
WITH DIFFERENTIAL;

### SQL CREATE TABLE Statement
The CREATE TABLE statement is used to create a new table in a database.
>CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);


### Create Table Using Another Table
A copy of an existing table can also be created using CREATE TABLE.
The new table gets the same column definitions. All columns or specific columns can be selected.
If you create a new table using an existing table, the new table will be filled with the existing values from the old table.
>CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers;

### SQL DROP TABLE Statement
The DROP TABLE statement is used to drop an existing table in a database.
>DROP TABLE customer;


### SQL TRUNCATE TABLE
The TRUNCATE TABLE statement is used to delete the data inside a table, but not the table itself.
>TRUNCATE TABLE customer;


### SQL ALTER TABLE Statement
The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.
The ALTER TABLE statement is also used to add and drop various constraints on an existing table.

The following SQL adds an "Email" column to the "Customers" table:
>ALTER TABLE Customers
ADD Email varchar(255);

ALTER TABLE - DROP COLUMN:
The following SQL deletes the "Email" column from the "Customers" table:
>ALTER TABLE Customers
DROP COLUMN Email;

ALTER TABLE - RENAME COLUMN:
>ALTER TABLE table_name
RENAME COLUMN old_name to new_name;


### ALTER TABLE - ALTER/MODIFY DATATYPE
To change the data type of a column in a table, use the following syntax:
>ALTER TABLE customer
ALTER COLUMN salary FLOAT;


### ALTER TABLE - ADD COLUMN
>ALTER TABLE customer
ADD mobile NUMBER;

### ALTER TABLE - DROP COLUMN
>ALTER TABLE customer
DROP COLUMN mobile;


### SQL Constraints
SQL constraints are used to specify rules for the data in a table.

Constraints are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. If there is any violation between the constraint and the data action, the action is aborted.

Constraints can be column level or table level. Column level constraints apply to a column, and table level constraints apply to the whole table.

The following constraints are commonly used in SQL:

* NOT NULL - Ensures that a column cannot have a NULL value
* UNIQUE - Ensures that all values in a column are different
* PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
* FOREIGN KEY - Prevents actions that would destroy links between tables
* CHECK - Ensures that the values in a column satisfies a specific condition
* DEFAULT - Sets a default value for a column if no value is specified
* CREATE INDEX - Used to create and retrieve data from the database very quickly

### NOT NULL on CREATE TABLE
The following SQL ensures that the "ID", "LastName", and "FirstName" columns will NOT accept NULL values when the "Persons" table is created:
>CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Age int
);

NOT NULL on ALTER TABLE :
>ALTER TABLE Person 
ADD COLUMN Age INT NOT NULL;

### SQL UNIQUE Constraint
The UNIQUE constraint ensures that all values in a column are different.
Both the UNIQUE and PRIMARY KEY constraints provide a guarantee for uniqueness for a column or set of columns.
A PRIMARY KEY constraint automatically has a UNIQUE constraint.
However, you can have many UNIQUE constraints per table, but only one PRIMARY KEY constraint per table.

>CREATE TABLE Persons (
    ID int NOT NULL UNIQUE,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

SQL UNIQUE Constraint on ALTER TABLE:
To create a UNIQUE constraint on the "ID" column when the table is already created.
>ALTER TABLE Persons
ADD UNIQUE (ID);

DROP a UNIQUE Constraint:
>ALTER TABLE Persons
DROP CONSTRAINT UC_Person;


### PRIMARY KEY Constraint
The PRIMARY KEY constraint is used to uniquely identify each record in a table.
Primary keys must contain unique values, and cannot contain NULL values.
Each table can have only ONE primary key. The primary key can be a single column or a combination of columns.
>CREATE TABLE Persons (
    ID INT NOT NULL PRIMARY KEY
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

### PRIMARY KEY on ALTER TABLE

To create a PRIMARY KEY constraint on the "ID" column when the table is already created, use the following SQL:

> ALTER TABLE customer
ADD PRIMARY KEY(id)

### DROP a PRIMARY KEY Constraint
To drop a PRIMARY KEY constraint, use the following SQL:
>ALTER TABLE customer
DROP PRIMARY KEY;


### FOREIGN KEY Constraint
The FOREIGN KEY constraint is used to prevent actions that would destroy links between tables.
A FOREIGN KEY is a field (or collection of fields) in one table, that refers to the PRIMARY KEY in another table.
The table with the foreign key is called the child table, and the table with the primary key is called the referenced or parent table.
>CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);

### FOREIGN KEY on ALTER TABLE
To create a FOREIGN KEY constraint on the "PersonID" column when the "Orders" table is already created, use the following SQL:
>ALTER TABLE customer
ADD FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);


### DROP a FOREIGN KEY Constraint
To drop a FOREIGN KEY constraint, use the following SQL:
>ALTER TABLE customer
DROP FOREIGN KEY PersonID;


### SQL CHECK Constraint
The CHECK constraint is used to limit the value range that can be placed in a column.
If you define a CHECK constraint on a column it will allow only certain values for this column.
If you define a CHECK constraint on a table it can limit the values in certain columns based on values in other columns in the row.
>CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);

### SQL CHECK on ALTER TABLE
>ALTER TABLE Persons
ADD CHECK(Age >= 18)

### DROP CHECK on ALTER TABLE
>ALTER TABLE Persons
DROP CHECK Age


### SQL DEFAULT Constraint
The DEFAULT constraint is used to set a default value for a column.
The default value will be added to all new records, if no other value is specified.
The following SQL sets a DEFAULT value for the "City" column when the "Persons" table is created:
>CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255) DEFAULT 'Sandnes'
);

### ADD DEFAULT with ALTER 
>ALTER TABLE Persons
ALTER city SET DEFAULT 'Indore';

### DROP DEFAULT with alter
>ALTER TABLE Persons
ALTER city DROP DEFAULT;


### SQL CREATE INDEX Statement
The CREATE INDEX statement is used to create indexes in tables.
Indexes are used to retrieve data from the database more quickly than otherwise. The users cannot see the indexes, they are just used to speed up searches/queries.

CREATE INDEX Example
The SQL statement below creates an index named "idx_lastname" on the "LastName" column in the "Persons" table:
>CREATE INDEX idx_lastname
ON Persons(lastname)

If you want to create an index on a combination of columns, you can list the column names within the parentheses, separated by commas:
>CREATE INDEX idx_pname
ON Persons (LastName, FirstName);

### DROP INDEX Statement
The DROP INDEX statement is used to delete an index in a table.
>ALTER TABLE Persons
DROP INDEX idx_lastname;

### AUTO INCREMENT Field
Auto-increment allows a unique number to be generated automatically when a new record is inserted into a table.
Often this is the primary key field that we would like to be created automatically every time a new record is inserted.
>CREATE TABLE Persons (
    Personid int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (Personid)
);

### SQL Date Data Types
MySQL comes with the following data types for storing a date or a date/time value in the database:

DATE - format YYYY-MM-DD
DATETIME - format: YYYY-MM-DD HH:MI:SS
TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
YEAR - format YYYY or YY

### SQL CREATE VIEW Statement
In SQL, a view is a virtual table based on the result-set of an SQL statement.
A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.
You can add SQL statements and functions to a view and present the data as if the data were coming from one single table.
A view is created with the CREATE VIEW statement. 

>CREATE VIEW [Brazil_Customers] AS
SELECT Name, Contact, City FROM Customers 
WHERE Country = 'Brazil';

### SQL Updating a View
A view can be updated with the CREATE OR REPLACE VIEW statement.
>CREATE OR REPLACE VIEW [Brazil_Customers] AS
SELECT Name, Contact, City FROM Customers 
WHERE Country = 'Brazil';

### DROP a VIEW

```sql
DROP VIEW [Brazil_Customers];
```

