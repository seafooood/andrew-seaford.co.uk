---
title: "Simple C# LINQ example"
date: 2013-08-28
categories:
  - "csharp"
keywords: [csharp, linq, query-syntax, collections, filtering]
---

The LINQ example below creates a generic collection of the class Car. Then using a LINQ statement the collection is filtered to find cars that are newer than 2009.

```
List myCars = new List() {
    new Car() { Make="BMW", Model="550i", Year=2009 },
    new Car() { Make="Toyota", Model="4Runner", Year=2010 },
    new Car() { Make="BMW", Model="745li", Year=2008 },
    new Car() { Make="Ford", Model="Escape", Year=2008 },
    new Car() { Make="BMW", Model="550i", Year=2010 }
};

var newCars = from c in myCars
                where c.Year > 2009
                select new { c.Model, c.Make, c.Year };

foreach (var car in newCars)
{
    Console.WriteLine("{0} {1} - {2}", car.Make, car.Model, car.Year);
}

class Car
{
   public string Make { get; set; }
   public string Model { get; set; }
   public int Year { get; set; }
}

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/simple-cshar-linq](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/simple-cshar-linq)

## C# Related Articles

- [Adding days to a DateTime in C#](../adding-days-datetime-csharp/index.md)
- [C# Open File Dialog](../c-open-file-dialog/index.md)
- [Create arraylist](../create-arraylist/index.md)
- [Create a autocompleting textbox using C#](../create-autocompleting-textbox-c/index.md)
- [C# class properties](../csharp-class-properties/index.md)
