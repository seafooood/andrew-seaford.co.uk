---
title: "Recursive delete files and folders using C#"
date: 2012-01-18
categories: 
  - "csharp"
slug: "recursive-delete-files-folders-c"
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
