---
title: "String formating within C#"
date: 2013-08-28
categories: 
  - "csharp"
slug: "string-formating-csharp"
---

Below is an example of using string formating to print a time

```
int h = 12;
int m = 13;
int s = 14;
string myString = string.Format("{0}:{1}:{2}", h, m, s);
Console.WriteLine(myString);

```

To format a number to two decimal places, you could use the string format.

```
double s = 14.123;
string myString = string.Format("{0:0.00}", s);
Console.WriteLine(myString);

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/string-formating-csharp](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/string-formating-csharp)
