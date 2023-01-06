
import mysql.connector
import tabulate
import time
# ----------------------------------------
# --------Connecting TO datadase----------
# ----------------------------------------
print("Loading...\n")
time.sleep(0.5)
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
time.sleep(0.5)
# ========================================
# ^^^^^^^^^^^^Connection end^^^^^^^^^^^^^^


# ----------------------------------------
# --------Functions starts from here------
# ----------------------------------------

#---------Login and SignUp----------------

def login(username,password):
    global listedGetDetailsFromUser #<< Details of the Current user
    #^ this returns a list in form [bool of login, user uid, usrname,password,name,role]
    sql_cursor.execute("SELECT * FROM userdetails WHERE username = '{}'".format(username))
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
def addRemoveViewRooms():
    print("(1)Add Room\n(2)Remove Room\n(3)View Rooms")
    getChooseRoomFunc = input("-->")
    if(getChooseRoomFunc == "1"):
        print(">>>Creating a new Room<<<")  
        isName = False
        while isName == False:
            try:
                getRoomName = input("Enter Room Username: ")
                sql_cursor.execute("INSERT INTO hslocations (hsl_uid,sa_uid,place_name) VALUES (UUID(),'{}','{}');".format(listedGetDetailsFromUser[1],getRoomName))
                time.sleep(0.6)
                print("\nRoom Added\n")
                isName = True
                time.sleep(0.6)
            except:
                print("The name is taken")
    elif(getChooseRoomFunc == "2"):
        print("<Deleting Room>")
        getRoomName = input("Enter Room Name: ")
        sql_cursor.execute("DELETE FROM hslocations WHERE place_name='{}';".format(getRoomName))
        print("the Room {} is deleted \n".format(getRoomName))
        time.sleep(1.5)
    elif(getChooseRoomFunc == "3"):
        sql_cursor.execute("SELECT place_name FROM hslocations WHERE sa_uid = '{}';".format(listedGetDetailsFromUser[1]))
        allRoomListOfTuple = sql_cursor.fetchall()
        print("--Rooms--")
        for eachRoom in allRoomListOfTuple:
            print(eachRoom[0])
        print("---------")
        time.sleep(0.5)

def addRemoveViewHouseKeepers():
    print("(1)Add Housekeeper\n(2)Remove Housekeeper\n(3)View Housekeepers")
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
            time.sleep(0.5)
            print("Added Housekeeper Successfully")
            time.sleep(0.5)
            print()
    elif(getChooseHkFunc == "2"):
        print("<Deleting Housekeeper>")
        getHKName = input("Enter Housekeeper Username: ")
        print()
        sql_cursor.execute("DELETE FROM userdetails WHERE username='{}' AND user_role='{}';".format(getHKName,"HK"))
        time.sleep(0.4)
        print("❎ the user {} is deleted ".format(getHKName))
        time.sleep(0.5)
        print()
    elif(getChooseHkFunc == "3"):
        namePlaceList = []
        sql_cursor.execute("SELECT userdetails.name,hslocations.place_name FROM userdetails INNER JOIN hslocations ON userdetails.user_uid =hslocations.hk_uid WHERE userdetails.sa_uid = '{}';".format(listedGetDetailsFromUser[1]))
        getNamePlaceNameFromDB = sql_cursor.fetchall()
        for eachNamePlaceFromDB in getNamePlaceNameFromDB:
            namePlaceList.append(eachNamePlaceFromDB)
        headers = ["Housekeeper Name","Room Currently on"]
        time.sleep(0.5)
        print(tabulate.tabulate(namePlaceList, headers, tablefmt="rounded_grid"))
        time.sleep(0.6)
