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


create table userdetails(user_uid VARCHAR(255) PRIMARY KEY,username VARCHAR(255) UNIQUE, password VARCHAR(255) UNIQUE, name VARCHAR(255) NOT NULL,user_role VARCHAR(255) NOT NULL);
# all dashboard screen would be here

def main_dashboard():
    print("Housekeeping Mananagement")
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