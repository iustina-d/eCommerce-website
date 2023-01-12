from psycopg2._psycopg import cursor
from psycopg2.extras import RealDictCursor
import database_common

@database_common.connection_handler
def get_first_6_books(cursor):
    cursor.execute("SELECT * FROM books ORDER BY book_name,author_name LIMIT 6;")
    return cursor.fetchall()


@database_common.connection_handler
def get_books_on_page(cursor,page):
    cursor.execute(f"SELECT * FROM books ORDER BY book_name,author_name OFFSET {page} ROWS LIMIT 6;"
    )
    return cursor.fetchall()

@database_common.connection_handler
def get_books_using_search_box(cursor,text):
    cursor.execute("SELECT * FROM books WHERE book_name ILIKE %(text)s OR author_name ILIKE %(text)s LIMIT 6;",
    {"text":f"%{text}%"})
    return cursor.fetchall()

