import mysql.connector
connector = mysql.connector.connect(
    host = "sql.freedb.tech",
    username = "freedb_main_user2",
    password = "GcFhae@3x9j4h5V",
    database = "freedb_housekeepingmngmnt"
)

#DBMS connmads
sql_cursor = connector.cursor()
sql_cursor.execute("")
if(connector.is_connected()):
    print("Database connected")
else:
    print("Connection falied")

def login():
    get_username = input("Enter username: ")
    get_password = input("Enter password: ")
    
    # have to enter the username and password and the hotel uid when any type of user logs in
    #aftr logged in hav to return sm value
    pass

def signup():
    #if the signup is 
    pass

def make_hs_kep_user():
    # the code for making 
    pass
"""
Signup is only for super admin and user
super admins add housekeeers for the place
"""
"""If the signup is as guest then ask for username and password, each user name should be unique
   if the sign up is as a Housekeeper ask for the same
   but if its as a super admin ask for address, contact info and unique place id
   ?? do we neeed housekeeper user details

"""

