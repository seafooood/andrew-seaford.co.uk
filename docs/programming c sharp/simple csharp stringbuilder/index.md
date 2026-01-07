---
title: "Simple c# StringBuilder example"
date: 2013-08-28
categories: 
  - "csharp"
slug: "simple-csharp-stringbuilder"
---

A simple example of using the StringBuilder to concat strings.

```
StringBuilder mySB = new StringBuilder();
mySB.Append("line 1");
mySB.Append("line 2");
mySB.Append("line 3");
Console.WriteLine(mySB.ToString());

```
