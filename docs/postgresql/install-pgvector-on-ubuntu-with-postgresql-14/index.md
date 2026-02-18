---
keywords: [pgvector, postgresql, ubuntu, vector extension, installation]
---

# Install pgvector on Ubuntu with PostgreSQL 14

## Installation Procedure

### Step 1: Install prerequisites

- Install the required tools to build the extension.

```bash
sudo apt update
sudo apt install -y postgresql-server-dev-14 build-essential git
```

### Step 2: Clone and build pgvector

- Clone and build the extension.

```bash
git clone https://github.com/pgvector/pgvector.git
cd pgvector
make
sudo make install
```

### Step 3: Switch to the postgres user and start the psql terminal

- Switch to the postgres user and start the psql terminal.

```bash
sudo -i -u postgres
psql
```

### Step 4: Enable the extension in the database

- Enable the extension in the database.

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### Step 5: Verify extension installation

```sql
select * from pg_extension;
```

- Verify that there is a row with the extension name `vector`

  oid  | extname | extowner | extnamespace | extrelocatable | extversion | extconfig | extcondition
-------+---------+----------+--------------+----------------+------------+-----------+--------------
 13747 | plpgsql |       10 |           11 | f              | 1.0        |           |
 16384 | vector  |       10 |         2200 | t              | 0.8.0      |           |
(2 rows)


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/postgresql/install-pgvector-on-ubuntu-with-postgresql-14](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/postgresql/install-pgvector-on-ubuntu-with-postgresql-14)
