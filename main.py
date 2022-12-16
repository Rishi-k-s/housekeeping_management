import credential_screens
import mysql

print("Loading...\n")

connector = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "!Kno!#@%[]k",
    database = "housekeepingmngmnt"
)


if(connector.is_connected()):
    print("Database connected")
else:
    print("Connection falied")
sql_cursor = connector.cursor()
sql_cursor.execute("")




def main_dashboard():
    print('''
--   _   _                      _                   _                                                                           _   
--  | | | |                    | |                 (_)                                                                         | |  
--  | |_| | ___  _   _ ___  ___| | _____  ___ _ __  _ _ __   __ _   _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
--  |  _  |/ _ \| | | / __|/ _ \ |/ / _ \/ _ \ '_ \| | '_ \ / _` | | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
--  | | | | (_) | |_| \__ \  __/   <  __/  __/ |_) | | | | | (_| | | | | | | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
--  \_| |_/\___/ \__,_|___/\___|_|\_\___|\___| .__/|_|_| |_|\__, | |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
--                                           | |             __/ |                               __/ |                              
--                                           |_|            |___/                               |___/                               
''')
    chek_new_user = input("Are you new here? (Y/n): ")
    if (chek_new_user == "y" or chek_new_user == "Y"):
        credential_screens.signup()
    else:
        get_username = input("Enter username: ")
        print("Hii {},".format(get_username))
        get_password = input("Enter password: ")
        credential_screens.login()

# the guest dashboard
#guest could give review and ratings
def guest_dashboard():
    pass

#the housekeeper dashboard
#house keepers should also be able to give reviews
def hs_kep_dashboard():
    pass

#super admin dashboard
# they get the statistics of how the housekeepers perform
#this is also wher they get to create housekeepers
def s_admin_dashboard():
    pass


main_dashboard()