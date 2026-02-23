---
title: "Enumerations with tryParse in C#"
date: 2013-08-28
categories:
  - "csharp"
keywords: [csharp, enumeration, enum, tryparse, parsing]
---

Here is an example of using enum with a tryParse. The program asks the user to enter a new state. The tryParse then attempts to convert the input into a enum.

```
// define current state
MyState currentState = MyState.off;
            
// get value from user
Console.WriteLine("Please enter the new state");
string input = Console.ReadLine();

if (Enum.TryParse(input, out currentState) == false)
{
    Console.WriteLine("Unable to compute input");
}
Console.WriteLine("Current state " + currentState);

Console.WriteLine("=== Finished ===");
Console.ReadLine();
}

enum MyState
{
on,
off,
idle
}

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/enumerations-with-tryparse-csharp](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/enumerations-with-tryparse-csharp)

## C# Related Articles

- [Adding days to a DateTime in C#](../adding-days-datetime-csharp/index.md)
- [C# Open File Dialog](../c-open-file-dialog/index.md)
- [Create arraylist](../create-arraylist/index.md)
- [Create a autocompleting textbox using C#](../create-autocompleting-textbox-c/index.md)
- [C# class properties](../csharp-class-properties/index.md)
