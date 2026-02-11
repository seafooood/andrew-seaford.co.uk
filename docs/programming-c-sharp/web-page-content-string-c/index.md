---
title: "Get Web Page Content as a String with C#"
date: 2012-01-18
categories: 
  - "csharp"
slug: "web-page-content-string-c"
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

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20c%20sharp/web%20page%20content%20string%20c](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20c%20sharp/web%20page%20content%20string%20c)
