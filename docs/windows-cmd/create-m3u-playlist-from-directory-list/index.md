---
title: "Create m3u playlist from directory list"
date: 2012-04-20
categories: 
  - "command-scripts"
tags: 
  - "create"
  - "generate"
  - "iterate-folders"
  - "m3u-playlist"
  - "windows-command-script"
slug: "create-m3u-playlist-from-directory-list"
---

This little command script iterates all sub folders to create an m3u playlist containing mp3 files. The m3u playlist can then be played using winamp.

To create the command script, open a text editor and add the following line.

```
dir *.mp3 /b /s > "playlist.m3u"

```

Next save the file as create-playlist.cmd. To execute place the command script in the same folder as the mp3s and double click create-playlist.cmd, this will generate playlist.m3u. Then open playlist.m3u in winamp.


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/windows%20cmd/create%20m3u%20playlist%20from%20directory%20list](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/windows%20cmd/create%20m3u%20playlist%20from%20directory%20list)
