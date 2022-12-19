import mysql.connector

def connect_to_database():
    print("Loading...\n\n")
    connector = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "!Kno!#@%[]k",
        database = "housekeepingmngmnt"
    )
    global x
    if(connector.is_connected()):
        print("Database connected")
    else:
        print("Connection falied")


# host = "sql.freedb.tech",
#     username = "freedb_main_user2",
#     password = "GcFhae@3x9j4h5V",
#     database = "freedb_housekeepingmngmnt"
#DBMS connmads
# sql_cursor.execute("CREATE TABLE user_details()") # celar error while creating table

# show_tables = sql_cursor.execute("SHOW TABLES")
# print(show_tables)