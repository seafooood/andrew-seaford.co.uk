---
title: "Sound Buttons"
date: 2012-02-25
categories: 
  - "natural-language-processing"
  - "php"
slug: "sound-buttons"
---

Sound Buttons are a technique used to teach children to read. This function generates the sound buttons for a given word, uing the Jolly Phonics system. This approach breaks each word into the groups of letter sounds, of which there are 42 letter sounds.

```php
/**
 * Generates phonics for a given word.
 * This function uses the Jolly Phonics, synthetic phonics programme.    
 * @param input The input word
 * @return array of phonemes
 */   
function phonomes($input)
{
  // create the output array
  $output = array();
  
  // create the Phoneme arrays
  $phoneme3 = array('ear','igh');
  $phoneme2 = array('ai','ar','ch','ck','ee','er','ie','ng','oa','oi','oo','or','ou','ow','qu','sh','th','ue','ue','ur');
  
  // process the input word
  $word =strtolower($input);
  $word = trim($word);
  $letterCount = strlen($word);
  $index = 0;
  
  // iterate each letter in the word searching for phonemes
  while($index <$letterCount)
  {
    if (in_array(substr($word, $index, 3), $phoneme3))
    {
      // found a three letter phoneme
      $output[] = substr($word,$index, 3);
      $index += 3;
    }
    else if (in_array(substr($word, $index, 2), $phoneme2))
    {
      // found a two letter phoneme
      $output[] = substr($word,$index, 2);
      $index += 2;
    }
    else
    {
      //found a single letter phoneme
      $output[] = substr($word,$index, 1);
      $index++;    
    }   
  }
  return $output;
}

```

To test the phonomes function use

```php
foreach(array('this','moth','that','three','them','thin','quick','quilt','liquid','squid') as $test)
{
  print "$test = " . implode(' - ', phonomes($test)) . "";
}

```

This produces the following output

- this = th - i - s
- moth = m - o - th
- that = th - a - t
- three = th - r - ee
- them = th - e - m
- thin = th - i - n
- quick = qu - i - ck
- quilt = qu - i - l - t
- liquid = l - i - qu - i - d
- squid = s - qu - i - d

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20php/sound%20buttons](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20php/sound%20buttons)
