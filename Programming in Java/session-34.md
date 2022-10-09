# Exception Handling :
## Exception: 
* An unexpected and unwanted event occurs in java programming during run time that stop or terminated the execution of program in Abnormal manner is called Exception.

## Purpose of Exception Handling: 
* To execute the java program in a smooth manner and terminate Normally. 
* Exception handling is done by providing alternate code that gets executed and makes possible for Normal Termination.

## Runtime Stack Concept:

```java
package exceptions.basic2;

public class Demo1 {

	public static void main(String[] args) {
		
		method1();
		System.out.println("main() terminated");

	}
	
	public static void method1() {
		
		method2();
		System.out.println("method1() terminated");
	}

	public static void method2() {
		
		System.out.println("Welcome to Jain Deemed to be University");
		System.out.println("method2()terminated ");
	}
}

```

Ouput:
```console
Welcome to Jain Deemed to be University
method2()terminated 
method1() terminated
main() terminated

```

## Default Exception:

```java
package exceptions.basic2;

public class DefaultException {

		public static void main(String[] args) {
			
			method1();
			System.out.println("main() terminated");

		}
		
		public static void method1() {
			
			method2();
			System.out.println("method1() terminated");
		}

		public static void method2() {
			
			System.out.println(10/0); //problematic Code
			System.out.println("method2()terminated ");
		}
	}

```

```console
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at exceptions.basic2.DefaultException.method2(DefaultException.java:20)
	at exceptions.basic2.DefaultException.method1(DefaultException.java:14)
	at exceptions.basic2.DefaultException.main(DefaultException.java:7)

```
## Information contained in the exception message:
* Name of the Exception
* Description about the exception
* Stack Trace

Note: 
* In this case when exception is not handled will be hand over to the JVM. 
* JVM takes care of producing the message then called Default Exception Handling process. 
* As soon as we as a programmer writes Exception handling code then the concept of Default Exception handling is done.

`Default Exception Handling - 1`
```java
package exceptions.basic2;

public class DefaultException {

		public static void main(String[] args) {
			
			method1();
			

		}
		
		public static void method1() {
			
			method2();
			
		}

		public static void method2() {
			
			System.out.println(10/0); //Risky Code
			
		}
	}

```
output:

```console
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at exceptions.basic2.DefaultException.method2(DefaultException.java:20)
	at exceptions.basic2.DefaultException.method1(DefaultException.java:14)
	at exceptions.basic2.DefaultException.main(DefaultException.java:7)

```
`Default Exception Handling - 2`
```java
package exceptions.basic2;

public class DefaultException {

		public static void main(String[] args) {
			
			method1();
			

		}
		
		public static void method1() {
			System.out.println(10/0);  //Risky Code
			method2();
			
		}

		public static void method2() {
			
			System.out.println("Welcome"); 
			
		}
	}

```
ouput:
```console
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at exceptions.basic2.DefaultException.method1(DefaultException.java:13)
	at exceptions.basic2.DefaultException.main(DefaultException.java:7)

```
`Default Exception Handling - 3`
```java
package exceptions.basic2;

public class DefaultException {

		public static void main(String[] args) {
			System.out.println(10/0);  //Risky Code
			method1();
			

		}
		
		public static void method1() {
			
			method2();
			
		}

		public static void method2() {
			
			System.out.println("Welcome");
			
		}
	}

```

Ouput:
```console
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at exceptions.basic2.DefaultException.main(DefaultException.java:6)

```
## Exception Hierarchy 
```
.
└── Throwable
    ├── Error
    │   ├── AssertionError
    │   ├── LinkageError
    │   │   └── VerifyError
    │   └── VMError
    │       ├── OutOfMemoryError
    │       └── StackOverflowError
    └── Exception
        ├── IOException
        │   └── FileNotFoundException
        ├── InterruptedException
        ├── RemoteException
        └── RuntimeException
            ├── ArithmeticException
            ├── ClassCascadeException
            ├── IllegalArgumentException
            │   └── NumberFormatException
            ├── IndexOutOfBoundsException
            │   ├── ArrayIndexOutOfBoundsException
            │   └── StringIndexOutOfBoundsException
            └── NullPointerException
```

