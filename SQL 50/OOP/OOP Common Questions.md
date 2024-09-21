#####  what is OOP concepts?
  
- ***Encapsulation***:
	- **Definition**: Encapsulation is about putting data (like attributes) and functions that work on the data into one unit (class) and controlling access to some parts of it.
	    
	- **Main Purpose**: It protects the data by limiting direct access and ensures that the data is only changed through specific functions.
	    
	- **Example**: A `BankAccount` class with a private `balance` attribute and public methods like `deposit()` and `withdraw()` to manage the balance.
- ***Abstraction***:

	- **Definition**: Abstraction means hiding the complex details of how something works and showing only the important parts. It gives a simple way to interact with the object.
	    
	- **Main Purpose**: It makes working with complicated systems easier by focusing on what’s important, rather than how it works behind the scenes.
	    
	- **Example**: A `Vehicle` class with methods like `start()` and `stop()`, which are used differently by subclasses like `Car` and `Motorcycle`.

- ***Inheritance***:

	- **Definition**: Inheritance allows a new class (child class) to take on the attributes and methods of an existing class (parent class). It creates a relationship between classes.
	    
	- **Main Purpose**: It helps to reuse code and create new classes based on existing ones, making it easier to organize and reduce repeated code.
	    
	- **Example**: A `Dog` class that inherits from an `Animal` class, meaning the `Dog` class gets all the properties and methods of the `Animal` class.
    

- ***Polymorphism***:

	- **Definition**: ability of a single function, method, or object to behave in different ways depending on the situation.
	    
	- **Main Purpose**: It increases flexibility by allowing one function to work with objects of different types, making it easier to handle different objects.
	    
	- **Example**: A `makeSound()` method in a `Cat` class that returns "Meow" and in a `Dog` class that returns "Bark". The behavior changes based on the type of object.
	    

##### what is constructor ?
  
> A **constructor** is a special method in a class that called automatically during object of the class is created.

  
##### Copy Constructor
> A copy constructor is a *special constructor* that *creates a new object by copying the contents of an existing object of the same class*.

##### Can a constructor be private?
>**Yes**, a constructor can be private. This is often used in design patterns like Singleton, where you want to control object creation.

##### Can a constructor be static ?
>**No**, a constructor cannot be static. Constructors are used to create and initialize object instances, which is inherently non-static behavior. 
> -بيشتغل علي مستوي Object level مش Class level .
>


##### Difference between interface and abstract class:
- **Interfaces**
	- هي عبارة عن اتفاقية ما بين مبرمجه وما بين المبرمج اللي هيستخدم الInterface والاتفاقية بتقول انه لو عاوز يستخدم الـ Functionsاللي في الـ Interface لازم يكتب بأيديه الكود بتاع الـ Functionsدي.
	- only contain *method declarations* (*method signatures*). (no implementation)
	- All methods in an interface are *implicitly public and abstract*
	- A class can implement multiple interfaces
	- الدوال في interface مجردة كليًا abstract Full  لا تحوي أي implementation أي أنها ال تقوم بتنفيذ شيء حتى يرثها  الابن* ويقوم بعمل override.*
-  **Abstract classes**
	- can have both abstract (unimplemented) and concrete (implemented) methods.
	- can only inherit from one abstract class.
	- في حين class abstract يمكن أن يحتوي على دوال تقوم بتنفيذ سلوك افتراضي ثم يأتي الابن إما أن ينفذ هذا السلوك نفسه أو سلوك آخر ايضا بعمليه override.

##### What is an abstract method ?
> An abstract method is a **method declared in an abstract class without an implementation**. Subclasses must provide an implementation for this method.

##### What is the diamond problem and its solution? 
>The diamond problem occurs in multiple inheritance when a class inherits from two classes that have a common ancestor. This can lead to ambiguity. In languages like C++, it's solved using *virtual inheritance*. Java avoids this by not allowing multiple inheritance of classes, only *interfaces*.


##### Pass by value **vs** pass by reference.
- **Pass by Value**: 
	- A copy of the actual value is passed to the function.
	- Changes made to the parameter inside the function do not affect the original
		value.
- **Pass by Reference**: 
	- A reference (or pointer) to the actual value is passed to the function. Changes made to the parameter inside the function affect the original value.
###### Difference between reference types and value types
 - **Value Types**
	 - **Stored directly in memory**: The actual data is stored in the memory location.
	 - **Copied on assignment**: When you assign a value type to another variable, a copy of the value is made.
- **Reference Types**
	- **Stored by reference**: The variable holds a reference (or pointer) to the actual memory location where the data is stored.
	- **Not copied on assignment**: When a reference type is assigned to another variable, both variables point to the same memory location. Modifying one will affect the other.

###### Summary:

- **Value Types** store the actual data and create copies when assigned.
- **Reference Types** store references to the data, and multiple variables can point to the same memory location, sharing the same data.


##### The destructor doesn't have overloads.?
> this correct because it **doesn't take parameters**



##### Shallow Copy vs Deep Copy:
 **Shallow Copy**

- A **shallow copy** of an object copies the reference structure of the object, not the actual data it points to.
- If the original object contains references to other objects (like arrays or objects), the shallow copy will contain references to the same objects. This means *changes to the referenced objects will affect both the original and the copied objects*.

