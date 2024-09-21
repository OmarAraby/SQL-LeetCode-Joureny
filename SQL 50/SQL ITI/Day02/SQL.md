- SQL ⇒ Structured Query Language
- SQL is a programming language used by nearly all [relational databases](https://www.oracle.com/ca-en/database/what-is-database/#relational) to query, manipulate, and define data, and *to provide access control*.
- ANSI SQL ⇒ **American National Standards Institute Structured Query Language**

![[Pasted image 20240715004239.png]]

## Microsoft Transact-SQL  commands
![[Pasted image 20240715005352.png]]
##### **Data definition language**
> Data definition language (DDL) refers to SQL commands that design the database structure. Database engineers use DDL to create and modify database objects based on the business requirements

##### **Data query language**

> Data query language (DQL) consists of instructions for retrieving data stored in relational databases. Software applications use the SELECT command to filter and return specific results from a SQL table.

##### **Data manipulation language**

> Data manipulation language (DML) statements write new information or modify existing records in a relational database.

##### **Data control language**

> Database administrators use data control language (DCL) *to manage or authorize database access for other users*. For example, they can use the GRANT command to permit certain applications to manipulate one or more tables.

##### **Transaction control language**

> The relational engine uses transaction control language (TCL) *to automatically make database changes*. For example, the database uses the ROLLBACK command to undo an erroneous transaction.
#### When you create new database…
    
there are two file
1. filename.mdf ⇒ metadata file → table,
2. filename.ldf ⇒ log file → any modify on data as archive
![[Pasted image 20240715010706.png]]

![[Pasted image 20240715010338.png]]



#### Comparison Operators


| **Operator**        | **Condition**                                        | **SQL Example**               |
| ------------------- | ---------------------------------------------------- | ----------------------------- |
| =, !=, <, <=, >, >= | Standard numerical operators                         | col_name != 4                 |
| BETWEEN … AND …     | Number is within range of two values (inclusive)     | col_name BETWEEN 1.5 AND 10.5 |
| NOT BETWEEN … AND … | Number is not within range of two values (inclusive) | col_name NOT BETWEEN 1 AND 10 |
| IN (…)              | Number exists in a list                              | col_name IN (2, 4, 6)         |
| NOT IN (…)          | Number does not exist in a list                      | col_name NOT IN (1, 3, 5)     |



| **Operator** | **Condition**                                                                                         | **Example**                                                             |
| ------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| =            | Case sensitive exact string comparison (_notice the single equals_)                                   | col_name = "abc"                                                        |
| != or <>     | Case sensitive exact string inequality comparison                                                     | col_name != "abcd"                                                      |
| LIKE         | Case insensitive exact string comparison                                                              | col_name LIKE "ABC"                                                     |
| NOT LIKE     | Case insensitive exact string inequality comparison                                                   | col_name NOT LIKE "ABCD"                                                |
| %            | Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE) | col_name LIKE "%AT%"  <br>(matches "AT", "ATTIC", "CAT" or even "BATS") |
| __           | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE)                    | col-name LIKE "AN_ "  <br>(matches "AND", but not "AN")                 |
| IN (…)       | String exists in a list                                                                               | col_name IN ("A", "B", "C")                                             |
| NOT IN (…)   | String does not exist in a list                                                                       | col_name NOT IN ("D", "E", "F")                                         |



### **Stored procedures**

Stored procedures are a collection of one or more SQL statements stored in the relational database. Software developers use stored procedures to improve efficiency and performance. For example, they can create a stored procedure for updating sales tables instead of writing the same SQL statement in different applications.

## What is SQL injection?

SQL injection is a cyberattack that involves tricking the database with SQL queries. Hackers use SQL injection to retrieve, modify, or corrupt data in a SQL database. For example, they might fill in a SQL query instead of a person's name in a submission form to carry out a SQL injection attack.
### SQL vs. MySQL

- Structured query language (SQL) is a standard language for database creation and manipulation. 
- MySQL is a relational database program that uses SQL queries. While SQL commands are defined by international standards, the MySQL software undergoes continual upgrades and improvements.

## What is NoSQL?

