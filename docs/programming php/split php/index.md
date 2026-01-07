---
title: "Split a name into First name and Last name using PHP"
date: 2013-08-30
categories: 
  - "php"
slug: "split-php"
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
