---
title: "Recursive delete files and folders using C#"
date: 2012-01-18
categories: 
  - "csharp"
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
