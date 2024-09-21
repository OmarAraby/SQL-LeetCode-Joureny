 
## Types of Joins :

### Cross Join
==> **Cartesian Product**
	 
```sql
-- the result will be cartesian product
Select Sname , Dname 
From Student, Dept;

```
```sql
 -- the result will be cartesian product 

Select Sname , Dname
From Student Cross Join Dept;
```

![[Pasted image 20240821063230.png]]



### Inner Join
==> **Equi Join** ==> *PK = FK*
- will get the Matched records --> Intersection 
```sql
Select Sname , Dname 
From Student , Dept
Where Dept.did = Student.Did ; -- in case two table have the same name -> equijoin
```
```sql
Select Sname , Dname 
from student S Inner join Dept D
on D.Did = S.did;
```
![[Pasted image 20240821065548.png]]

### Outer Join 
>  Display match records and mismatch  records will also display but with *null value*
#### Left Outer Join
--> will return all data from the table on left side and the matched records/rows from the right table.
 ```sql
	Select Sname, Dname
	From Student S left outer join Dept D
	on D.did = S.Did
```
    
![[Pasted image 20240821071129.png]]

#### Right Outer Join  
-->  will return all data from the table on Right side and the matched records/rows from the left table.

```sql
Select Sname, Dname
From Student S right outer join Dept D
on D.did = S.Did
```
![[Pasted image 20240821071559.png]]

#### Full Outer Join 
--> Mixed between *Inner , Left , Right* joins
--> Retrieves all the records where there is a match in either the left or right table.

```sql
Select Sname, Dname
From Student S full outer join Dept D
on D.did = S.Did
```
![[Pasted image 20240821072426.png]]



### Self Join
==> ***Unary relationship***
> To join table with itself we *Must have a Recursive Relationship*
```sql
Select X.Ename as EmpName , Y.Ename as SuperName
From Employee X , Employee Y 
Where Y.eid = X.superid
```
-> **Note** =>  ==We give FK to the table that i have on my database==

![[Pasted image 20240821080444.png]]

-> **Note** => ==In Self join the table that have FK is the table that i have on my database==

***We can write it with Inner Join***
```sql
Select X.Ename as EmpName , Y.Ename as SuperName
From Employee X inner join Employee Y 
on Y.eid = X.superid
```




#### Note 
> ==the number of join conditions is less than the number of table by 1==