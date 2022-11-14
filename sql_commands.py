import mysql.connector

connector = mysql.connector.connect(
    host = "sql.freedb.tech",
    username = "freedb_main_user2",
    password = "GcFhae@3x9j4h5V",
    database = "freedb_housekeepingmngmnt"
)

#SQL cursor
sql_cursor = connector.cursor()

sql_cursor.execute("CREATE TABLE user_details") # celar error while creating table

show_tables = sql_cursor.execute("SHOW TABLES")
print(show_tables)