
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
            listedGetDetailsFromUser = [True,details[0],details[1],details[2],details[3],details[4],details[5]]
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
        #69
        # print(sql_cursor.fetchall())
        get_passwd_signup = input("Enter password: ")
        while passCheck == False:
            get_pass_check = input("Re-enter password: ")
            if(get_passwd_signup == get_pass_check):
                passCheck = True
        if(passCheck ==  True):
            sql_cursor.execute("INSERT INTO userdetails (user_uid,username,password,name,user_role) VALUES (UUID(),'{}','{}','{}','{}');".format(get_username_signup,get_passwd_signup,get_Name_user,setUserRole))
            login()
            
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
            sql_cursor.execute("INSERT INTO userdetails (user_uid,username,password,name,user_role) VALUES (UUID(),'{}','{}','{}','{}');".format(get_username_signup,get_passwd_signup,get_Name_user,setUserRole))
    #if the signup is 


"""
Signup is only for super admin and user
super admins add housekeeers for the place
"""
"""If the signup is as guest then ask for username for each user name should be unique
   if the sign up is as a Housekeeper ask for the same
   but if its as a super admin ask for address, contact info and unique place id
   ?? do we neeed housekeeper user details

"""
# ----------SuperAdmin Functions----------
def addOrRemoveRooms():
    print("(1)Add Room\n(2)Remove Room")
    getChooseRoomFunc = input("-->")
    if(getChooseRoomFunc == "1"):
        print(">>>Creating a new Room<<<")
        getRoomName = input("Enter Room Name: ")
        sql_cursor.execute("INSERT INTO hslocations (hsl_uid,sa_uid,place_name) VALUES (UUID(),'{}','{}');".format(listedGetDetailsFromUser[1],getRoomName))
    elif(getChooseRoomFunc == "2"):
        print("<Deleting Room>")
        getRoomName = input("Enter Room Name: ")
        sql_cursor.execute("DELETE FROM hslocations WHERE place_name='{}';".format(getRoomName))
        print("the Room {} is deleted ".format(getRoomName))

def addOrRemoveHouseKeepers():
    print("(1)Add Housekeeper\n(2)Remove Housekeeper")
    getChooseHkFunc = input("-->")
    if(getChooseHkFunc == "1"):
        print("~ Craete Housekeeper Account(s) ~")
        get_Name_user = input("Enter Housekeeper Name: ")
        print("\nAdding {} as Housekeeper".format(get_Name_user))
        setUserRole = "HK"
        passCheck = False
        isUserPresent = False
        while isUserPresent == False:
            get_username_signup = input("Enter username: ")
            sql_cursor.execute("SELECT username FROM userdetails WHERE username = '{}';".format(get_username_signup))
            get_detais = sql_cursor.fetchall()
            #print("Details: ",get_detais,",",bool(get_detais))
            if(bool(get_detais)==False):
                isUserPresent = True
            else:
                print("Smone is using that username already :/")
                print("Use a different username: ")
        get_passwd_signup = input("Enter password: ")
        while passCheck == False:
            get_pass_check = input("Re-enter password: ")
            if(get_passwd_signup == get_pass_check):
                passCheck = True
        if(passCheck ==  True):
            print()
            print("Assign Room to {}".format(get_Name_user))
            sql_cursor.execute("SELECT place_name FROM hslocations WHERE sa_uid = '{}';".format(listedGetDetailsFromUser[1]))
            allRoomListOfTuple = sql_cursor.fetchall()
            print("--Rooms--")
            for eachRoom in allRoomListOfTuple:
                print(eachRoom[0])
            print("---------")
            sql_cursor.execute("INSERT INTO userdetails VALUES (UUID(),'{}','{}','{}','{}','{}');".format(get_username_signup,get_passwd_signup,get_Name_user,setUserRole,listedGetDetailsFromUser[1]))
            #Adding HK to Specified rooms
            getRoomName = input("Enter Room Name: ")
            sql_cursor.execute("SELECT hsl_uid FROM hslocations WHERE place_name = '{}';".format(getRoomName))
            rawSqlPlaceUid = sql_cursor.fetchall()
            PlaceUid = rawSqlPlaceUid[0][0]
            #get hk uid from user details
            sql_cursor.execute("SELECT user_uid FROM userdetails WHERE username = '{}';".format(get_username_signup))
            rawSqlHkUid = sql_cursor.fetchall()
            hKUid = rawSqlHkUid[0][0]

            #update the housekeeper uid in HK location table
            sql_cursor.execute("UPDATE hslocations SET hk_uid ='{}' WHERE hsl_uid = '{}';".format(hKUid,PlaceUid))

            print("Added Housekeeper Successfully")
    elif(getChooseHkFunc == "2"):
        print("<Deleting Housekeeper>")
        getHKName = input("Enter Housekeeper Name: ")
        sql_cursor.execute("DELETE FROM userdetails WHERE username='{}' AND user_role='{}';".format(getHKName,"HK"))
        print("the user {} is deleted ".format(getHKName))