[NoSQL](https://aws.amazon.com/nosql/) refers to non-relational databases that don't use tables to store data. Developers store information in different types of NoSQL databases, i*ncluding graphs, documents, and key-value*s. NoSQL databases are popular for modern applications because they are horizontally scalable.* Horizontal scaling means increasing the processing power by adding more computers that run NoSQL software*.

### SQL vs. NoSQL

Structured query language (SQL) provides a uniform data manipulation language, but NoSQL implementation is dependent on different technologies. Developers use SQL for transactional and analytical applications, whereas NoSQL is suitable for responsive, heavy-usage applications





# SQL Constraints

In a database table, we can add rules to a column known as **constraints**. These rules control the data that can be stored in a column.

For example, if a column has `NOT NULL` constraint, it means the column cannot store `NULL` values.

*The constraints used in SQL are*:

| Constraint     | Description                         |
| -------------- | ----------------------------------- |
| `NOT NULL`     | values cannot be null               |
| `UNIQUE`       | values cannot match any older value |
| `PRIMARY KEY`  | used to uniquely identify a row     |
| `FOREIGN KEY`  | references a row in another table   |
| `CHECK`        | validates condition for new value   |
| `DEFAULT`      | set default value if not passed     |
| `CREATE INDEX` | used to speedup the read process    |
|                |                                     |
#### NOT NULL Constraint
The `NOT NULL` constraint in a column means that the column cannot store `NULL` values. For example,

```sql

CREATE TABLE Colleges (
  college_id INT NOT NULL,
  college_code VARCHAR(20) NOT NULL,
  college_name VARCHAR(50)
);
```

Here, the college_id and the college_code columns of the Colleges table won't allow `NULL` values.


#### UNIQUE Constraint

The `UNIQUE` constraint in a column means that the column must have unique value. For example,

```sql
CREATE TABLE Colleges (
  college_id INT NOT NULL UNIQUE,
  college_code VARCHAR(20) UNIQUE,
  college_name VARCHAR(50)
);
```

Here, the value of the college_code column must be unique. Similarly, the value of college_id must be unique as well as it cannot store `NULL` values.



#### PRIMARY KEY Constraint

The `PRIMARY KEY` constraint is simply a combination of `NOT NULL` and `UNIQUE` constraints. It means that the column value is used to uniquely identify the row. For example,

```sql
CREATE TABLE Colleges (
  college_id INT PRIMARY KEY,
  college_code VARCHAR(20) NOT NULL,
  college_name VARCHAR(50)
);
```

Here, the value of the college_id column is a unique identifier for a row. Similarly, it cannot store `NULL` value and must be `UNIQUE`


#### FOREIGN KEY Constraint

The `FOREIGN KEY` (`REFERENCES` in some databases) constraint in a column is used to reference a record that exists in another table. For example,

```sql
CREATE TABLE Orders (
  order_id INT PRIMARY KEY,
  customer_id int REFERENCES Customers(id)
);
```

Here, the value of the college_code column references the row in another table named Customers.

It means that the value of customer_id in the Orders table must be a value from the id column of the Customers table


#### CHECK Constraint

The `CHECK` constraint checks the condition before allowing values in a table. For example,

```sql
CREATE TABLE Orders (
  order_id INT PRIMARY KEY,
  amount int CHECK (amount >= 100)
);
```

Here, the value of the amount column must be **greater than or equal to 100**. If not, the SQL statement results in an error.

#### DEFAULT Constraint

The `DEFAULT` constraint is used to set the default value if we try to store `NULL` in a column. For example,

```sql
CREATE TABLE College (
  college_id INT PRIMARY KEY,
  college_code VARCHAR(20),
  college_country VARCHAR(20) DEFAULT 'EGY'
);
```

Here, the default value of the college_country column is **EGY**.

If we try to store the `NULL` value in the college_country column, its value will be **EGY**.


#### CREATE INDEX Constraint

If a column has `CREATE INDEX` constraint, it's faster to retrieve data if we use that column for data retrieval. For example,

```SQL
-- create table
CREATE TABLE Colleges (
  college_id INT PRIMARY KEY,
  college_code VARCHAR(20) NOT NULL,
  college_name VARCHAR(50)
);

-- create index
CREATE INDEX college_index
ON Colleges(college_code);
```

Here, the SQL command creates an index named `college_index` on the `Colleges` table using `college_code` column.


  
### DROP and TRUNCATE in SQL

***DROP and TRUNCATE in SQL*** remove data from the table. The main difference between DROP and TRUNCATE commands in SQL is that DROP removes the table or database completely, while TRUNCATE only removes the data, preserving the table structure.

Let’s understand both these SQL commands in detail below:

#### Differences Between DROP and TRUNCATE

The key differences between DROP and TRUNCATE statements are explained in the following table:

| DROP                                                                                                           | TRUNCATE                                                                                |
| -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| In the drop table data and its definition is deleted with their full structure.                                | It preserves the structure of the table for further use exist but deletes all the data. |
| Drop is used to eliminate existing complications and fewer complications in the whole database from the table. | Truncate is used to eliminate the tuples from the table.                                |
| Integrity constraints get removed in the DROP command.                                                         | Integrity constraint doesn’t get removed in the Truncate command.                       |
| Since the structure does not exist, the View of the table does not exist in the Drop  command.                 | Since the structure exists, the View of the table exists in the Truncate command.       |
| Drop query frees the table space complications from memory.                                                    | This query does not free the table space from memory.                                   |
| It is slow as there are so many complications compared to the TRUNCATE command.                                | It is fast as compared to the DROP command as there are fewer complications.            |
### SQL DROP Statement

> - Completely removes a table or database from the database, including the data and structure.
> - Is a permanent operation and cannot be rolled back.
> - Removes integrity constraints and indexes associated with the table.
> - Is slower compared to the TRUNCATE statement.


### SQL TRUNCATE Statement

> - Removes all the rows or data from a table, but preserves the table structure and columns.
> - Is a faster operation compared to the DROP statement.
> - Resets the identity column (if any) back to its seed value.
> - Does not remove integrity constraints associated with the table.