# Type conversion and casting, Automatic type promotion in Expressions Arrays

`Type Casting`: a data type is `converted by programmer` into another data type using the casting operator `(datatype)`  during the program design.

The destination data type may be `smaller` than the source data type (also called `narrowing conversion`).

May be `compatible datatypes` or `Incompatible datatypes`.

```java 
destination_datatype = (target_datatype)variable;


(): is a casting operator.
```

Example: 
```java 
float x;
byte y;
...
...
y=(byte)x;  //Line 5 
```

`Type Conversion`: a data type is `automatically converted` or `implicitly` into another data type by a compiler at the compiler time.

The destination data type `cannot be smaller` than the source data type (also called Widening conversion).

`Only` be applied to compatible datatypes.

```java
int x=30;
float y;
y=x;  // y==30.000000. 
```

Note: We can easily convert a `primitive data type` into `another primitive data type` by using type casting.

Similarly, it is also possible to convert a `non-primitive data type` (referenced data type) into `another non-primitive data type` by using type casting.

But `we cannot convert` a primitive data type into an advanced (referenced) data type by using type casting. For this case, we will have to use methods of `Java Wrapper classes`.

