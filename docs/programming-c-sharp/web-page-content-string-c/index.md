---
title: "Get Web Page Content as a String with C#"
date: 2012-01-18
categories:
  - "csharp"
keywords: [csharp, web-scraping, http-request, networking, html]
---

This function dowloads the html content of a webpage and returns the content as a string.

```
public static string GetWebPageAsString(string url) {
    HttpWebRequest httpWebRequest =(HttpWebRequest)WebRequest.Create(url);
    HttpWebResponse httpWebResponse = (HttpWebResponse)httpWebRequest.GetResponse();
    Stream stream = httpWebResponse.GetResponseStream();
    StreamReader streamReader = new StreamReader(stream, Encoding.ASCII);
    return streamReader.ReadToEnd();
}

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/web-page-content-string-c](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/web-page-content-string-c)

## C# Related Articles

- [Adding days to a DateTime in C#](../adding-days-datetime-csharp/index.md)
- [C# Open File Dialog](../c-open-file-dialog/index.md)
- [Create arraylist](../create-arraylist/index.md)
- [Create a autocompleting textbox using C#](../create-autocompleting-textbox-c/index.md)
- [C# class properties](../csharp-class-properties/index.md)