## Checked and Unchecked Exception

## Fully Checked and Partially Checked Exception

## Customized Exception Handling by try--catch Block

## Without try--catch Block (Abnormal Termination)

## With try--catch 
* `Risky Code:` goes to try block
* `Alternative Code:` goes to catch block 

Example:
```java
package exceptions.basic2;

public class DefaultException {

		public static void main(String[] args) {
			System.out.println("statement-1");
			System.out.println(10/0); //Risky Code
			System.out.println("Statement-3");
		}
		
		
	}
```
Output:
```console
statement-1
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at exceptions.basic2.DefaultException.main(DefaultException.java:7)

```

## Handling the Above Exception
```java
package exceptions.basic2;

public class DefaultException {

		public static void main(String[] args) {
			System.out.println("statement-1");
			try{
				System.out.println(10/0); //Risky Code
			}
			catch(ArithmeticException e) {
				System.out.println(e);
				System.out.println("Handled Successfully");
			}
			System.out.println("Statement-3");
		}
		
		
	}

```

Output:
```console
statement-1
java.lang.ArithmeticException: / by zero
Handled Successfully
Statement-3

```
## Control Flow in try--catch block
Example code snippet
```java

```
### Case-1: No Exception occurs


### Case-2: There is exception raised at Statement-2 and the corresponding Catch Block is Matched


### Case-3: There is exception raised at Statement-2 and the corresponding Catch Block is not Matched

### Case-4: There is exception raised at Statement-4 


Note:
We should keep each Risky code in seperate try blocks rather than keeping every risky code in the same try block.


## Methods to print the Exception Information

1. e.printStackTrace();
2. System.out.println(e.toString()); or System.out.println(e);
3. System.out.println(e.getMessage());

## Information contained in the Exception 
1. Name of the Exception that has occured.
2. Description of the Exception.
3. Stack Trace 

## try with multiple catch Block
```java
package exceptions.basic2;

public class DefaultException {

		public static void main(String[] args) {
			try {
				System.out.println("Statement-1");
				System.out.println("Statement-2");
				System.out.println("Statement-3");
			}
			catch(Exception e) {
				System.out.println("Statement-4");
			}
			catch(Exception e) {
				System.out.println("Statement-5");
			}
			catch(Exception e) {
				System.out.println("Statement-6");
			}
			
			System.out.println("Statement-7");
			
		}

	}
```
Output:
```console
Exception has already been caught
```

## finally Block (Clean up code)
```java
package exceptions.basic2;

public class DefaultException {

		public static void main(String[] args) {
			try {
				System.out.println("Statement-1");
				System.out.println("Statement-2");
				System.out.println("Statement-3");
			}
			catch(Exception e) {
				System.out.println("Statement-4");
			}
			finally {
				System.out.println("Statement-5");
			}
			System.out.println("Statement-6");
		}
		
	}
```

Note:
* finally block will always execute irrespective of exception occured or not as well as irrespective of Exception is handled or not.

* Once the execution flow entered to try--block the finally must exectute.

## Constrol flow of try-catch-finally 
```java
package exceptions.basic2;

public class DefaultException {

		public static void main(String[] args) {
			try {
				System.out.println("Statement-1");
				System.out.println("Statement-2");
				System.out.println("Statement-3");
			}
			catch(Exception e) {
				System.out.println("Statement-4");
			}
			finally{
                System.out.println("Statement-5");
            }
			
			System.out.println("Statement-6");
		}

	}
```

## Complete the following with the respective code and it ouput
### Case-1: There is No Exception raised

### Case-2: Exception Raised at the Statement-2 and corresponding Exception is matched

### Case-3: Exception Raised at the Statement-2 and corresponding Exception is not matched

### Case-4: Exception Raised at Statement-4

