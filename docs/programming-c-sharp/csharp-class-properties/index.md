---
title: "C# class properties"
date: 2013-08-28
categories:
  - "csharp"
keywords: [csharp, properties, class, getter-setter, object-oriented]
---

The code below shows the short hand and long hand syntax for defining class properties.

```
public class Example
{
  // class property short hand
  public string Firstname {get; set;}

  // class property long hand
  private string _Lastname;
  public string Lastame
  {
     get {return _Lastname}
     set {_Lastname = value}
  }
}

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/csharp-class-properties](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/csharp-class-properties)
