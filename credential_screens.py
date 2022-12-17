import main


# sql_cursor = main.connector.cursor()
# sql_cursor.execute("SELECT username FROM userdetails WHERE username ='hotel1';")
class credentials:
    def login(get_username,get_password):
        sql_cursor.execute("SELECT * FROM FROM")
        
        # have to enter the username and password and the hotel uid when any type of user logs in
        #aftr logged in hav to return sm value
        pass

    def signup():
        print("----Signing Up----")
        get_role = input("Choose your role\n(1) Super Admin\n(2) Guest")
        if(get_role == "1"):
            get_username_signup = input("Enter username: ")
            # sql_cursor.execute("SELECT username FROM userdetails WHERE username ='hotel1';")
            # print(sql_cursor.fetchall())
            print("Hola {}, lets get you signed in\n".format(get_username_signup))
            get_passwd_signup = input("Enter password: ")
            get_pass_check = input("Re-enter password: ")

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

