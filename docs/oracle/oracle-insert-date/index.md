---
title: "Oracle Insert Date"
date: 2014-07-22
categories:
  - "oracle"
tags:
  - "insert"
  - "oracle-2"
  - "sql"
  - "to_date"
keywords: [oracle, sql, date, insert, to_date]
---

A simple SQL example of using the To\_Date function to format a date.

```
INSERT INTO EXAMPLETBL (EXAMPLEID, EXAMPLEDATE) VALUES ('5', TO_DATE('2014-05-08 08:06:24', 'YYYY-MM-DD HH24:MI:SS'))

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/oracle/oracle-insert-date](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/oracle/oracle-insert-date)

## Oracle Related Articles

- [Backup Oracle database with Windows Batch Script](../backup-oracle-database/index.md)
- [Installing MySQL with phpMyAdmin](../../mysql/installing-mysql-with-phpmyadmin/index.md)
- [Create m3u playlist from directory list](../../windows-cmd/create-m3u-playlist-from-directory-list/index.md)
- [Adding days to a DateTime in C#](../../programming-c-sharp/adding-days-datetime-csharp/index.md)
- [C# Open File Dialog](../../programming-c-sharp/c-open-file-dialog/index.md)
