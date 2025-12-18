---
title: "Enumerations with tryParse in C#"
date: 2013-08-28
categories: 
  - "csharp"
slug: "enumerations-with-tryparse-csharp"
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
