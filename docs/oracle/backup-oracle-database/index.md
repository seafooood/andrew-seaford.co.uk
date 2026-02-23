---
title: "Backup Oracle database with Windows Batch Script"
date: 2014-07-22
categories:
  - "command-scripts"
  - "prog"
keywords: [oracle, backup, batch, database, windows]
---

This simple batch script creates a new folder based on the date and time and then executes a oracle database dump.

```
REM Backup oracle database

@echo Starting database backup

REM get the current datestamp in the format year-month-day-hour-minute
SET DATESTAMP=%date:~6,4%-%date:~3,2%-%date:~0,2%-%time:~0,2%-%time:~3,2%

REM Create a new directory
md "c:\backup\%DATESTAMP%"

REM backup database
REM Dont forget to change username and password
exp username/password@xe FILE="c:\backup\%DATESTAMP%\databasename.dmp"

@echo Finished backing up database to c:\backup\%DATESTAMP%

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/oracle/backup-oracle-database](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/oracle/backup-oracle-database)

## Oracle Related Articles

- [Oracle Insert Date](../oracle-insert-date/index.md)
- [Installing MySQL with phpMyAdmin](../../mysql/installing-mysql-with-phpmyadmin/index.md)
- [Create m3u playlist from directory list](../../windows-cmd/create-m3u-playlist-from-directory-list/index.md)
- [Adding days to a DateTime in C#](../../programming-c-sharp/adding-days-datetime-csharp/index.md)
- [C# Open File Dialog](../../programming-c-sharp/c-open-file-dialog/index.md)
