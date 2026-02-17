---
title: "How To Use Extension Methods in C#"
date: 2023-04-25
categories: 
  - "csharp"
---

Extension Methods can extend any type with additional methods  
Extension Methods requirements:

- Class must be static

- The function must be static

- The function must use 'this' in the arguments to denote the type that is being extended.

```
using System;

namespace ExtensionMethodExample
{
    internal class Program
    {
        static void Main()
        {
            string hello = "Hello";
            Console.WriteLine(hello.Shout());

            Console.WriteLine("Press any key to exit");
            Console.ReadKey();
        }
    }

    public static class StringExtensions
    {
        public static string Shout(this string message)
        {
            return message.ToUpper();
        }
    }
}
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/how-to-use-extension-methods-in-c](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/how-to-use-extension-methods-in-c)
