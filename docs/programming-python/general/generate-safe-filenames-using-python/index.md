---
title: "Generate safe filenames using Python"
date: 2013-02-08
categories:
  - "python"
tags:
  - "operating-system"
  - "python-2"
keywords: [python, filename, sanitization, string-filtering, filesystem]
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

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/general/generate-safe-filenames-using-python](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/general/generate-safe-filenames-using-python)

## Python Related Articles

- ['django-admin startproject' vs 'python -m django startproject'](../../django/'django-admin-startproject'-vs-'python-m-django-startproject'/index.md)
- [Creating a Django Site With User Authentication](../../django/creating-a-django-site-with-user-authentication/index.md)
- [Django Database Seeding](../../django/django-database-seeding/index.md)
- [Getting Started with Django for Flask Developers](../../django/getting-started-with-django-for-flask-developers/index.md)
- [Getting Started with Django - Working with Databases](../../django/getting-started-with-django-working-with-databases/index.md)
