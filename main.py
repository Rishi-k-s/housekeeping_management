
import mysql.connector
# ----------------------------------------
# --------Function starts from here-------
# ----------------------------------------
def login(get_username,get_password):
    sql_cursor.execute("SELECT * FROM FROM")
    
    # have to enter the username and password and the hotel uid when any type of user logs in
    #aftr logged in hav to return sm value
    pass

def signup():
    print("----Signing Up----")
    get_role = input("Choose your role\n(1) Super Admin\n(2) Guest\n-->")
    if(get_role == "1"):
        passCheck = False
        get_username_signup = input("Enter username: ")
        # sql_cursor.execute("SELECT username FROM userdetails WHERE username ='hotel1';")
        "INSERT INTO TABLE userdeails VALUES (UUID(),u1,123,Sreejesh,SA);"
        # print(sql_cursor.fetchall())
        print("Hola {}, lets get you signed in\n".format(get_username_signup))
        get_passwd_signup = input("Enter password: ")
        while passCheck == False:
            get_pass_check = input("Re-enter password: ")
            if(get_passwd_signup == get_pass_check):
                passCheck = True
        if(passCheck ==  True):
            get_Name_user = input("Enter Your Name: ")

    elif(get_role == "2"):
        get_username_signup = input("Enter username: ")
        print("Hola {}, lets get you signed in\n".format(get_username_signup))
        get_passwd_signup = input("Enter password: ")
        get_pass_check = input("Re-enter password: ")
        if(get_passwd_signup == get_pass_check):
            pass
    #if the signup is 


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

# ========================================
# ^^^^^^^^^^^^Functions end^^^^^^^^^^^^^^^
# ________________________________________


# ----------------------------------------
# --------Connecting TO datadase----------
# ----------------------------------------
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

# ========================================
# ^^^^^^^^^^^^Connection end^^^^^^^^^^^^^^

# ----------------------------------------
# -----------User Dashboards--------------
# ----------------------------------------
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
        signup()
    else:
        get_username = input("Enter username: ")
        print("Hii {},".format(get_username))
        get_password = input("Enter password: ")
        login()

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