---
title: "C# type checking with the is statement"
date: 2013-08-29
categories: 
  - "csharp"
slug: "csharp-type-checking-statement"
---

A var type can be checked using the 'is' statement

```
var a = 1.0;

if (a is int)
{
    MessageBox.Show("int");
}
else
{
    MessageBox.Show("is NOT int");
}

```
