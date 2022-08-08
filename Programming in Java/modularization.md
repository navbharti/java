```python
package myPackage;

public class RectangleDemo {

	public static void main(String[] args) {
		//create local variables
		double l;
		double b;
		l = 12.5;
		b = 14.5;
		double a = area(l, b);
		double p = peri(l, b);
		System.out.println("Area: " + a);
		System.out.println("Perimeter: "+p);
		
	}
	
	//area() method to calculate Rectangle area
	static double area(double l, double b)
	{
		return l * b;
	}
	
	//peri() method to calculate Rectangle Perimeter
	static double peri(double l, double b)
	{
		return 2.0 *(l + b);
	}

}

```

```java
package myPackage;

public class RectangleDemo1 {
	static double l;
	static double b;
	public static void main(String[] args) {
		//initialize value to static variables
		l = 12.5;
		b = 14.5;
		double a = area(l, b);
		double p = peri(l, b);
		System.out.println("Area: " + a);
		System.out.println("Perimeter: "+p);
		
	}
	
	//area() method to calculate Rectangle area
	static double area(double l, double b)
	{
		return l * b;
	}
	
	//peri() method to calculate Rectangle Perimeter
	static double peri(double l, double b)
	{
		return 2.0 *(l + b);
	}

}

```