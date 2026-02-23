---
title: "Explicit Conversion of a string to Integer using c#"
date: 2013-08-28
categories:
  - "csharp"
keywords: [csharp, conversion, parsing, type-casting, int-parse]
---

Explicit Conversion of a string to Integer, sometimes known as cast.

```
string myString = "7";
int myInt = int.Parse(myString);
Console.WriteLine(myInt);

```

The above code will fail if the string can not be converted to a integer. For example if myString="Seven", the code would fail. To avoid this problem use TryParse.

```
string myString = "Seven";
int myInt = 0;
if (int.TryParse(myString, out myInt) == true)
{
   Console.WriteLine("String converted");
}
else
{
   Console.WriteLine("String NOT converted");
}
Console.WriteLine(myInt);

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/explicit-conversion-string-integer-csharp](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/explicit-conversion-string-integer-csharp)

## C# Related Articles

- [Adding days to a DateTime in C#](../adding-days-datetime-csharp/index.md)
- [C# Open File Dialog](../c-open-file-dialog/index.md)
- [Create arraylist](../create-arraylist/index.md)
- [Create a autocompleting textbox using C#](../create-autocompleting-textbox-c/index.md)
- [C# class properties](../csharp-class-properties/index.md)
