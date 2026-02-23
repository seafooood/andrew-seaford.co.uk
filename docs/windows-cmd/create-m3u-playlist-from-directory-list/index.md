---
title: "Create m3u playlist from directory list"
keywords: [windows cmd, m3u playlist, batch script, mp3, directory listing]
date: 2012-04-20
categories:
  - "command-scripts"
tags:
  - "create"
  - "generate"
  - "iterate-folders"
  - "m3u-playlist"
  - "windows-command-script"
---

This little command script iterates all sub folders to create an m3u playlist containing mp3 files. The m3u playlist can then be played using winamp.

To create the command script, open a text editor and add the following line.

```
dir *.mp3 /b /s > "playlist.m3u"

```

Next save the file as create-playlist.cmd. To execute place the command script in the same folder as the mp3s and double click create-playlist.cmd, this will generate playlist.m3u. Then open playlist.m3u in winamp.


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/windows-cmd/create-m3u-playlist-from-directory-list](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/windows-cmd/create-m3u-playlist-from-directory-list)

## Windows Related Articles

- [Backup Oracle database with Windows Batch Script](../../oracle/backup-oracle-database/index.md)
- [Oracle Insert Date](../../oracle/oracle-insert-date/index.md)
- [Adding days to a DateTime in C#](../../programming-c-sharp/adding-days-datetime-csharp/index.md)
- [C# Open File Dialog](../../programming-c-sharp/c-open-file-dialog/index.md)
- [Create arraylist](../../programming-c-sharp/create-arraylist/index.md)
