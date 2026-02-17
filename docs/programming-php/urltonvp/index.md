---
title: "Convert a url data in to Name Value Pairs array PHP"
date: 2013-08-29
categories: 
  - "php"
---

Convert a url data in to Name Value Pairs array.

```
/** Convert a url data in to Name Value Pairs array
 * @param url The url and the data string
 * @return array of named value pairs
 */
function urlToNvp($url)
{
   $output = array();
   
   $questionmark = strpos($url, '?');
   if ($questionmark !== false)
   {
      $url = substr($url, $questionmark+1, strlen($url));
   }   
   
   foreach(explode('&', $url) as $data)
   {
      $value = explode('=', $data);
      $output[$value[0]] = $value[1];
   }
      
   return $output;
}
```

Here are three examples of using this function

```
print_r(urlToNvp("www.example.co.uk?p1=one&p2=two"));
print_r(urlToNvp("p1=one&p2=two"));
print_r(urlToNvp("www.example.co.uk?p1=one"));

```

The result

> Array ( \[p1\] => one \[p2\] => two ) Array ( \[p1\] => one \[p2\] => two ) Array ( \[p1\] => one )


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-php/urltonvp](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-php/urltonvp)
