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
slug: "oracle-insert-date"
---

A simple SQL example of using the To\_Date function to format a date.

```
INSERT INTO EXAMPLETBL (EXAMPLEID, EXAMPLEDATE) VALUES ('5', TO_DATE('2014-05-08 08:06:24', 'YYYY-MM-DD HH24:MI:SS'))

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/oracle/oracle%20insert%20date](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/oracle/oracle%20insert%20date)
