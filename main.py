
import mysql.connector

# ----------------------------------------
# --------Connecting TO datadase----------
# ----------------------------------------
print("Loading...\n")

connector = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "!Kno!#@%[]k",
    database = "housekeepingmngmnt",
    autocommit = True,
)


if(connector.is_connected()):
    print("Database connected")
else:
    print("Connection falied")

sql_cursor = connector.cursor()

# ========================================
# ^^^^^^^^^^^^Connection end^^^^^^^^^^^^^^


# ----------------------------------------
# --------Function starts from here-------
# ----------------------------------------
def login(username,password):
    sql_cursor.execute("SELECT * FROM userdetails WHERE username = '{}'".format(username))
    global listedGetDetailsFromUser
    getDetailsFromUser = sql_cursor.fetchall()
    for details in getDetailsFromUser:
        if(details[2] == password):
            listedGetDetailsFromUser = [True,details[0],details[1],details[2],details[3],details[4]]
            #print([True,details[0],details[1],details[2],details[3],details[4]])
            return(listedGetDetailsFromUser)
    # have to enter the username and password and the hotel uid when any type of user logs in
    #aftr logged in hav to return sm value

def signup():
    print("----Signing Up----")
    get_role = input("Choose your role\n(1) Super Admin\n(2) Guest\n-->")
    # ___________________
    # -------For SA------
    # ___________________
    if(get_role == "1"):
        print("Signing Up as Super Admin")
        get_Name_user = input("Enter Your Name: ")
        print("\nHola {}, lets get you signed in\n".format(get_Name_user))
        setUserRole = "SA"
        passCheck = False
        isUserPresent = False
        while isUserPresent == False:
            get_username_signup = input("Enter username: ")
            sql_cursor.execute("SELECT username FROM userdetails WHERE username = '{}'".format(get_username_signup))
            get_detais = sql_cursor.fetchall()
            #print("Details: ",get_detais,",",bool(get_detais))
            if(bool(get_detais)==False):
                isUserPresent = True
            else:
                print("Smone is using that username already :/")
                print("Use a different username: ")
        # sql_cursor.execute("SELECT username FROM userdetails WHERE username ='hotel1';")
        #"INSERT INTO TABLE userdeails VALUES (UUID(),u1,123,Sreejesh,SA);"
        # print(sql_cursor.fetchall())
        get_passwd_signup = input("Enter password: ")
        while passCheck == False:
            get_pass_check = input("Re-enter password: ")
            if(get_passwd_signup == get_pass_check):
                passCheck = True
        if(passCheck ==  True):
            sql_cursor.execute("INSERT INTO userdetails VALUES (UUID(),'{}','{}','{}','{}');".format(get_username_signup,get_passwd_signup,get_Name_user,setUserRole))
            
    # ___________________
    # -----For USER------
    # ___________________
    elif(get_role == "2"):
        print("Signing Up as Guest")
        get_Name_user = input("Enter Your Name: ")
        print("Hola {}, lets get you signed in\n".format(get_Name_user))
        setUserRole = "U"
        passCheck = False
        isUserPresent = False
        while isUserPresent == False:
            get_username_signup = input("Enter username: ")
            sql_cursor.execute("SELECT username FROM userdetails WHERE username = '{}'".format(get_username_signup))
            get_detais = sql_cursor.fetchall()
            #print("Details: ",get_detais,",",bool(get_detais))
            if(bool(get_detais)==False):
                isUserPresent = True
            else:
                print("Smone is using that username already :/")
                print("Use a different username: ")
        # sql_cursor.execute("SELECT username FROM userdetails WHERE username ='hotel1';")
        #"INSERT INTO TABLE userdeails VALUES (UUID(),u1,123,Sreejesh,SA);"
        # print(sql_cursor.fetchall())
        get_passwd_signup = input("Enter password: ")
        while passCheck == False:
            get_pass_check = input("Re-enter password: ")
            if(get_passwd_signup == get_pass_check):
                passCheck = True
        if(passCheck ==  True):
            sql_cursor.execute("INSERT INTO userdetails VALUES (UUID(),'{}','{}','{}','{}');".format(get_username_signup,get_passwd_signup,get_Name_user,setUserRole))
    #if the signup is 


def make_hs_kep_user():
    # the code for making house keeper
    pass
"""
Signup is only for super admin and user
super admins add housekeeers for the place
"""
"""If the signup is as guest then ask for username for each user name should be unique
   if the sign up is as a Housekeeper ask for the same
   but if its as a super admin ask for address, contact info and unique place id
   ?? do we neeed housekeeper user details

"""

# ========================================
# ^^^^^^^^^^^^Functions end^^^^^^^^^^^^^^^
# ________________________________________


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
        print("Log In")
        get_username = input("Enter username: ")
        sql_cursor.execute("SELECT name FROM userdetails WHERE username = '{}'".format(get_username))
        get_detais = sql_cursor.fetchall()
        for tuple_name in get_detais:
            for name in tuple_name:
                print("Hii {},".format(name))
        get_password = input("Enter password: ")
        if(login(get_username,get_password)[0] == True and listedGetDetailsFromUser[-1] == "SA"):
            s_admin_dashboard()
        elif(login(get_username,get_password)[0] == True and listedGetDetailsFromUser[-1] == "U"):
            guest_dashboard()
        elif(login(get_username,get_password)[0] == True and listedGetDetailsFromUser[-1] == "HK"):
            hs_kep_dashboard()

# the guest dashboard
#guest could give review and ratings
def guest_dashboard():
    print("Guest Dashboard")
    print("(1)View All reviews\n(1)Housekeeping reviews\n(3)User Reviews")
    print("(4)Add/Remove Housekeeper\n(5)Add/Remove Rooms\n(6)Exit\n")

#the housekeeper dashboard
#house keepers should also be able to give reviews
def hs_kep_dashboard():
    print("Housekeeping Dashboard")

#super admin dashboard
# they get the statistics of how the housekeepers perform
#this is also wher they get to create housekeepers
def s_admin_dashboard():
    print("Super admin Dashboard")


main_dashboard()