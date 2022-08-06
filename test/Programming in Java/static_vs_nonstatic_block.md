# Understading Static Block and Non-Static Block

## Static Block
1. Static block executes at class loading time.
2. Static keyword is prefixed before the start of the block.

```java
public class StaticDemo
{
    static 
    {
        //here goes the static block statements
    }

    public static void main(String[] args) 
    {
        //main block
    }

}

```

3. All static variables can be accessed freely. 
```java
public class StaticDemo
{
    static int a=10;
    static int b;
    static {
        System.out.println("Value of a: "+ a);
        System.out.println("Value of b: "+ b);
        b = 300;
        System.out.println("Value of b: "+ b);
    }

    public static void main(String[] args) 
    {
        //main block
        System.out.println("This is main method block");
    }
}

```

```console
-----Ouput-----
Value of a: 10
Value of b: 100
Value of b: 300
This is main method block

```
4.  Non-static or instance variable can only be accessed through object reference, that also only after object creation.

```java
public class StaticDemo
{
    static int a=10;
    static int b;
    int c = 10;
    int d = 100;
    static {
        System.out.println("Value of a: "+ a);
        StaticDemo sd = new StaticDemo();
        System.out.println("sd.c: "+ sd.c);
        System.out.println("sd.d: "+ sd.d);
        
    }

    public static void main(String[] args) 
    {
        //main block
        System.out.println("This is main method block");
    }
}

```

```console
-----Ouput-----
Value of a: 10
Value of Instance Variable c: 10
Value of Instance variable d: 100
This is main method block
```

5. In case of multiple static blocks they execute in the order they are defined in the class.

```java
package myPackage;

public class StaticBlockDemo {
	int a=10;
	static int b=20;
	static {
		System.out.println("This is static block: "+ b);
	}

    static {
        System.out.println("This is Second Static Block.");
    }
	
	public static void main(String[] args) {
        //main method block
	}
	
	static {
		System.out.println("This is Third Static block");
	}

}

```
```console
-----Ouput-----
This is First Static Block.
This is Second Static Block.
This is Third Static Block.
```

6. All static blocks executes only once per classloader.

## Non-Static Block
1. Non-static block executes whenever the object is created, even before the constructor call.

```java 
//Case-1: non creating any object
package myPackage;

public class StaticBlockDemo {

	//non static block
     {
        System.out.println("This is non-static block");
    
     }
     
     //constructor
     StaticBlockDemo(){
    	 System.out.println("This is constructor");
     }
	
	public static void main(String[] args) {
		//main method block
		System.out.println("This is main method block");
		
	}

}
```
```console
-----Ouput-----
This is main method block

```

```java
//case-2: Creating object
package myPackage;

public class StaticBlockDemo {

	//non static block
     {
        System.out.println("This is non-static block");
    
     }
     
     //constructor
     StaticBlockDemo(){
    	 System.out.println("This is constructor");
     }
	
	public static void main(String[] args) {
		//main method block
		System.out.println("This is main method block");
		StaticBlockDemo sbd = new StaticBlockDemo();
		
	}

}
```

```console
-----Ouput-----
This is main method block
This is non-static block
This is constructor

```
2. No keyword is prefix to non-static block, unlike static blocks.

3. In case of multiple non-static blocks, the block executes in the same order how they are defined.

```java
package myPackage;

public class StaticBlockDemo {

	//non static block
     {
        System.out.println("This is first non-static block");
    
     }
     
   //non static block
     {
        System.out.println("This is second non-static block");
    
     }
     //constructor
     StaticBlockDemo(){
    	 System.out.println("This is constructor");
     }
	
	public static void main(String[] args) {
		//main method block
		System.out.println("This is main method block");
		StaticBlockDemo sbd = new StaticBlockDemo();
		
	}
	
	//non static block
    {
       System.out.println("This is third non-static block");
   
    }
}
```

```console
-----Ouput-----
This is main method block
This is first non-static block
This is second non-static block
This is third non-static block
This is constructor

```
4. All static and non-static fields can be access freely.

```java
package myPackage;

public class StaticBlockDemo {
	int a=10;
	static int b=20;
	StaticBlockDemo()
	{
		System.out.println("This is constructor");
	}
	
	
	{
		System.out.println("This is non static block non static value: "+ a);
		System.out.println("This is non static block staic value: "+ b);
	}
	
	public static void main(String[] args) {
		System.out.println("This is main method!!!");
		StaticBlockDemo demo = new StaticBlockDemo();
			
	}

}

```

```console
-----Ouput-----
This is main method!!!
This is non static block non static value: 10
This is non static block staic value: 20
This is constructor
```
5. All non-static block executes every time an object is created.
```java
package myPackage;

public class StaticBlockDemo {
	int a=10;
	static int b=20;
	StaticBlockDemo()
	{
		System.out.println("This is constructor");
	}
	
	
	{
		System.out.println("This is non static block non static value: "+ a);
		System.out.println("This is non static block staic value: "+ b);
	}
	
	public static void main(String[] args) {
		System.out.println("This is main method!!!");
		StaticBlockDemo demo = new StaticBlockDemo();
		StaticBlockDemo demo1 = new StaticBlockDemo();
			
	}

}

```

```console
-----Ouput-----
This is main method!!!
This is non static block non static value: 10
This is non static block staic value: 20
This is constructor
This is non static block non static value: 10
This is non static block staic value: 20
This is constructor
```

## Code from the class 06.08.2022
```java
//Complete Program
package myPackage;

public class StaticBlockDemo {
	int a=10;
	static int b=20;
	StaticBlockDemo()
	{
		System.out.println("This is constructor");
	}
	static {
		System.out.println("This is static block: "+ b);
	}
	
	{
		System.out.println("This is non static block non static value: "+ a);
		System.out.println("This is non static block staic value: "+ b);
	}
	
	public static void main(String[] args) {
		System.out.println("This is main method!!!");
		StaticBlockDemo demo = new StaticBlockDemo();
		StaticBlockDemo demo1 = new StaticBlockDemo();
		b = 12;
		System.out.println("b value: "+b);
		System.out.println("StaticBlockDemo.b: "+ StaticBlockDemo.b);
		System.out.println("demo.b: "+ demo.b);
		demo.b = 123;
		System.out.println("demo1.b: "+demo1.b);
		
		System.out.println("demo.a: "+ demo.a);
		demo.a = 10000;
		System.out.println("demo.a: "+ demo.a);
		System.out.println("demo1.a: "+ demo1.a);
		
	}
	
	static {
		b = 1000;
		System.out.println("This is second Static block: "+b);
	}

}

```

```console
-----Ouput-----
This is static block: 20
This is second Static block: 1000
This is main method!!!
This is non static block non static value: 10
This is non static block staic value: 1000
This is constructor
This is non static block non static value: 10
This is non static block staic value: 1000
This is constructor
b value: 12
StaticBlockDemo.b: 12
demo.b: 12
demo1.b: 123
demo.a: 10
demo.a: 10000
demo1.a: 10

```