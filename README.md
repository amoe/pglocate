# pglocate

Config file is searched for at `/usr/local/etc/pglocate.cf`.

It looks as such:

```
[main]
db_hostname = localhost
db_username = file_indexer
db_password = somepassword
db_database = files
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
