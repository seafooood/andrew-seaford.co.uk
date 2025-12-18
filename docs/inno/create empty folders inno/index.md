---
title: "Create empty folders using Inno"
date: 2015-02-23
categories: 
  - "inno"
slug: "create-empty-folders-inno"
---

When installing a program using Inno, to create an empty directory you will need to add a dirs section to the installer script.

`[Dirs] Name: "{app}\Example1"`

Download installer script [**CreateEmptyDirectories.iss**](http://andrew-seaford.co.uk/code/CreateEmptyDirectories.iss "CreateEmptyDirectories.iss")
