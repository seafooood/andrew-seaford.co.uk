---
title: "Convert a date and time to UTC"
date: 2011-11-13
categories:
  - "php"
keywords: [php, date, time, utc, conversion]
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

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-php/convert-date-time-utc](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-php/convert-date-time-utc)

## PHP Related Articles

- [Sound Buttons](../sound-buttons/index.md)
- [Split a name into First name and Last name using PHP](../split-php/index.md)
- [Convert a url data in to Name Value Pairs array PHP](../urltonvp/index.md)
- [Installing MySQL with phpMyAdmin](../../mysql/installing-mysql-with-phpmyadmin/index.md)
- [How To Find WooCommerce Consumer Key and Secret](../../woocommerce/how-to-find-woocommerce-consumer-key-and-secret/index.md)
