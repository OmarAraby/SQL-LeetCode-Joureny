[SQL Interview Questions](https://www.geeksforgeeks.org/sql-interview-questions/?ref=shm)


![[Database_Interview_Question[1].pdf]]

### SQL Handwritten 

![[SQL .pdf]]

![[Introduction to dataBase (final review) .pdf]]


![[ sql.pdf]]



##### what Stored Procedure and View?

**Stored Procedure**: A precompiled set of SQL statements that performs operations and can be called to execute complex tasks. Enhances performance and security.

**View**: A virtual table created from a SELECT query that simplifies data access and presentation without storing data itself. Provides abstraction and restricts data access.

##### how to do update in database?
```sql
UPDATE table_name

SET column1 = value1, column2 = value2, ...

WHERE condition;
```



  
  

##### what is trigger and types?

A **trigger** is a tool in a database that automatically performs a task when something happens, like adding or changing data in a table.

For example, you can use a trigger to automatically update a log whenever a record in a table is updated.

**Types:**

**- BEFORE Trigger****:** Runs before the event to validate or modify data.

**- AFTER Trigger**: Runs after the event, often used for logging or auditing.

**- INSTEAD OF Trigger**: Replaces the default behavior, typically used for views.

  
  

##### what is sql categoryies?
######  Data Definition Language (DDL)

- **Purpose**: Used to define and modify the structure of database objects like tables, indexes, and schemas.
    
- **Common Commands**:
    
    - **CREATE**: Creates new objects in the database (such as tables or indexes).
        
    - **ALTER**: Changes the structure of existing database objects (like adding a new column to a table).
        
    - **DROP**: Deletes database objects.
        
    - **TRUNCATE**: Deletes all data from a table but keeps the table structure intact.
        

###### Data Manipulation Language (DML)

- **Purpose**: Used to manipulate data within the database (add, modify, delete, or retrieve data).
    
- **Common Commands**:
    
    - **SELECT**: Retrieves data from the database.
        
    - **INSERT**: Adds new data into the database.
        
    - **UPDATE**: Modifies existing data in the database.
        
    - **DELETE**: Removes data from the database.
        

###### Data Control Language (DCL)

- **Purpose**: Used to control access to data in the database and define permissions for users.
    
- **Common Commands**:
    
    - **GRANT**: Gives users specific access rights to database objects (like permission to read or modify data).
        
    - **REVOKE**: Removes users' access rights to certain database objects.
###### Transaction Control Language (TCL)

- **Purpose**: Used to manage transactions in the database, ensuring data integrity during operations.
    
- **Common Commands**:
    
    - **COMMIT**: Saves all changes made during the current transaction permanently in the database.
        
    - **ROLLBACK**: Reverts changes made during the current transaction, undoing modifications.
        
    - **SAVEPOINT**: Sets a marker within a transaction to which you can rollback.
        
    - **SET TRANSACTION**: Defines properties for the transaction (such as the level of isolation).
        


##### View

- A `View` is a virtual table based on the result of a SQL query. It's used to simplify complex queries, secure sensitive data, and provide abstraction.
```sql
 CREATE VIEW HighSalaryEmployees AS 
 SELECT * FROM employees WHERE salary > 10000;
```
    
##### `UNION` vs `UNION ALL` vs `INTERSECT` vs `MINUS`

- **`UNION`**: Combines the result of two queries, removing duplicates.
```sql
SELECT first_name FROM employees
UNION
SELECT first_name FROM managers;
```
- **`UNION ALL`**: Combines the result of two queries, including duplicates. 
```sql
SELECT first_name FROM employees
UNION ALL
SELECT first_name FROM managers;
```

- **`INTERSECT`**: Returns only the rows that appear in both result sets (the common values).
```sql
SELECT first_name FROM employees
INTERSECT
SELECT first_name FROM managers;

```

- **`MINUS`** (or **`EXCEPT`** in some databases): Returns the rows in the first query that do not appear in the second query.
```sql
SELECT first_name FROM employees
MINUS
SELECT first_name FROM managers;

```
------------------------------------------------------------------------------------------------------------------------

web &ui

  
  

1) what is java script data types?

**Primitive Data Types**: `Number`, `BigInt`, `String`, `Boolean`, `Symbol`, `undefined`, `null`.

**Reference Data Types**: `Object`, `Array`, `Function`, `Date`, `RegExp`.

