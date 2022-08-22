# Menu Driven Program in Java

```java
//File Name: ArithmeticCalc.java
package arithmetic;

public class ArithmeticCalc {
	private double num1;
	private double num2;
	public double getNum1() {
		return num1;
	}
	public void setNum1(double num1) {
		this.num1 = num1;
	}
	public double getNum2() {
		return num2;
	}
	public void setNum2(double num2) {
		this.num2 = num2;
	}
	
	public double add()
	{
		return this.getNum1() + this.getNum2();
	}
	
	public double subtract()
	{
		return this.getNum1() - this.getNum2();
	}

	public double multiply()
	{
		return this.getNum1() * this.getNum2();
 	}
	
	public double divide()
	{
		return this.getNum1() / this.getNum2();
	}
	
}
```

```java
//File Name: ArithmeticDemo.java
package arithmetic;

import java.util.Scanner;

public class ArithmeticDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int choice;
		double n1;
		double n2;
		displayMenu();
		choice = sc.nextInt();
		System.out.println("Enter First Value: ");
		n1 = sc.nextDouble();
		System.out.println("Enter Second Value: ");
		n2 = sc.nextDouble();
		//create object of ArithmeticCalc
		ArithmeticCalc calc = new ArithmeticCalc();
		calc.setNum1(n1);
		calc.setNum2(n2);
		
		switch(choice)
		{
		case 1: 
			
			System.out.println("Addition: "+ calc.add());
			break;
			
			
		case 2:
			System.out.println("Subtraction: "+ calc.subtract());

			break;
			
		case 3: 
			System.out.println("Multiply: "+ calc.multiply());

			break;

		case 4:
			System.out.println("Division: "+ calc.divide());

			break;
			
		case 5:
			System.exit(0);
			break;
		
		default:
			System.out.println("Wrong Choice....");
		}

	}
	
	public static void displayMenu() {
		System.out.println("Main Menu");
		System.out.println("1. Addition");
		System.out.println("2. Subtraction");
		System.out.println("3. Multiplication");
		System.out.println("4. Division");
		System.out.println("5. Exit");
		System.out.println("Your Choice...");
		
	}

}

```

`Question`: Update the Above program to apply looping for the process. Loops exits when option for exiting is given.