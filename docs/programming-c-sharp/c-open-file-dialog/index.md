---
title: "C# Open File Dialog"
date: 2015-01-07
categories:
  - "csharp"
keywords: [csharp, file-dialog, openfiledialog, windows-forms, ui]
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

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/c-open-file-dialog](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/c-open-file-dialog)

## C# Related Articles

- [Adding days to a DateTime in C#](../adding-days-datetime-csharp/index.md)
- [Create arraylist](../create-arraylist/index.md)
- [Create a autocompleting textbox using C#](../create-autocompleting-textbox-c/index.md)
- [C# class properties](../csharp-class-properties/index.md)
- [C# type checking with the is statement](../csharp-type-checking-statement/index.md)