#------------Guest Dashboard -------------
def giveReviewsGuest():
    print("Give Review\n")
    roomAvailable = False
    while roomAvailable == False:
        try:
            getRoomName = input("Enter Room Name: ")
            sql_cursor.execute("SELECT hk_uid,sa_uid,hsl_uid FROM hslocations WHERE place_name = '{}';".format(getRoomName))
            reviewList = []
            listOfUids = sql_cursor.fetchall()[0]
            for eachUid in listOfUids:
                reviewList.append(eachUid)
            sql_cursor.execute("SELECT NOW()")
            currentDateTime = sql_cursor.fetchall()
            reviewList.append(currentDateTime)
            roomAvailable = True 
        except :
            # print(ValueError)
            print("The entered room is not available")
    # sql_cursor.execute("SELECT sa_uid,hk_uid,place_name,hsl_uid FROM hslocations WHERE place_name = '{}';".format(getRoomName))
    # allRoomListOfTuple = sql_cursor.fetchall()
    # print("--Rooms--")
    # for eachRoom in allRoomListOfTuple:
    #     print(eachRoom[0])
    # print("---------")
    print("TO skip any question press enter")
    getRevRoom = int(input("Was the room clean?(out of 10) : "))
    print()
    getRevMeal = int(input("Enjoyed the meal?(out of 10) : "))
    print()
    getRevHospitality = int(input("Was the staff friendly and helpful?(out of 10) : "))
    print()
    getRevWashroom = int(input("Cleanliness of the restrooms(out of 10) : "))
    print()
    getRevOverall = int(input("Was the staff friendly and helpful?(out of 10) : "))
    print()
    getRevRemarks = input("Review\n(max:250 letters): ")

    reviewList = reviewList+[getRevRoom,getRevMeal,getRevHospitality,getRevWashroom,getRevOverall,getRevRemarks]
    print(reviewList)


#----------Global Func------------------
def viewGuestReviews():
    pass


# ========================================
# ^^^^^^^^^^^^Functions end^^^^^^^^^^^^^^^


# ----------------------------------------
# -----------User Dashboards--------------
# ----------------------------------------

# the guest dashboard
#guest could give review and ratings
def guest_dashboard():
    
    viewGuestDashboard = True
    while viewGuestDashboard:
        print("Guest Dashboard")
        print("(1) Give Reviews\n(2) View Reviews\n(3) exit")
        getMenuInput = input("-->")
        if(getMenuInput == "1"):
            giveReviewsGuest()
        if(getMenuInput == "2"):
            viewGuestReviews()
        elif(getMenuInput == "3"):
            viewGuestDashboard = False

#the housekeeper dashboard
#house keepers should also be able to give reviews
def hs_kep_dashboard():
    print("Housekeeping Dashboard")

#super admin dashboard
# they get the statistics of how the housekeepers perform
#this is also wher they get to create housekeepers
def s_admin_dashboard():
    viewAdminDashboard = True
    while viewAdminDashboard:
        print("Super admin Dashboard")
        print("(1)View All reviews\n(2)Housekeeping reviews\n(3)User Reviews")
        print("(4)Add/Remove/View Housekeeper\n(5)Add/Remove/View Rooms\n(6)Exit\n")
        getMenuInput = input("-->")
        if(getMenuInput == "4"):
            addOrRemoveHouseKeepers()
        if(getMenuInput == "5"):
            addOrRemoveRooms()
        elif(getMenuInput == "6"):
            viewAdminDashboard = False
    # ========================================
# ^^^^^^^^^^^Dashboards end^^^^^^^^^^^^^^^
"""Have to work on reviews"""

# ----------------------------------------
# ---------------MAIN MENU----------------
# ----------------------------------------

print('''
     _   _                      _                   _                                                                           _   
    | | | |                    | |                 (_)                                                                         | |  
    | |_| | ___  _   _ ___  ___| | _____  ___ _ __  _ _ __   __ _   _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
    |  _  |/ _ \| | | / __|/ _ \ |/ / _ \/ _ \ '_ \| | '_ \ / _` | | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
    | | | | (_) | |_| \__ \  __/   <  __/  __/ |_) | | | | | (_| | | | | | | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
    \_| |_/\___/ \__,_|___/\___|_|\_\___|\___| .__/|_|_| |_|\__, | |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
                                             | |             __/ |                               __/ |                              
                                             |_|            |___/                               |___/                               
''')
chek_new_user = input("Are you new here? (Y/n): ")
if (chek_new_user == "y" or chek_new_user == "Y"):
    signup()
else:
    isLoggingIn = True
    while isLoggingIn:
        print("Log In")
        get_username = input("Enter username: ")
        sql_cursor.execute("SELECT name FROM userdetails WHERE username = '{}'".format(get_username))
        get_detais = sql_cursor.fetchall()
        if(bool(get_detais)==False):
            print("This Account doesnt exist, Signup?\n")
            print("(1)Signup\n(2)Login\n(3)Exit")
            getSignUpChoice = input("-->")
            if(getSignUpChoice == "1"):
                signup()
            elif(getSignUpChoice == "3"):
                isLoggingIn = False
        else:
            for tuple_name in get_detais:
                for name in tuple_name:
                    print("Hii {},".format(name))
            get_password = input("Enter password: ")
            check_login = login(get_username,get_password)
            if(check_login[0] == True and check_login[-2] == "SA"):
                isLoggingIn = False
                s_admin_dashboard()
            elif(check_login[0] == True and check_login[-2] == "U"):
                isLoggingIn = False
                guest_dashboard()
            elif(check_login[0] == True and check_login[-2] == "HK"):
                isLoggingIn = False
                hs_kep_dashboard()