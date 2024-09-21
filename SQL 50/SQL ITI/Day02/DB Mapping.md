> Database mapping refers to the process of defining how data is structured, stored, and accessed within a database system. This process involves creating a blueprint for how data entities (like tables, fields, and relationships) in a database are linked to each other and how they correspond to objects or classes in an application.


![[Pasted image 20240713191334.png]]

### ER-to-Relational Mapping
*Step 1:* [[#Mapping of Regular Entity Types]] --> Strong Entity
*Step 2:* [[#Mapping of Weak Entity Types]]
*Step 3:* [[#Mapping of Binary 1:1 Relation Types]]
*Step 4:* [[#Mapping of Binary 1:N Relationship Types]]
*Step 5:* [[#Mapping of Binary M:N Relationship Types]]
*Step 6:* [[#Mapping of N-ary Relationship Types]]
*Step 7:* [[#Mapping of Unary Relationship]]

***Note***
> If i have a relationship with a *Cardinality 1:1*  and *Total participation from both side* I **MUST start Mapping it first** --> It's ***Mandatory*** 


#### Mapping of Regular Entity Types
> -  Create table for each entity type -> if there is no 1-1 relationship mandatory from 2 sides 
> - Choose one of key attributes to be the primary key.



![[Pasted image 20240713225555.png]]

![[Pasted image 20240713225607.png]]


![[Pasted image 20240713230248.png]]

***Note1***
> *Derived Attribute* --> we usually didn't store it on Database *WHY* ? 
> - It causes a headache for database
> - Because it based on a calculation so this delays retrieval and slow down performance

***Note2***
> Mapping Complex Like Mapping Multivalued attribute then including parts of the multivalued attributes as columns in DB

#### Mapping of Weak Entity Types

*Step 1* --> Create table for each weak entity
*Step 2* --> Add *Foreign key* that correspond to the owner entity type .
*Step 3* --> *Primary Key* composed of :-  
- Partial identifier of weak entity
- Primary key of identifying relation (Strong entity)


![[Pasted image 20240714003118.png]]


#### Mapping of Binary 1:1 Relation Types

- Merged  two tables if both sides are Mandatory. 

- Add FK into  table with the total participation relationship  to represent optional side.

- Create third table if both sides are optional.

![[Pasted image 20240714163910.png]]


![[Pasted image 20240714164044.png]]


![[Pasted image 20240714184705.png]]


#### Mapping of Binary 1:N Relationship Types

- *Add FK to N-side table* if N-Side mandatory

- Add  any simple attributes of relationship as column to N-side table. 

![[Pasted image 20240714185521.png]]

![[Pasted image 20240714185553.png]]

#### Mapping of Binary M:N Relationship Types

- Create a new third  table
- Add FKs to the new table for both parent tables
- Add simple attributes of relationship to the new table if any .
![[Pasted image 20240714190017.png]]


***Note***
> the attribute that are in the relationship always follow foreign key
> ![[Pasted image 20240714190600.png]]



#### Mapping of N-ary Relationship Types

- If n > 2 then :
- on this mapping *we didn't care about Cardinality Or Participation of relationship *
- Create a new third  table
- Add FKs to the new table for all parent tables
- Add simple attributes of relationship to the new table if any .
![[Pasted image 20240714191450.png]]

![[Pasted image 20240714191509.png]]


#### Mapping of Unary Relationship
![[Pasted image 20240714193037.png]]