### Case-5: Exception Raised at Statement-5

### Case-6: Exception Raised at Statement-6

## finally Block vs Return Statement
Note: We can have return statement in the try, catch, even in finally block as well.

```java
package exceptions.basic2;

public class FinallyVsReturn {
	public static void main(String args[]) {
		System.out.println(method1());
	}
	
	public static int method1() {
		try {
			System.out.println("try block");
			return 10;
			
		}
		catch(Exception e) {
			System.out.println("catch block");
			return 100;
		}
		finally {
			System.out.println("finally block");
			return 1000;
		}
	}
}

```

Output:
```console
try block
finally block
1000
```

Note: 
* finally block will not execute only in one case when the program exits and the JVM get Shuts down by executing the statement below:
```java
System.exit(0); 
//0 means Normal Termination
//non-zero means abnormal Termination
```
## Nested try-catch-finally
```java

try {
	------------
	try {
		-----------------
		-----------------
		-----------------
	}
	catch(Exception e) {
		-----------------
	}
	------------
}
catch(Exception e) {
	------------
}
finally{
    ------------
}
-----------
```
## Constrol flow of Nested try-catch-finally
```java
package exceptions.basic2;

public class ControlflowNestedTryCatchFinally {
	public static void main(String args[]) {

		try {
			System.out.println("Statement-1");
			System.out.println("Statement-2");
			System.out.println("Statement-3");
			try {
				System.out.println("Statement-4");
				System.out.println("Statement-5");
				System.out.println("Statement-6");
			}
			catch(Exception e) {
				System.out.println("Statement-7");
			}
			finally {
				System.out.println("Statement-8");
			}
			System.out.println("Statement-9");
		}
		catch(Exception e) {
			System.out.println("Statement-10");
		}
		finally {
			System.out.println("Statement-11");
		}
		System.out.println("Statement-12");
	}

}

```

## Complete the following with the respective code and it ouput

### Case-01: There is no Exception Raised

### Case-02: Exception Raised at Statement-2 and Corresponding Exception is matched

### Case-03: Exception Raised at Statement-2 and Corresponding Exception is not matched

### Case-04: Exception Raised at Statement-5 and Corresponding Exception is matched

### Case-05: Exception Raised at Statement-5 and Corresponding Exception is not matched in Inner catch block but matched in Outter catch block

### Case-06: Exception Raised at Statement-5 and Corresponding Exception is not matched either in Inner catch or Outter catch Block

### Case-07: Exception Raised at Statement-7 and corresponding Exception is matched

### Case-08: Exception Raised at Statement-7 and corresponding Exception is not matched

### Case-09: Exception Raised at Statement-8 and corresponding Exception is matched

### Case-10: Exception Raised at Statement-8 and corresponding Exception is matched

### Case-11: Exception Raised at Statement-9 and corresponding Exception is matched

### Case-12: Exception Raised at Statement-9 and corresponding Exception is not matched

### Case-13: Exception Raised at Statement-10

### Case-14: Exception Raised at Statement-11

## Various Possible Combination of try-catch-finally