def viewAdminReviews():
    #so the sa can choose which type of rev they want avg, only the overall or the remars or  full
    multipleAvgRevList = []
    print("Reviews")
    print("[1] Average\n[2] Remarks\n[3] Full Review\n[Press any other key to exit]")
    getTypeReview = input("Enter what kindda rev ya want?\n-->")
    if(getTypeReview == "1"):
        print("Showing the average data")
        sql_cursor.execute("SELECT AVG(room),AVG(meal),AVG(hospitality),AVG(washroom),AVG(overall) FROM reviews;")
        rawAvgRevDataSql = sql_cursor.fetchall()
        if(bool(rawAvgRevDataSql) == False):
            print("Guests Havnt done any reviews :/\n")
        for eachAvgReview in rawAvgRevDataSql:
            multipleAvgRevList.append(eachAvgReview)#Append as a list of tuple
        #print(multipleAvgRevList)
        headers = ["Room facilities","Meal","Friendliness","washroom","overall"]
        print(tabulate.tabulate(multipleAvgRevList, headers, tablefmt="rounded_grid"))
    elif(getTypeReview == "2"):
        multipleRemarks =[]
        print("Remarks")
        # sql_cursor.execute("SELECT user_uid,remarks FROM reviews;")
        # rawRemarkRevDataSql = sql_cursor.fetchall()
        # sql_cursor.execute("SELECT user_uid,remarks FROM reviews;")
        sql_cursor.execute("SELECT reviews.user_uid,userdetails.username,reviews.remarks FROM reviews INNER JOIN userdetails ON reviews.user_uid=userdetails.user_uid;")
        rawRemarkRevDataSql = sql_cursor.fetchall()
        if(bool(rawRemarkRevDataSql) == False):
            print("Guests Havnt done any reviews :/\n")
        for eachAvgReview in rawRemarkRevDataSql:
            multipleRemarks.append((eachAvgReview[1],eachAvgReview[2]))#Append as a list of tuple
        #print(multipleRemarks)
        headers = ["Guest","remarks"]
        print(tabulate.tabulate(multipleRemarks, headers, tablefmt="rounded_grid"))
    elif(getTypeReview == "3"):
        fullReviewFromDB = []
        sql_cursor.execute(
            "SELECT userdetails.name,reviews.dateAndTime,reviews.room,reviews.meal,reviews.hospitality,reviews.washroom,reviews.overall,reviews.remarks  FROM reviews  INNER JOIN userdetails ON reviews.user_uid = userdetails.user_uid WHERE reviews.sa_uid = '{}';".format(listedGetDetailsFromUser[1])
            )
        rawGuestDataSql = sql_cursor.fetchall()
        if(bool(rawGuestDataSql) == False):
            print("You Havnt done any reviews\n")
            print("Do some reviews to show up here")
        for eachReview in rawGuestDataSql:
            fullReviewFromDB.append(eachReview)#Append as a list of tuple
        #print(fullReviewFromDB)
        headers = ['User','Date and time',"Room facilities","Meal","Friendliness","washroom","overall","remarks"]
        print(tabulate.tabulate(fullReviewFromDB, headers, tablefmt="rounded_grid"))

#------------Guest Functions -------------
def giveReviewsGuest():
    print("Give Review\n")
    roomAvailable = False
    while roomAvailable == False:
        try:
            getRoomName = input("Enter Room Name: ")
            userUid = listedGetDetailsFromUser[1]
            sql_cursor.execute("SELECT hk_uid,sa_uid,hsl_uid FROM hslocations WHERE place_name = '{}';".format(getRoomName))
            reviewList = []
            listOfUids = sql_cursor.fetchall()[0]
            for eachUid in listOfUids:
                reviewList.append(eachUid)
            reviewList.append(userUid)
            sql_cursor.execute("SELECT NOW()")
            currentDateTime = sql_cursor.fetchall()[0][0]
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
    getRevOverall = int(input("overall impression?(out of 10) : "))
    print()
    getRevRemarks = input("Review\n(max:250 letters): ")

    reviewList = reviewList+[getRevRoom,getRevMeal,getRevHospitality,getRevWashroom,getRevOverall,getRevRemarks]
    # print(reviewList)
    sql_cursor.execute(
        "INSERT INTO reviews VALUES (UUID(),'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') ;"
        .format(
            reviewList[0],reviewList[1],reviewList[2],reviewList[3],
            reviewList[4],reviewList[5],reviewList[6],reviewList[7],
            reviewList[8],reviewList[9],reviewList[10]
            )
    )
    print("✨ Review given successfully")
    
def viewGuestReviews():
    multipleRevList = []
    print("Previous Reviews")
    sql_cursor.execute(
        "SELECT dateAndTime,room,meal,hospitality,washroom,overall,remarks FROM reviews WHERE user_uid = '{}';".format(listedGetDetailsFromUser[1])
        )
    rawGuestDataSql = sql_cursor.fetchall()
    if(bool(rawGuestDataSql) == False):
        print("You Havnt done any reviews\n")
        print("Do some reviews to show up here")
    for eachReview in rawGuestDataSql:
        multipleRevList.append(eachReview)#Append as a list of tuple
    #print(multipleRevList)
    headers = ['Date and time',"Room facilities","Meal","Friendliness","washroom","overall","remarks"]
    print(tabulate.tabulate(multipleRevList, headers, tablefmt="rounded_grid"))
        


#----------Global Func------------------



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
            sql_cursor.close()
            connector.close()

