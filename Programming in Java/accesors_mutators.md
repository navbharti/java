# Accessors (Getters) and Mutaters (Setters)

Since access specifiers are used for applying Data Hiding, we need some mechanism to access private members if not accessible.

### Accesss Specifiers
* default (~)
* private (-)
* public (+)
* protected (#)

Example: 
```java
//File Name: Rectangle.java
package bca.java;

public class Rectangle {
		private double length;
		private double breadth;
		
}

```

`private` variables can only be accessed inside the same class (an outside class has no access to it). It is possible to access `private` variables indirectly through public `getters` and `setters` methods also called `accessor` and `mutators`.

### Getters (Accessors) methods for `length` and `breadth`
```java
//File Name: Rectangle.java
package bca.java;

public class Rectangle {
		private double length;
		private double breadth;
		
		//getters or Accessors
		public double getBreadth()
		{
			return this.breadth;
		}

		public double getLength() {
			// TODO Auto-generated method stub
			return this.length;
		}
		
}

```

### Setters (Mutaters) methods for `length` and `breadth`
```java
package bca.java;

public class Rectangle {
		private double length;
		private double breadth;
        
        //setter or mutoters
		public void setLength(double length) {
			this.length = length;
		}

		public void setBreadth(double breadth) {
			this.breadth = breadth;
		}
		
}

```


The `getter` method returns the private variable value, and the `seters` method sets the value to the private variable.

The `this` keyword is used to refer to the current object.




### Completer Program

```java
//File Name: RectangleDemo.java
package bca.java;

public class RectangleDemo {

	public static void main(String[] args) {
		//create object of Rectangle
		Rectangle r1  = new Rectangle();
		
		//set the length and breadth using setLength() and setBreadth()
		//r1.length = 12.4;
		r1.setLength(12.4);
		r1.setBreadth(5.6);
		
		System.out.println(r1.getLength());
		System.out.println(r1.getBreadth());
		
		System.out.println("Area: "+ r1.area());
		System.out.println("Perimeter: "+ r1.peri());
	}

}
```

```java
//File Name: Rectangle.java
package bca.java;

public class Rectangle {
		private double length;
		private double breadth;
		
		public double area()
		{
			return this.getLength() * this.getBreadth();
		}
		
		public double peri()
		{
			return 2 * (this.getLength() + this.getBreadth());
		}
		
		//getters or Accessors
		public double getBreadth()
		{
			return this.breadth;
		}

		public double getLength() {
			// TODO Auto-generated method stub
			return this.length;
		}

		public void setLength(double length) {
			this.length = length;
		}

		public void setBreadth(double breadth) {
			this.breadth = breadth;
		}
		
}

```