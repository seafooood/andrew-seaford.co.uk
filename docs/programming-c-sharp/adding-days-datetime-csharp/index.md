---
title: "Adding days to a DateTime in C#"
date: 2013-08-28
categories: 
  - "csharp"
slug: "adding-days-datetime-csharp"
---

Add seven days to the current time.

```
DateTime start = DateTime.Now;
Console.WriteLine("Start date = " + start.ToString("dd/MM/yyyy hh:mm:ss"));
DateTime end = start.AddDays(7);
Console.WriteLine("End date = " + end.ToString("dd/MM/yyyy hh:mm:ss"));

```

Other methods for defining a DateTime object

```
DateTime start = DateTime.Parse("23/01/1984 01:02:03");

```

```
DateTime start = new DateTime(1984, 01, 23, 01, 02, 03);

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20c%20sharp/adding%20days%20datetime%20csharp](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20c%20sharp/adding%20days%20datetime%20csharp)
