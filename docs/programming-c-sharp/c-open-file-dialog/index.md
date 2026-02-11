---
title: "C# Open File Dialog"
date: 2015-01-07
categories: 
  - "csharp"
slug: "c-open-file-dialog"
---

```cs
// Configure open file dialog box 
Microsoft.Win32.OpenFileDialog dlg = new Microsoft.Win32.OpenFileDialog();
dlg.Title = "Select File"; // dialog title
dlg.FileName = ""; // Default file name 
dlg.DefaultExt = ".csv"; // Default file extension 
dlg.Filter = "CSV File (.csv)|*.csv|All Files (*.*)|*.*"; // Filter files by extension 

// Show the dialog and process result
if (dlg.ShowDialog() == true)
{
    string filename = dlg.FileName;
}
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20c%20sharp/c%20open%20file%20dialog](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20c%20sharp/c%20open%20file%20dialog)
