---
title: "Reading a file with C#"
date: 2013-08-28
categories: 
  - "csharp"
slug: "reading-file-csharp"
---

Reading a text file line by line in C#. Dont forget to include using System.IO;

```
StreamReader myReader = new StreamReader(@"c:\test.txt");
string line = "";
while (line != null)
{
   line = myReader.ReadLine();
   Console.WriteLine(line);
}

```

You can read all the text within a file using the ReadAllText function.

```
string filename = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments) + @"\test.txt";
string content = File.ReadAllText(filename);
MessageBox.Show(content);

```
