# Introduction to JSP and Servlet :
## JSP (Java Server Page):
1. All features of servlets and extension of servlets
2. Whenever any modification is done in Servlet we must restart the Web Server and redeploye the servlet application in the server.
3. But in case of JSP modificaiton we may not need to restart the server and redeploy the application.
4. JSP is tag based 
5. used in MVS (Model, View and Control) Architecuture.

# Dynamic Web Application Code used in Class

## Develop a Dynamic Web project with one HTML form to enter two number which calls Servlet to do Addition of these two number and display the result.

### Project folder Structure:
```markdown
├── servletproject1
│   └── src
│       └── main
│           ├── java
│           │   └── jain
│           │       └── bca
│           │           └── MyServletForSum.java
│           └── webapp
│               ├── META-INF
│               │   └── MANIFEST.MF
│               ├── WEB-INF
│               │   ├── lib
│               │   ├── web.xml
│               └── index.html
```

### File Name: index.html
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<form action="sum">
	First Number: <input type="text" name="num1" /> <br>
	Second Number: <input type="text" name="num2" /> <br>
	<input type="submit" >
</form>
</body>
</html>
```

```java
//file name: MyServletForSum

package jain.bca;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class MyServletForSum extends HttpServlet {
	
	public void service(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		int n1 = Integer.parseInt(request.getParameter("num1"));
		int n2 = Integer.parseInt(request.getParameter("num2"));
		
		int sum = n1 + n2;
		
	System.out.println(sum);
		PrintWriter out = response.getWriter();
		out.println("The Result: "+ sum);
		
	}

}

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" version="4.0">
	<servlet>
		<servlet-name> sumPage </servlet-name>
		<servlet-class> jain.bca.MyServletForSum</servlet-class>
	</servlet>
	
	<servlet-mapping>
		<servlet-name> sumPage</servlet-name>
		<url-pattern> /sum </url-pattern>
	</servlet-mapping>
	
</web-app>
```

## Communicating one Servlet to another Servlet

## Modify the above project to call one servlet (FactorialServlet) from anther servlet (MyServletForSum) to display the result. MyServletForSum servlet gets two numbers and finds sum of these number then FactorialServlet servlet finds Factorial of the sum value then finally display the factorial as result.

### Folder Structure
```markdown
├── servletproject1
│   └── src
│       └── main
│           ├── java
│           │   └── jain
│           │       └── bca
│           │           ├── FactorialServlet.java
│           │           └── MyServletForSum.java
│           └── webapp
│               ├── META-INF
│               │   └── MANIFEST.MF
│               ├── WEB-INF
│               │   ├── lib
│               │   ├── web.xml
│               │   └── web.xsl
│               └── index.html
```

### Presentation File: index.html
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<form action="sum">
	First Number: <input type="text" name="num1" /> <br>
	Second Number: <input type="text" name="num2" /> <br>
	<input type="submit" >
</form>
</body>
</html>
```

### first servlet file: 
```java
//File Name: MyServletForSum.java
package jain.bca;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class MyServletForSum extends HttpServlet {
	
	public void service(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		int n1 = Integer.parseInt(request.getParameter("num1"));
		int n2 = Integer.parseInt(request.getParameter("num2"));
		
		int sum = n1 + n2;
			
		request.setAttribute("k", sum);
		
		RequestDispatcher dispatcher = request.getRequestDispatcher("factorial");
		dispatcher.forward(request, response);
		
		System.out.println(" dispatcher forwarded ");
	}
}

```

### Second Servlet File
```java
//File Name: FactorialServlet.java
package jain.bca;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class FactorialServlet extends HttpServlet{
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
		System.out.println("Entered to FactorialServlet");
		int n = (int)request.getAttribute("k");
		
		int ans = factorial(n);
		PrintWriter out = response.getWriter();
		out.println("Factorial is "+ ans);
		System.out.println("response page printed");
	}
	
	public int factorial(int n) {
		System.out.println("facorial() method called");
		int f = 1;
		for(int i=1; i<=n; i++)
			f*=i;
		return f;
			
	}
}

```

### Descriptor file (web.xml)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" version="4.0">
	<servlet>
		<servlet-name> sumPage </servlet-name>
		<servlet-class> jain.bca.MyServletForSum</servlet-class>
	</servlet>
	
	<servlet-mapping>
		<servlet-name> sumPage</servlet-name>
		<url-pattern> /sum </url-pattern>
	</servlet-mapping>
	
	<servlet>
		<servlet-name> fact </servlet-name>
		<servlet-class> jain.bca.FactorialServlet</servlet-class>
	</servlet>
	
	<servlet-mapping>
		<servlet-name> fact</servlet-name>
		<url-pattern>/factorial</url-pattern>
	</servlet-mapping>
</web-app>
```

