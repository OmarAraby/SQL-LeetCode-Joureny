
![[Pasted image 20240602113858.png]]


**Tables & Relationship**

| Sid | Sname |
| :-: | ----- |
|  1  | Ahmed |
|  2  | Ali   |
|  3  | Omar  |

| Did | Dname |
| --- | ----- |
| 10  | CS    |
| 20  | IT    |
| 30  | IS    |




Advantage of DB System
	1. One Standard
	2.  [Metadata](#metadata) + Data --> (Actual Value in table)
	3. Column --> Data type
	4. Primary Key-->Unique -- Not NULL 
	5. Centralized DB
	6. 

##### Metadata
- Metadata is data that provides information about other data. It helps to organize, find, and understand data by providing context and details about the data's characteristics
- Description in [[ERD]]  --> Objects in the system 


# Basic Definitions 

***Database*** --> A collection of related data .

***Database Management System(DBMS)*** --> A software package / system to facilitate the creation and maintenance of a computerized database .


***Database System*** --> The DBMS software together with the data itself.
sometimes, the applications are also included. (Software+Database)




### DBMS Advantage

- **Standardization** and better data accessibility and response (SQL)
-  **Sharing Data**
	- Different users get different views of data
- **Enforcing Integrity** --> Constraints
- **Improved Data quality**
	- Constraints, data validation rules
- **Inconsistency** can be avoided because of data sharing
- Providing Backup and Recovery
- Restricting Unauthorized Access
- Minimal Data Redundancy
	- Leads to increased data integrity / Consistency  
- **Program-Data Independence**
	- Metadata stored in DBMS --> So applications don't worry about data formats
	- Data quires/updates managed by DBMS

### DBMS Disadvantages

- Needs **Expertise** to use
- DBMS itself is **Expensive**
- The DBMS may be **Incompatible** with any other available **DBMS**



