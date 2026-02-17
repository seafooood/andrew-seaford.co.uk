# How To Create A Multi Layer Docker Compose

## Introduction

Many projects need to support multiple environments or configurations (like Oracle vs. Postgres, local vs. CI, dev vs. prod).

In this article we are going to explore using multiple compose files layered together. This is the most common and recommended approach.

You keep a base docker-compose.yml that defines the shared services (e.g., app, API, etc.) and then create override files for database-specific configuration.

Example file structure:

- docker-compose.yml
- docker-compose.oracle.yml
- docker-compose.postgres.yml


## Base file (docker-compose.yml):

```yml
version: '3.9'
services:
  app:
    build: .
    environment:
      - DB_CONNECTION_STRING=${DB_CONNECTION_STRING}
    depends_on:
      - db
```

## Oracle override (docker-compose.oracle.yml):

```yml
services:
  db:
    image: oracleinanutshell/oracle-xe-11g
    environment:
      - ORACLE_PASSWORD=oracle
    ports:
      - "1521:1521"

  app:
    environment:
      - DB_CONNECTION_STRING=User Id=system;Password=oracle;Data Source=oracle:1521/XE;
```

## Postgres override (docker-compose.postgres.yml):

```yml
services:
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=labdb
    ports:
      - "5432:5432"

  app:
    environment:
      - DB_CONNECTION_STRING=Host=postgres;Port=5432;Database=labdb;Username=postgres;Password=postgres;
```

## Usage

### Start Oracle setup

```bash
docker compose -f docker-compose.yml -f docker-compose.oracle.yml up -d
```

# Start Postgres setup
docker compose -f docker-compose.yml -f docker-compose.postgres.yml up -d


💡 You can also define COMPOSE_FILE in a .env file:

COMPOSE_FILE=docker-compose.yml:docker-compose.oracle.yml


and switch it dynamically by changing that variable.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/docker/how-to-create-a-multi-layer-docker-compose](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/docker/how-to-create-a-multi-layer-docker-compose)
