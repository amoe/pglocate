# pglocate

It provides a faster version of `locate`.

## Requirements

psycopg2 module: `python3-psycopg2`

Install using `make install`.

Config file is searched for at `/usr/local/etc/pglocate.cf`.

It looks as such:

```
[main]
db_hostname = localhost
db_username = file_indexer
db_password = somepassword
db_database = files
```

Run the DDL (as the same user specified in this file, otherwise the table will
get the wrong ownership).

```
CREATE TABLE files (filename TEXT NOT NULL)
```


You need to create the appropriate index on the database after creating it
yourself.

```
files=# CREATE INDEX filename_trgm_idx ON files USING gin (filename gin_trgm_ops);
CREATE INDEX
files=# \d files
    Table "public.files"
  Column  | Type | Modifiers 
----------+------+-----------
 filename | text | not null
Indexes:
    "filename_trgm_idx" gin (filename gin_trgm_ops)
```

## Caveats

This program assumes that all filenames can be decoded as UTF-8.  Use a separate
program to check your filesystem for valid filenames (`check_filenames.py` from
scriptpool).
