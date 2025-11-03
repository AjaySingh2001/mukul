# SQL Commands 

SQL is a standard language for storing, manipulating and retrieving data in databases.

### The following SQL statement returns all records from a table named "Customers":
>select * from customers;

### Some of The Most Important SQL Commands
SELECT - extracts data from a database
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index

### select distinct values from columns

>select distinct city from customers;

### The SQL WHERE Clause
The WHERE clause is used to filter records.
It is used to extract only those records that fulfill a specified condition.

>SELECT * FROM Customers
>WHERE CustomerID=1;

### Operators

* = - Equal,
* < - Lessthen,
* (>) - Greaterthen,
* <= - Lessthen or equal to,
* (>=) - Lessthen or equal to,
* <> - Not equal to,
* BETWEEN - " BETWEEN 50 AND 60 ",
* IN  - IN ('Paris','London'),
* LIKE - " LIKE 's%' ",


### The SQL ORDER BY

The ORDER BY keyword is used to sort the result-set in ascending or descending order.
Default it order in ascending.

>SELECT * FROM Products
>ORDER BY Price;

For alphabetical order(asc, desc) use column name
>SELECT * FROM Products
>ORDER BY PoductName;

### The SQL AND, OR, NOT Operator

>select * from customer
where name = "Ram" and salary = '100000'


>select * from customer
where name = "Ram" OR name = "Rama"


>select * from customer
where NOT name = "rahul" 

>select * from customer
where salary IN (100000,200000)


### Insert Data into table

>INSERT INTO Customers (CustomerName, City, Country)
>VALUES ('Cardinal', 'Stavanger', 'Norway'),
>       ('Cardinal1', 'Stavanger1', 'Norway1'),
>       ('Cardinal3', 'Stavanger3', 'Norway3');

### Difference between '=' and 'is'
| Comparison | Example              | Used For            | Meaning                            | Notes                          |
| ---------- | -------------------- | ------------------- | ---------------------------------- | ------------------------------ |
| `=`        | `Salary = 50000`     | Normal comparison   | Checks if two values are **equal** | Works with numbers, text, etc. |
| `IS NOT`   | `Salary IS NOT NULL` | **NULL comparison** | Checks if a value is **not NULL**  | Works only with `NULL` values  |


### The SQL UPDATE Statement

The UPDATE statement is used to modify the existing records in a table.

> UPDATE FROM Customer SET salary = 10000  WHERE id = 4;

### The SQL DELETE Statement

The DELETE statement is used to delete existing records in a table.

> DELETE FROM Customer WHERE id = 4;

Delete All Records

> DELETE FROM Customer;

### Delete a Table

To delete the table completely, use the DROP TABLE statement:

> DROP TABLE Customer;


### SQL Aggregate Functions
An aggregate function is a function that performs a calculation on a set of values, and returns a single value.
Aggregate functions are often used with the GROUP BY clause of the SELECT statement. 
The GROUP BY clause splits the result-set into groups of values and the aggregate function can be used to return a single value for each group.

SQL aggregate functions are:

MIN() - returns the smallest value within the selected column
MAX() - returns the largest value within the selected column
COUNT() - returns the number of rows in a set
SUM() - returns the total sum of a numerical column
AVG() - returns the average value of a numerical column

> SELECT MIN(salary), MAX(salary), AVG(salary), COUNT(*)
  FROM OrderDetails;

> SELECT OrderID, SUM(Quantity) AS [Total Quantity]
  FROM OrderDetails
  GROUP BY OrderID;


### The SQL LIKE Operator

The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

> SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';

Like examples - 
* 'L_nd__' - Return all customers from a city that starts with 'L' followed by one wildcard character, then 'nd' and then two wildcard characters.
* '%L%' - Return all customers from a city that contains the letter 'L'.
* 'La%' - Return all customers that starts with 'La'.
* '%a' - Return all customers that ends with 'a'.
* 'b%s' - Return all customers that starts with "b" and ends with "s".
* '%or%' - Return all customers that contains the phrase 'or'.


### Using the [] Wildcard

Return all customers starting with either "b", "s", or "p":

> SELECT * FROM Customers
  WHERE CustomerName LIKE '[bsp]%';


### Aliases

SQL aliases are used to give a table, or a column in a table, a temporary name.

> SELECT CustomerID AS ID
FROM Customers;
AS is Optional

> SELECT CustomerID ID
FROM Customers;


### SQL JOIN
A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

there are different types of the JOINs in SQL:
JOIN and INNER JOIN will return the same result.
INNER JOIN: Returns records that have matching values in both tables:

>SELECT ProductID, ProductName, CategoryName
FROM Products
INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID;

LEFT JOIN: Returns all records from the left table, and the matched records from the right table:

>SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;

RIGHT JOIN: Returns all records from the right table, and the matched records from the left table:

>SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;

FULL JOIN: Returns all records when there is a match in either left or right table.

>SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName;

### SQL Self Join
A self join is a regular join, but the table is joined with itself.

>SELECT E.emp_name AS Employee, m.emp_name AS Manager 
FROM Employee e join Employee m
ON e.manager_id = m.emp_id;







