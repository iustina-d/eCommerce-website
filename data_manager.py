from psycopg2._psycopg import cursor
from psycopg2.extras import RealDictCursor
import database_common

@database_common.connection_handler
def get_books(cursor):
    cursor.execute("SELECT * FROM books ORDER BY book_name;")
    return cursor.fetchall()
