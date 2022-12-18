
# from tqdm import tqdm
# from time import sleep
 
 
# for i in tqdm(range(20), desc ="Text You Want"):
#     pass


# import sys

# # 👇️ print all built-in module names
# print(sys.builtin_module_names)



# def main_dashboard():
#     print('''
# --   _   _                      _                   _                                                                           _   
# --  | | | |                    | |                 (_)                                                                         | |  
# --  | |_| | ___  _   _ ___  ___| | _____  ___ _ __  _ _ __   __ _   _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
# --  |  _  |/ _ \| | | / __|/ _ \ |/ / _ \/ _ \ '_ \| | '_ \ / _` | | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
# --  | | | | (_) | |_| \__ \  __/   <  __/  __/ |_) | | | | | (_| | | | | | | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
# --  \_| |_/\___/ \__,_|___/\___|_|\_\___|\___| .__/|_|_| |_|\__, | |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
# --                                           | |             __/ |                               __/ |                              
# --                                           |_|            |___/                               |___/                               
# ''')
#     chek_new_user = input("Are you new here? (Y/n): ")
#     if (chek_new_user == "y" or chek_new_user == "Y"):
#         signup()
#     else:
#         print("Log In")
#         get_username = input("Enter username: ")
#         sql_cursor.execute("SELECT name FROM userdetails WHERE username = '{}'".format(get_username))
#         get_detais = sql_cursor.fetchall()
#         for tuple_name in get_detais:
#             for name in tuple_name:
#                 print("Hii {},".format(name))
#         get_password = input("Enter password: ")
#         if(login(get_username,get_password)[0] == True and listedGetDetailsFromUser[-1] == "SA"):
#             s_admin_dashboard()
#         elif(login(get_username,get_password)[0] == True and listedGetDetailsFromUser[-1] == "U"):
#             guest_dashboard()
#         elif(login(get_username,get_password)[0] == True and listedGetDetailsFromUser[-1] == "HK"):
#             hs_kep_dashboard()


l1 = ["1"]

print(bool(l1))