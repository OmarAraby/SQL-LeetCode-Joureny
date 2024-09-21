A class is a **blueprint** ( *Standard Or Template* ) of an object. You can think of a class as a concept, and the object is the **embodiment** of that concept. You need to have a class before you can create an object.
> - A blueprint or template for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
> ![[Pasted image 20240917032705.png]]


##### Visibility in class 
- All member are private by default 
- **Public** : its access is available from anywhere inside or outside class
- **Private** : the access Availability within the class *only*  
- Make the attributes members private. **(90%)**
- Make the functions member Public. **(70%)**
![[Pasted image 20240917043743.png]]


##### Default Arguments in Function Calls ^default-args
![[Pasted image 20240917044049.png]]
![[Pasted image 20240917044208.png]]
![[Pasted image 20240917044244.png]] 
![[Pasted image 20240917044527.png]]
***Examples***
```cpp
int sum (int x = 0, int y)  // this wrong way to set default arguments
```

```cpp
// the compiler will refuse it because two function equal in signature 
// params with default value didn't count in function signature
int sum (int x, int y  = 0) 
int sum (int x)

```

##### `this` pointer 
- `this` *pointer to the current object that call function*
- It refers to the object that is executing the current code.
![[Pasted image 20240917080046.png]]


##### Static Members
> ![[Pasted image 20240918021433.png]]
> **Static Attributes**
> 	- we can consider it as global variable but for object of my Class
> 	![[Pasted image 20240918021841.png]]
> **Static Methods** ==> Function
> 
>  ==Only Deal with Static attributes==
> 	
> 	- ![[Pasted image 20240918022303.png]]


##### Friend Function 
![[Pasted image 20240918022914.png]]