**Deep Copy**

- A **deep copy** creates an entirely independent copy of an object and all the objects referenced by it. In other words, it recursively copies all objects it refers to, ensuring that no references to the original object remain.
- *Changes made to the deep copy will not affect the original object in any way*.

**Key Differences**:

| Aspect                | Shallow Copy                                                    | Deep Copy                                             |
| --------------------- | --------------------------------------------------------------- | ----------------------------------------------------- |
| **Copying Behavior**  | Copies only the top-level structure; nested objects are shared  | Copies the entire structure, including nested objects |
| **Shared References** | Yes, nested objects are shared                                  | No, all objects are fully copied                      |
| **Performance**       | Faster and uses less memory                                     | Slower and uses more memory                           |
| **Side Effects**      | Changes in nested objects affect both the original and the copy | Changes in the copy do not affect the original        |
| **Use Case**          | When only the top-level object needs to be modified             | When a completely independent copy is needed          |




##### Struct vs Class :

 **Key Differences**:
 - Default Access Specifier:
    - *Struct*: Public by default
    - *Class*: Private by default

| Aspect          | Struct                             | Class                               |
| --------------- | ---------------------------------- | ----------------------------------- |
| **Type**        | Value type                         | Reference type                      |
| **Memory**      | Stored in the stack                | Stored in the heap                  |
| **Copying**     | Copied by value (new copy)         | Copied by reference (same instance) |
| **Inheritance** | Does not support inheritance       | Supports inheritance                |
| **Performance** | Faster for small, simple data      | Slower due to heap allocation       |
| **Use Case**    | Small, lightweight data structures | Complex, larger data structures     |
![[Pasted image 20240920065520.png]]

##### Difference Between **Array** and **Class**
- **Array**: A simple data structure to store and access a collection of elements by index.
- **Class**: A template for creating objects, encapsulating both data (attributes) and functionality (methods).

| **Aspect**            | **Array**                                                                      | **Class**                                                                                              |
| --------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **Definition**        | A collection of elements of the same type stored in a contiguous memory block. | A blueprint for creating objects, containing attributes (data) and methods (functions).                |
| **Purpose**           | Primarily used to store multiple values of the same type, accessed via index.  | Used to represent entities with properties and behavior, encapsulating data and operations.            |
| **Type**              | A data structure.                                                              | A user-defined data type or a blueprint for objects.                                                   |
| **Data Storage**      | Stores only values (primitive or object references) in sequential order.       | Can store both data (attributes) and methods (functions) that operate on the data.                     |
| **Memory Allocation** | Fixed size (in most languages, though some support dynamic arrays).            | Memory allocated as needed for objects created from the class.                                         |
| **Operations**        | Operations on arrays are typically accessing or modifying elements by index.   | Operations include defining methods, creating objects, and modifying object attributes.                |
| **Access**            | Access elements by index (e.g., `array[0]`).                                   | Access object properties or methods using dot notation (e.g., `object.method()` or `object.property`). |
| **Example**           | `int[] numbers = {1, 2, 3};`                                                   | `class Car { string brand; void drive() {...} };`                                                      |
| **Use Case**          | Use when you need to store and manage a collection of values of the same type. | Use when you need to model complex entities with attributes and behaviors.                             |

---
##### Virtual Function  vs Pure Virtual Function
- **Virtual Function**
	 - A function declared with 'virtual' keyword in base class, *allowing derived classes to override it. Enables polymorphism through late binding.*
	 - Function in base class can be overriden in derived class ,enabling runtime polymorphism

 - **Pure Virtual Function (Abstract Function)**

	 - A **pure virtual function** is a virtual function that **does not have any implementation** in the base class. It is specified by assigning `0` to the virtual function in the base class. This makes the base class an **abstract class**, which means it **cannot be instantiated**, and any derived class must override the pure virtual function.

##### Linked List

A **linked list** is a **data structure** made up of a series of nodes, where each node contains two parts:

1. **Data**: The value or information the node holds.
2. **Pointer**: A reference (or pointer) to the next node in the sequence.

###### Types of Linked Lists:

1. **Singly Linked List**: Each node points to the next node.
2. **Doubly Linked List**: Each node points to both the previous and the next node.
3. **Circular Linked List**: The last node points back to the first node, forming a loop.
##### Pointer

> A **pointer** is a variable that holds the **memory address** of another variable. Pointers are widely used in languages like C and C++ for direct memory access, dynamic memory management, and efficient data manipulation.



##### Static vs Const
 ***Static***:
- **Static** members belong to the class itself rather than to any specific object. This means all objects of the class share the same static variable or method.
- Static methods can only access other static members (methods or variables).
- **Key Points about `static`:**
	- A static variable retains its value across all instances of the class.
	- Static methods and variables are accessed via the class name, not the object.


***Const***:
- **Const** means that a value cannot be changed after it's initialized. It can apply to variables, pointers, member functions, or parameters.
- **Key Points about `const`:**
	- A `const` variable or pointer means its value cannot change after initialization.
	- A `const` method guarantees that no member variables of the class will be modified.