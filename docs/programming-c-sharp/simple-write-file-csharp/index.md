---
title: "Simple Write File using C#"
date: 2013-08-29
categories: 
  - "csharp"
slug: "simple-write-file-csharp"
---

A very simple method for writing to a file, not forget to include using System.IO;.

```
string filename = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments) + @"\test.txt";
string content = "This is the new file content";
File.WriteAllText(filename, content);

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/simple-write-file-csharp](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/simple-write-file-csharp)
