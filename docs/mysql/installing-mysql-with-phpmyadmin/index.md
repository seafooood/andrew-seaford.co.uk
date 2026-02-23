---
keywords: [mysql, phpmyadmin, lamp stack, ubuntu, tasksel]
---

# Installing MySQL with phpMyAdmin

The fastest way to get started is to install LAMP using tasksel. Tasksel is a Debian/Ubuntu tool that installs multiple related packages as a co-ordinated “task” onto your system.

At a terminal prompt enter the following commands:

```bash
sudo apt-get update
sudo apt-get install -y tasksel
sudo tasksel install lamp-server
```

## References

[Get started with lamp applications](https://ubuntu.com/server/docs/get-started-with-lamp-applications)

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/mysql/installing-mysql-with-phpmyadmin](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/mysql/installing-mysql-with-phpmyadmin)

## MySQL Related Articles

- [How To Perform a Vector Search in A Postgres Database using pgvector](../../postgresql/how-to-perform-a-vector-search-in-a-postgres-database-using-pgvector/index.md)
- [Install pgvector on Ubuntu with PostgreSQL 14](../../postgresql/install-pgvector-on-ubuntu-with-postgresql-14/index.md)
- [Apt vs Apt-get Commands on Ubuntu](../../ubuntu/apt-vs-apt-get/index.md)
- [Disk Cleanup Ubuntu](../../ubuntu/disk-cleanup-ubuntu/index.md)
- [How To Assign A Static Ip Address in Ubuntu](../../ubuntu/how-to-assign-a-static-ip-address-in-ubuntu/index.md)
