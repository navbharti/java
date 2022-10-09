# Class and Objects :

```java
class Rectangle{
    //member variables

    //member methods
}
```

## 1. Declaring objects
```java
//declaring a reference
Rectangle r1;

//creating an object
r1 = new Rectangle();
```
## 2. Assigning object reference variables
```java
Rectangle r2 = r1;
```
## 3. Variables in Java

### 3.1 Static Variables or Class Variables
```java
class Rectangle{
    //static variable
    static double length;
    static double breadth;

    //member methods
}
```
### 3.2 Instance Variables or Non-Static Variables
```java
class Rectangle{
    //instance variable
    double length;
    double breadth;

    //member methods
}
```
### 3.3 Local Variables
```java
class Rectangle{
    //member variables
    //1. static variable
    static double length;
    static double breadth;

    //member methods
    void doSomething(){
        //local variable
        int a;
    }
}
```

## 4. Methods in Java

```java 
modifier static returnType nameOfMethod (parameter1, parameter2, ...) {
  // method body
}
```
A block of code that performs a specific task.

Dividing a complex problem into smaller chunks makes your program easy to understand and reusable.

Methods has return-Type, method-Name and method-Body.

Method can be declared

Method can be defined

Method can be called

Method can have zero or more parameters

Parameters vs Arguments (Acutual Arguments vs Formal Arguments)

Method modifier can be (`default`, `public`, `private`, `protected`)

### 4.1 Static Methods or Class Methods
```java
class Rectangle{
    //member variables

    //static methods
    static void fun1(){
        //method-body
    }
}
```

A static method belongs to a class.

A static method can be called without the instance or object of that class.


Non-static methods can access any static method and static variable, without creating an instance or object of the class.

A static method can only access static data members and static methods but cannot access non-static methods and variables.

Static vs Non-Static methods are differntiated on the basis of the following:

* Accessing members and methods
* Calling process
* Binding process
* Overriding process
* Memory allocation


### 4.2 Instance Methods or Non-Static Methods
```java
class Rectangle{
    //member variables

    //intance methods
    void fun2(){
        //method-body
    }
}
```
## 5. Constructors

```java
class Rectangle{
    //member variables
     double length;
     double breadth;

     //constructor
     Rectangle()
     {
        this.length = 1.0;
        this.breadth = 1.0;
     }

    //member methods
}
```
Special type of instance method.

Does not have a return type (not even void also).

Constructor name is exactly same as the its Class name.

Constructor is called whenever an object is created.

Used to do the initial operations (variable initialization or etc) before an object is created.

Constructor can be user defined or provided bey JVM (Java Virtual Machine).

As soon as used defined zero-parameter user defined constructor, the concept of default constructor does not exist anymore.

A constructor cannot be `abstract` or `static` or `final`.

A constructor can be `overloaded` but can not be `overridden`.
### 5.1 Default Constructors
When Constructor is not defined in the class definition it is JVM responsibility to provide a constructor that is also called Default Constructor.

Default constructor is alway zero-parameter constructor and empty body.

But zero-parameter constructor may not be empty body.

```java
class Rectangle{
    //default constructor looks like zero-parameter construcor.
    Rectangle(){ }
}
```

### The Default Constructor initializes with default values

|Type	|Default Value|
|-------|-------------|
|`boolean`|	`false`|
|`byte`	|`0`|
|`short`|	`0`|
|`int`|	`0`|
|`long`|	`0L`|
|`char`	|`\u0000`|
|`float`	|`0.0f`|
|`double`|	`0.0d`|
|`object`|	Reference `null`|
### 5.2 Zero-Parameter Constructor
The consctructor which does not take any parameters is called zeor-parameterized constructor. 
```java
class Rectangle{
    double length;
    double breadth;
    //zero-parameter construcor.
    Rectangle(){
        length = 1.0;
        breadth = 1.0;
     }
}
```
### 5.3 Parameterized Constructor
The consctructor which takes one or more parameters is called parameterized constructor. 
```java
class Rectangle{
    double length;
    double breadth;
    //parameterized construcor.
    Rectangle(double l, double b){
        length = l;
        breadth = b;
     }
}
```

```java
class Rectangle{
    double length;
    double breadth;
    //parameterized construcor.
    Rectangle(double length, double breadth){
        this.length = length;
        this.breadth = breadth;
     }
}
```
### 5.4 Copy Constructor
A constructor that creates an object using another object of the same Java class.

Helpful when we want to copy a complex object that has several fields, or when we want to make a deep copy of an existing object.

```java
class Rectangle{
    double length;
    double breadth;

    //copy constructor
    Rectangle(Rectangle r){
        this.length = r.length;
        this.breadth = r.breadth;
    }
}
```
## 6. Recursive Methods
Methods called itself is recursive method.

calling method vs called method

method call Stack in memory

Almost all iterative work can be converted to recursive methods. 