---
title: "Generate safe filenames using Python"
date: 2013-02-08
categories: 
  - "python"
tags: 
  - "operating-system"
  - "python-2"
slug: "generate-safe-filenames-using-python"
---

This function removes illegal  characters to create file names that are safe to use on most operating systems.

```
import string

## Make a file name that only contains safe charaters
# @param inputFilename A filename containing illegal characters
# @return A filename containing only safe characters
def makeSafeFilename(inputFilename):   
  try:
     safechars = string.letters + string.digits + " -_."
    return filter(lambda c: c in safechars, inputFilename)
   except:
     return ""  
  pass

print makeSafeFilename("test1******.txt")  # test1.txt

print makeSafeFilename("test2:\.txt") # test2.txt

print makeSafeFilename("test39328764876!%^&*().txt") # test39328764876.txt

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20python/general/generate%20safe%20filenames%20using%20python](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20python/general/generate%20safe%20filenames%20using%20python)
