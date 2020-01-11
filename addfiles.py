import psycopg2
import psycopg2.extras
import sys
import os

# No primary key as we do not want a btree index to be created.

DDL = """
CREATE TABLE files (filename TEXT NOT NULL)
"""


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

cur.execute('TRUNCATE files')
conn.commit()

DEFAULT_ROOT = '/'

INSERT_QUERY = """
INSERT INTO files (filename) VALUES %s
"""

interval = 1000

class PathsInserter:
    def __init__(self):
        self.insert_buffer = []
        self.counter = 0

    def run(self, root):
        for root, dirs, files in os.walk(root):
            for file_ in files:
                full_path = os.path.join(root, file_)
                self.insert_buffer.append((full_path,))
                self.counter += 1

                if self.counter % interval == 0:
                    self.flush_buffer()
                    print(self.counter)

        self.flush_buffer()

    def flush_buffer(self):
        psycopg2.extras.execute_values(
            cur, INSERT_QUERY, self.insert_buffer, template=None, page_size=interval
        )
        conn.commit()
        self.insert_buffer = []


obj = PathsInserter()
obj.run(DEFAULT_ROOT)
