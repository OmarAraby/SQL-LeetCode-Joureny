> - A database design technique that *reduces redundancy and ensures data dependencies* are logical. Forms include 1NF, 2NF, 3NF, etc., each removing different types of redundancy.


>-  The process of structuring data to *minimize duplication and inconsistencies*(التناقضات). 
>- The process usually involves breaking down a *single* Table into *two or more tables* and defining relationships between those tables. 
>- The process of decomposing(تحليل) unsatisfactory "bad" relations by breaking up their attributes into smaller relations

> [!NOTE]
> >  ==> We can use Normalization as another method for creating a Database Design (Schema)
> > 


### Avoid *** DML Anomalies***
- ***Insertion Anomaly*** –> adding new rows forces user to create duplicate data
- ***Deletion Anomaly*** –> deleting rows may cause a loss of data that would be needed for other future rows
- ***Modification Anomaly*** –> changing data in a row forces changes to other rows because of duplication

==> " *a table should not have more than one entity type* "


------------------------------------------
### Function Dependency 
Before go deep in Normalization We want to know **What is the Function dependency ?** 
- ==> *A constraint between two attributes (columns) or two  sets of columns at the **SAME Table** *
- A --> B : The value of A *uniquely determines* the value of B **WHICH MEANS** existing of B depending on a value of A
``` 
A ---> B
SSN ---> NAme
Eid ---> Address , age 
---------------------------
A ---> B
PK ---> name , Age , address, job
---------------------------------
H,M ---> Z
SSN,Projectno ---> hours
StdID,CourseID ---> Grades
```

#### Type of Function Dependency 
- **Full Functional Dependency**
	- Attribute is fully Functional Dependency on a *PK* if its value is determined by the *whole PK*
- **Partial Functional Dependency**
	- Attribute if has a Partially Functional Dependency on a *PK* if its value is determined by *part of the PK(Composite Key)*
- **Transitive Functional Dependency**
	- Attribute is Transitively Functional Dependency on a table if its value is determined by anther *non-key attribute* which it self determined by PK 
![[Pasted image 20240906002541.png]]
![[Pasted image 20240906002641.png]]


### Normalization Steps
![[Pasted image 20240906003533.png]]


##### First Normal Form (1NF)
- When we call Normal Form Is a **1NF** ?
	- It **MUST NOT  Have** 
		- Multi-valued Attributes
		- Repeating Group
		- Composite Attribute 

##### Second Normal Form (2NF)
- When we can applied it ?
	- when it achieve (*1NF*) --> 1NF should satisfy 
	- shouldn't have a *Partial Dependency*
		- means there is no *non-key attribute* depend on a part of the key (*Composite Key* )

##### Third Normal Form (3NF)
- When we can applied it ?
	- when it achieve (*2NF*) --> 2NF should satisfy
	- shouldn't have a *Transitive Dependency*
		- means there is non-key attribute depend on a non-key attribute which depend on the key (*PK*)

### Example of applied Normal Forms
##### Example 1

![[Pasted image 20240906153007.png]]
![[Pasted image 20240906153014.png]]
![[Pasted image 20240906165515.png]]
![[Pasted image 20240906165647.png]]
![[Pasted image 20240906165831.png]]![[Pasted image 20240906170009.png]]
![[Pasted image 20240906170057.png]]
##### Example 2
![[Pasted image 20240906170318.png]]
###### 1NF --> Separate Repeating Groups into new tables
==Platform== ( **pfName** , pfDesc , pfManager)
==Students== ( **pfName , appno** , name , faculty , F-Code , grade , attd , startDate)
==Std_Tel== (**appno,telno**)

###### 2NF --> Separate Partial Dependency into new tables
==Students==: (**appno**, name , faculty , FCode, address)
==Students_pf==: ( **pfname,appno**, grade, attd , start_date )

***Unchanged Tables***
==Platform== :( **pfname** , pfdesc , pfManager )
==Std_Tel==: ( **appno, telno** )

###### 3NF --> Separate Transitive Dependency into new tables
==Students==: (**appno**, name , *FCode*, address)
==Fac_majors==:(faculty , **FCode**)

***Unchanged Tables***
==Platform== :(**pfname** , pfdesc , pfManager)
==Std_Tel==: (**appno, telno**)
==Students_pf==: (**pfname,appno**, grade, attd , start_date)

##### Example 3
> *Employee*  (Eid , Ename , Eadd, Pro_id , Pro_Name, PLoc_id , PLoc_city, hours, bonus)
> 
###### 1NF --> Separate Repeating Groups into new tables
==Employee== (**Eid** , Ename , Eadd)
==Emp_Pro== (**Eid , Pro_id**, Pro_name , PLoc_id, PLoc_city , hours , bonus)
###### 2NF --> Separate Partial Dependency into new tables
==Employee== (**Eid** , Ename , Eadd)
==Project== (**Pro_id** , Pro_name , PLoc_id , PLoc_city)
==Emp_Pro== (**Eid , Pro_id**, hours , bonus)
###### 3NF --> Separate Transitive Dependency into new tables
==Employee== (**Eid** , Ename , Eadd)
==Project== (**Pro_id** , Pro_name , *PLoc_id* )
==Emp_Pro== (**Eid , Pro_id**, hours , bonus)
==Cities== (**PLoc_id**, PLoc_city)