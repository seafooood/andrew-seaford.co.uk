---
title: "Recursive delete files and folders using C#"
date: 2012-01-18
categories:
  - "csharp"
keywords: [csharp, file-deletion, recursion, directory-operations, file-io]
---

This function will Recursively delete all files and folders.

```
private void DeleteAllFiles(string sPath)
{
    foreach(string strFile in Directory.GetFiles(sPath))
    {
        File.Delete(strFile);
    }
    foreach (string strDir in Directory.GetDirectories(sPath))
    {
        DeleteAllFiles(strDir);
    }
    Directory.Delete(sPath);
}

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/recursive-delete-files-folders-c](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/recursive-delete-files-folders-c)

## C# Related Articles

- [Adding days to a DateTime in C#](../adding-days-datetime-csharp/index.md)
- [C# Open File Dialog](../c-open-file-dialog/index.md)
- [Create arraylist](../create-arraylist/index.md)
- [Create a autocompleting textbox using C#](../create-autocompleting-textbox-c/index.md)
- [C# class properties](../csharp-class-properties/index.md)
