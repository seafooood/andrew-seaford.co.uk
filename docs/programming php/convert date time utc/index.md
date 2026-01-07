---
title: "Convert a date and time to UTC"
date: 2011-11-13
categories: 
  - "php"
slug: "convert-date-time-utc"
---

```
/** Converts a date and time to UTC
* /param date The date in the format dd/mm/yyyy
* /param time The time in the format HH/mm/ss
* /return utc
*/   

function utc($inputDate, $inputTime)
{
$pieces = explode("/", $inputDate);
$dateus = $pieces[2]."-".$pieces[1]."-".$pieces[0];
$stringtime = "$dateus $inputTime";
return strtotime($stringtime);

}

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20php/convert%20date%20time%20utc](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20php/convert%20date%20time%20utc)
