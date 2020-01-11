import psycopg2
import configparser
import sys

search_substring = sys.argv[1]


cfg = configparser.ConfigParser()
cfg.read("/usr/local/etc/pglocate.cf")

db_hostname = cfg.get('main', 'db_hostname')
db_username = cfg.get('main', 'db_username')
db_password = cfg.get('main', 'db_password')
db_database = cfg.get('main', 'db_database')


conn = psycopg2.connect(
    host=db_hostname, dbname=db_database, user=db_username, password=db_password
)
cur = conn.cursor()

QUERY_TEMPLATE = "SELECT filename FROM files WHERE filename ILIKE '%{}%'"
real_query = QUERY_TEMPLATE.format(search_substring)

cur.execute(real_query)

result = cur.fetchall()

for f in result:
    print(f[0])

