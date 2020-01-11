files=# CREATE INDEX filename_trgm_idx ON files USING gin (filename gin_trgm_ops);
CREATE INDEX
files=# \d files
    Table "public.files"
  Column  | Type | Modifiers 
----------+------+-----------
 filename | text | not null
Indexes:
    "filename_trgm_idx" gin (filename gin_trgm_ops)

[main]
db_hostname = localhost
db_username = file_indexer
db_password = somepassword
db_database = files
