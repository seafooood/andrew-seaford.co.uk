---
title: "Split a name into First name and Last name using PHP"
date: 2013-08-30
categories:
  - "php"
keywords: [php, string, split, parsing, name]
---

```
/** split a name into the first name and last name
 * @param input The name eg 'John Doe'
 * @return Array containing firstname and lastname eg array('firstname'=>'John', 'lastname'=>'Doe');
 */
function splitname($input)
{
   $output = array("firstname"=>"", "lastname"=>"");
   $space = strpos($input, " ");
   if ($space !== false)
   {
      $output['firstname'] = substr($input, 0, $space);
      $output['lastname'] = substr($input, $space, strlen($input));     
   }
   else
   {
      $output['lastname'] = $input;
   } 
   return $output;
}

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-php/split-php](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-php/split-php)

## PHP Related Articles

- [Convert a date and time to UTC](../convert-date-time-utc/index.md)
- [Sound Buttons](../sound-buttons/index.md)
- [Convert a url data in to Name Value Pairs array PHP](../urltonvp/index.md)
- [Installing MySQL with phpMyAdmin](../../mysql/installing-mysql-with-phpmyadmin/index.md)
- [How To Find WooCommerce Consumer Key and Secret](../../woocommerce/how-to-find-woocommerce-consumer-key-and-secret/index.md)
