
### Entity-Relationship Diagram  ( ERD ) 

- Identifies information required by the business by display the relevant entities and the relationships between them


## ER Model

### Basic Constructs of the ER Model

 1. **Entities**  --> person, place, object , event , concept ( often corresponds to a real time object that is ***distinguishable*** from any other object)
	 1. ***Entity*** ==> Is a thing (an Object) in the real world with an independence existence , physical existence or conceptual existence 
	 
 2. **Attributes** --> property or ***Characteristic*** of an entity type (often corresponds to a field in a table)
 3. **[[#Relationships]]** --> Link between entities (corresponds to ***primary key - foreign key*** equivalencies in related tables)


### ER Diagram

![[Pasted image 20240602123631.png]]



### Strong Entity Vs Weak Entity

- **Strong Entity**
	- An entity set that has a primary key
	- An entity has a unique identifier 
- **Weak Entity**
	- An entity set that do not have a sufficient attributes to form a primary key 
	- It is an entity whose existence is dependent on another entity
	
>  ***Partial key*** --> A set of attributes that can be associated with P.K of an owner entity set to distinguish a weak entity 


![[Pasted image 20240602132954.png]]


### Type of Attributes

 - [[#Simple Attribute]] 
 - [[#Composite Attribute]]
 - [[#Multi-Valued Attribute]]
 - [[#Derived Attribute]]
 - [[#Complex Attribute]]
 



#### Simple Attribute

- refers to an attribute that cannot be further divided into smaller sub-parts

- smallest semantic unit of data, atomic (no internal structure)-singular e.g. city
-![[Pasted image 20240603095015.png]]

#### Composite Attribute

- can be divided into smaller sub-parts
- group of attributes e.g. address (street, city, state, zip)
![[Pasted image 20240603095105.png]]



## Multi-Valued Attribute
- multiple values e.g. phone numbers.

![[Pasted image 20240603095456.png]]

#### Derived Attribute
- Can be calculated from another attribute or entity 
![[Pasted image 20240603095319.png]]


#### Complex Attribute 
- an attribute that is a combination of multiple other attributes. 
- It can include both composite and multi-valued attributes
![[Pasted image 20240603100412.png]]



## Relationships

==> A Relationship is a connection between entity classes
==> Relationships Always expressed as a ***VERB***
==> Relation has three properties :
- [[#Degree of Relationships]]
- [[#Cardinality Constraint]]
- [[#Participation Constraint]]


#### Degree of Relationships.

**Degree** --> Number of entity type that participate in a relationship 

**Three Cases :**
- ***Unary*** / ***Recursive Relationships***--> Between two instances of one entity 
- ***Binary*** --> Between the instances of two entity types
- ***Ternary*** --> Among the instances of three entity types

![[Pasted image 20240603102120.png]]


#### Cardinality Constraint

==> Represents the ***Maximum*** number of relationships
==> (**One-One Relationship**) (**One-Many Relationship**) (**Many-Many Relationship**)

![[Pasted image 20240603104737.png]]


#### Participation Constraint

==> Represents the ***Minimum*** number of relationships that can occur with this instances
==> Can be represented using **MUST** or **MAY**
###### Types of Participation Constraints

- **Total Participation (Mandatory Participation)**: Every instance of an entity ***Must***participate in at least one instance of the relationship. This means that for every entity instance, there is a corresponding relationship instance. In ER diagrams, total participation is usually represented by a double line connecting the entity to the relationship.

- **Partial Participation (Optional Participation)**: Some instances of an entity ***May*** participate in the relationship, but it is not mandatory for all instances. This means that an entity can exist without being part of the relationship. In ER diagrams, partial participation is typically represented by a single line connecting the entity to the relationship.

![[Pasted image 20240603105329.png]]

![[Pasted image 20240603105539.png]]




## Keys
##### Different types of keys:
 - **Candidate Key** 
	 - when multiple possible identifiers exist, each is a candidate key.
	 - Potential unique identifiers.
 - **Primary Key**
	 - the primary key is a specific candidate key chosen by the database designer to uniquely identify tuples in a table. Each table can have only one primary key.
	 - Chosen unique identifier.
 - **Foreign Key**
	 - A foreign key is an attribute or set of attributes in one table that refers to the primary key in another table, creating a relationship between the two tables.
	 - Links tables together.
 - **Composite Key** 
	 - a key that consists of two or more attributes that together uniquely identify a tuple in a table.
	 - Combined attributes for unique identification
 - **Partial Key**
	 - A partial key, also known as a surrogate key or a weak key, is an attribute in a weak entity set that, in combination with the primary key of its owning entity set, uniquely identifies a tuple.
	 - Weak entity's identifier combined with owner's key.
 - **Alternative Key**
	 - An alternative key is any candidate key that is not chosen to be the primary key. It's an alternative way to uniquely identify tuples in the table.
	 - Non-primary candidate key
 - **Super Key**
	 - A super key is a set of one or more attributes that, taken collectively, can uniquely identify a tuple in a table. A super key may contain additional attributes that are not necessary for unique identification.
	 - Set of attributes that uniquely identifies a tuple, possibly with extra attributes.