### Combination-01
```java
try{
    ----
}
catch(X e){
    ----
}
```
### Combination-02
```java
try{
    ----
}
catch(X e){
    ----
}
catch(Y e){
    ----
}
```
### Combination-03
```java
try{
    ----
}
catch(X e){
    ----
}
catch(X e){
    ----
}
```
### Combination-04
```java
try{
    ----
}
catch(X e){
    ----
}
finally {
    ----
}
```
### Combination-05
```java
try{
    ----
}
catch(X e){
    ----
}

try{
    ------
}
catch(X e){
    ----
}
```
### Combination-06
```java
try{
    ----
}
finally {
    ----
}

```
### Combination-07
```java
try{
    ----
}

```
### Combination-08
```java
catch(Y e){
    ----
}
```
### Combination-09
```java
finally {
    ----
}

```
### Combination-10
```java
try{
    ----
}
finally {
    ----
}
catch(Y e){
    ----
}
```
### Combination-11
```java
try{
    ----
}
try{
    ----
}
catch(X e){
    ----
}
finally {
    ----
}
```
### Combination-12
```java
try{
    ----
}
catch(X e){
    ----
}
catch(Y e){
    ----
}
finally {
    -----
}
```
### Combination-13
```java
try{
    ----
}
catch(X e){
    ----
}
finally{
    ----
}
finaly {
    -----
}
```
### Combination-14
```java
try{
    ----
}
System.out.println("Statement");
catch(X e){
    ----
}
```
### Combination-15
```java
try{
    ----
}
catch(X e){
    ----
}
System.out.println("Statement");
catch(Y e){
    ----
}
```
### Combination-16
```java
try{
    ----
}
catch(X e){
    ----
}
System.out.println("statement");
finally {
    ----
}
```
### Combination-17
```java
try{
    ----
    try{
        ----
    }
}
catch(X e){
    ----
}
```
### Combination-18
```java
try{
    ----
    try{
        ----
    }
    catch( Y e){
        ----
    }
}
catch(X e){
    ----
}

```
### Combination-19
```java
try{
    ----
    try{
        ----
    }
}
catch(X e){
    ----
}
```
### Combination-20
```java
try{
    ----
}
catch(X e){
    ----
    try{
        -----
    }
    catch(Y e){
        -----
    }
}
```
### Combination-21
```java
try{
    ----
}
catch(X e){
    ----
}
finally {
    ----
    try{
        ----
    }
    catch(Y e){
        -----
    }
    finally{
        -----
    }
}
```
### Combination-22
```java
try
    System.out.println("Statement");
catch(X e){
    ----
    System.out.println("Statment");
}
```
### Combination-23
```java
try{
    ----
}
catch(X e)
    System.out.println("Statement");
```
### Combination-24
```java
try{
    ----
}
catch(X e){
    ----
}
finally 
    System.out.println("Statement");
```

## Throw Exception
Programmer throw Exception object, JVM catches the Exception.

### Without throw Keyword
```java 
class Demo{
    public static void main(String args[]){
        System.out.println(10/0);
    }
}
```

```java
class Demo{
    public static void main(String args[]){
        throw new ArithmeticException();
    }
}
```
### Important Cases related to throw Keyword
#### Case-1
```java
class Demo{
    static ArithmeticException e = new ArithmeticException(;)
    public static void main(String args[]){
        throw e;
    }
}
```

```java
class Demo{
    static ArithmeticException e ;
    public static void main(String args[]){
        throw e;
    }
}
```
#### Case-2
```java
class Demo{
    public static void main(String args[]){
        System.out.println(10/0);
        System.out.println("Welcome");
    }
}
```

```java
class Demo{
    public static void main(String args[]){
       throw new ArithmeticException();
        System.out.println("Welcome");
    }
}
```
#### Case-3
```java
class Demo{
    public static void main(String args[]){
       throw new Demo();
    }
}
```

Note:
* `throw` keyword is only used for `Throwable` class (Exception).

```java
class Demo{
    public static void main(String args[]){
        throw new Demo();
    }
}
```

## Need and `Usages` of throws keyword
```java 
class Demo{
    public static void main(String args[]){
        PrintWriter pw = new PrintWriter();
        pw.println("Welcome to Jain Deemed to be University");
    }
}
```

```java 
class Demo{
    public static void main(String args[]){
        int a = 10/0;
    }
}
```

* can be resolve by using `try-catch` block
* can be resolve by using `throws`

## throws across multiple methods
```java
class Demo{
    public static void main(String args[]) throws Exception{
        method1();
    }

    public static void method1() throws Exception{
        method2();
    }

    public static void method2() throws Exception{
        String s = null;
        System.out.println(s.length());
    }
}
```

## User Define Exception

### How to Write User Defined Exception

## try-with Resource

## try-with multiple Resource

## Multiple Catch Block

## Exception Propagation

## Rethrowing Exception