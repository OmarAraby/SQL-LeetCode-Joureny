## Database defined

*A database is an organized collection of structured information*, or data, typically stored electronically in a computer system. A database is usually controlled by a [database management system (DBMS)](https://www.oracle.com/ca-en/database/what-is-database/#WhatIsDBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.

## Types of databases

There are many different types of databases. The best database for a specific organization depends on how the organization intends to use the data.

#### Relational databases

- [Relational databases](https://www.oracle.com/ca-en/database/what-is-a-relational-database/) became dominant in the 1980s. *Items in a relational database are organized as a set of tables with columns and rows*. Relational database technology provides  *the most efficient and flexible way to access* **structured information**.
- An [RDBMS](https://www.quest.com/learn/what-is-a-relational-database.aspx) organizes the structured data into tables. A table consists of rows and columns.
- Each table has a pre-defined schema with columns and their data types
#### Object-oriented databases

- Information in an object-oriented database is represented in the form of *objects based on classes* , as in object-oriented programming.
- It stores data in the form of objects based on classes.
- It is suitable for handling complex data structures.
- It allows for the creation of classes and inheritance
- Examples include ObjectDB and db4o.
#### Distributed databases

- A distributed database consists of two or more files located in different sites. The database may be stored on multiple computers, located in the same physical location, or scattered over different networks.

#### Data warehouses

- A central repository for data, a data warehouse is a type of database specifically designed for *fast query and analysis*.

#### NoSQL databases

- A NoSQL, or nonrelational database, allows unstructured and semistructured data to be stored and manipulated (in contrast to a relational database, which defines how all data inserted into the database must be composed). NoSQL databases grew popular as web applications became more common and more complex.

#### Graph databases
- A graph database stores data in terms of *entities* and *the relationships between entities*
- **OLTP databases.** An OLTP database is a speedy, analytic database designed for large numbers of transactions performed by multiple users.



---------------------------------------------------------
These are only a few of the several dozen types of databases in use today. Other, less common databases are tailored to very specific scientific, financial, or other functions. In addition to the different database types, changes in technology development approaches and dramatic advances such as the cloud and automation are propelling databases in entirely new directions. Some of the latest databases include

#### Open source databases

- An open source database system is one whose source code is open source; such databases could be SQL or NoSQL databases.

#### Cloud databases

- A [cloud database](https://www.oracle.com/ca-en/database/what-is-a-cloud-database/) is a collection of data, either structured or unstructured, that resides on a private, public, or hybrid cloud computing platform. There are two types of cloud database models: traditional and database as a service (DBaaS). With DBaaS, administrative tasks and maintenance are performed by a service provider.

#### Multimodel database

- Multimodel databases combine different types of database models into a single, integrated back end. This means they can accommodate various data types.

#### Document/JSON database

- Designed for storing, retrieving, and managing document-oriented information, [document databases](https://www.oracle.com/ca-en/autonomous-database/autonomous-json-database/) are a modern way to store data in JSON format rather than rows and columns.

#### Self-driving databases

- The newest and most groundbreaking type of database, self-driving databases (also known as autonomous databases) are cloud-based and use machine learning to automate database tuning, security, backups, updates, and other routine management tasks traditionally performed by database administrators.


## What is database software?

Database software is used to create, edit, and maintain database files and records, enabling easier file and record creation, data entry, data editing, updating, and reporting. The software also handles data storage, backup and reporting, multi-access control, and security. Strong database security is especially important today, as data theft becomes more frequent. Database software is sometimes also referred to as a “database management system” (DBMS).
## What is a database management system (DBMS)?

A database typically requires a comprehensive database software program known as a database management system (DBMS). A *DBMS serves as an interface between the database and its end users or programs, allowing users to retrieve, update, and manage how the information is organized and optimized*. A DBMS also *facilitates oversight and control of databases, enabling a variety of administrative operations such as performance monitoring, tuning, and backup and recovery*.

Some examples of popular database software or DBMSs include MySQL, Microsoft Access, Microsoft SQL Server, FileMaker Pro, Oracle Database, and dBASE.


## What are the key features of a database management system?

A few key features of a DBMS are as follows:

- **Data storage**: Data can be structured, unstructured, or semi-structured. A DBMS should be able to organize and manage data.
- **Data retrieval and manipulation**: A DBMS allows users to query data with specific query languages such as SQL, PL\SQL, and KQL. Users can run commands such as inserts, updates, and deletes to perform database activities.
- **Data integrity and concurrency control**: A DBMS includes mechanisms to ensure data is accurate and consistent, and multiple users can work on the data without affecting its consistencies or conflicts.
- **Security**: A DBMS supports user authentication, authorization, and encryption mechanisms to ensure data is safe and secure while data is at rest or motion.
- **Backup and recovery**: A DBMS supports database backup and restoration mechanisms to safeguard against data loss or corruption. It should allow data recovery quickly, securely, and safely.
- **Consistency**: A DBMS ensures data is accurate, consistent, and anomalies-free. Any transaction should be a complete success or failure, not a partial failure or success.
- **Indexing**: A DBMS supports various indexing mechanisms for faster data retrieval and query performance tuning.