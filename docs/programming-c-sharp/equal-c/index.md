---
title: "Almost Equal C#"
date: 2014-07-25
categories:
  - "csharp"
keywords: [csharp, floating-point, comparison, epsilon, math]
---

Test if two values are almost equal.

```
/// 
/// Test if two doubles are approximately equal
/// 
/// Test variable one
/// Test variable two
/// epsilon a measure of equality
/// boolean true = values are approximately equal, false = values are not equal
public static Boolean almostEqual(double a, double b, double eps)
{
    return Math.Abs(a - b) < eps;
}

```

Example using the function.

```
double a = 1.234;
double b = 1.235;
double eps = 0.01;
Console.WriteLine("equal = " + almostEqual(a, b, eps).ToString());

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/equal-c](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/equal-c)

## C# Related Articles

- [Adding days to a DateTime in C#](../adding-days-datetime-csharp/index.md)
- [C# Open File Dialog](../c-open-file-dialog/index.md)
- [Create arraylist](../create-arraylist/index.md)
- [Create a autocompleting textbox using C#](../create-autocompleting-textbox-c/index.md)
- [C# class properties](../csharp-class-properties/index.md)