#the housekeeper dashboard
#house keepers should also be able to give reviews
def hs_kep_dashboard():
    viewHkDashboard = True
    while viewHkDashboard:
        print("Housekeeping Dashboard")
        print("(1)Remarks\n(2)View Full Reviews\n(3)View Assigned Room\n[Press any other key to exit]\n")
        getHkMenuStuff = input("Enter your selction\n-->")
        if(getHkMenuStuff == "1"):
            multipleRemarks =[]
            print("Remarks")
            sql_cursor.execute("SELECT reviews.user_uid,userdetails.username,reviews.remarks FROM reviews INNER JOIN userdetails ON reviews.user_uid=userdetails.user_uid WHERE reviews.hk_uid = '{}';".format(listedGetDetailsFromUser[1]))
            rawRemarkRevDataSql = sql_cursor.fetchall()
            if(bool(rawRemarkRevDataSql) == False):
                print("Guests Havnt done any reviews :/\n")
            for eachAvgReview in rawRemarkRevDataSql:
                multipleRemarks.append((eachAvgReview[1],eachAvgReview[2]))#Append as a list of tuple
            #print(multipleRemarks)
            headers = ["Guest","remarks"]
            print(tabulate.tabulate(multipleRemarks, headers, tablefmt="rounded_grid"))
        elif(getHkMenuStuff == "2"):
            fullReviewFromDB = []
            sql_cursor.execute(
                "SELECT userdetails.name,reviews.dateAndTime,reviews.room,reviews.meal,reviews.hospitality,reviews.washroom,reviews.overall,reviews.remarks  FROM reviews  INNER JOIN userdetails ON reviews.user_uid = userdetails.user_uid WHERE reviews.hk_uid = '{}';".format(listedGetDetailsFromUser[1])
                )
            rawGuestDataSql = sql_cursor.fetchall()
            if(bool(rawGuestDataSql) == False):
                print("You Havnt done any reviews\n")
                print("Do some reviews to show up here")
            for eachReview in rawGuestDataSql:
                fullReviewFromDB.append(eachReview)#Append as a list of tuple
            #print(fullReviewFromDB)
            headers = ['User','Date and time',"Room facilities","Meal","Friendliness","washroom","overall","remarks"]
            print(tabulate.tabulate(fullReviewFromDB, headers, tablefmt="rounded_grid"))
        elif(getHkMenuStuff == "3"):
            sql_cursor.execute("SELECT place_name FROM hslocations WHERE hk_uid = '{}';".format(listedGetDetailsFromUser[1]))
            getRoomNameFromDB = sql_cursor.fetchall()[0][0]
            print("---Your assigned Room is----")
            print(getRoomNameFromDB)
            print("----------------------------")
            
        else:
            viewHkDashboard = False
#super admin dashboard
# they get the statistics of how the housekeepers perform
#this is also wher they get to create housekeepers
def s_admin_dashboard():
    viewAdminDashboard = True
    while viewAdminDashboard:
        print("Super admin Dashboard")
        print("(1)View All reviews")
        print("(2)Add/Remove/View Housekeeper\n(3)Add/Remove/View Rooms\n(4)Exit\n")
        getMenuInput = input("-->")
        if(getMenuInput == "1"):
            viewAdminReviews()
        elif(getMenuInput == "2"):
            addRemoveViewHouseKeepers()
        elif(getMenuInput == "3"):
            addRemoveViewRooms()
        elif(getMenuInput == "4"):
            sql_cursor.close()
            connector.close()
            viewAdminDashboard = False
# ========================================
# ^^^^^^^^^^^Dashboards end^^^^^^^^^^^^^^^
"""Have to work on reviews"""

# ----------------------------------------
# ---------------MAIN MENU----------------
# ----------------------------------------

print('''
   _____                 _     _____            _               
  / ____|               | |   |  __ \          (_)              
 | |  __ _   _  ___  ___| |_  | |__) |_____   ___  _____      __
 | | |_ | | | |/ _ \/ __| __| |  _  // _ \ \ / / |/ _ \ \ /\ / /
 | |__| | |_| |  __/\__ \ |_  | | \ \  __/\ V /| |  __/\ V  V / 
  \_____|\__,_|\___||___/\__| |_|  \_\___| \_/ |_|\___| \_/\_/  
  __  __                                                   _    
 |  \/  |                                                 | |   
 | \  / | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_  
 | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __| 
 | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_  
 |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__| 
                            __/ |                               
                           |___/                                
''')
time.sleep(0.5)
#General Purpouse Software??
chek_new_user = input("Are you new here? (Y/n): ")
time.sleep(0.2)
if (chek_new_user == "y" or chek_new_user == "Y"):
    signup()
else:
    isLoggingIn = True
    while isLoggingIn:
        print("🔑 Log In\n")
        get_username = input("📄 Enter username: ")
        sql_cursor.execute("SELECT name FROM userdetails WHERE username = '{}'".format(get_username))
        get_detais = sql_cursor.fetchall()
        if(bool(get_detais)==False):
            print("This Account doesnt exist, Signup?\n")
            print("(1)Signup\n(2)Login\n(3)Exit\n")
            getSignUpChoice = input("-->")
            if(getSignUpChoice == "1"):
                signup()
            elif(getSignUpChoice == "3"):
                isLoggingIn = False
        else:
            for tuple_name in get_detais:
                for name in tuple_name:
                    print("Hii {},".format(name))
            get_password = input("🔒 Enter password: ")
            check_login = login(get_username,get_password)
            #print(check_login)
            if(check_login[0] == True and check_login[-2] == "SA"):
                isLoggingIn = False
                s_admin_dashboard()
            elif(check_login[0] == True and check_login[-2] == "U"):
                isLoggingIn = False
                guest_dashboard()
            elif(check_login[0] == True and check_login[-2] == "HK"):
                isLoggingIn = False
                hs_kep_dashboard()