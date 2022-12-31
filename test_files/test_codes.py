
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


# l1 = ["1"]

# print(bool(l1))

# demo-ncurses-hello-world.py

import curses
import sys

def main(argv):
  # BEGIN ncurses startup/initialization...
  # Initialize the curses object.
  stdscr = curses.initscr()

  # Do not echo keys back to the client.
  curses.noecho()

  # Non-blocking or cbreak mode... do not wait for Enter key to be pressed.
  curses.cbreak()

  # Turn off blinking cursor
  curses.curs_set(False)

  # Enable color if we can...
  if curses.has_colors():
    curses.start_color()

  # Optional - Enable the keypad. This also decodes multi-byte key sequences
  # stdscr.keypad(True)

  # END ncurses startup/initialization...

#   caughtExceptions = ""
#   try:
#     # Coordinates start from top left, in the format of y, x.
#     stdscr.addstr(0, 0,'''     _   _                      _                   _                                                                           _   
#     | | | |                    | |                 (_)                                                                         | |  
#     | |_| | ___  _   _ ___  ___| | _____  ___ _ __  _ _ __   __ _   _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
#     |  _  |/ _ \| | | / __|/ _ \ |/ / _ \/ _ \ '_ \| | '_ \ / _` | | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
#     | | | | (_) | |_| \__ \  __/   <  __/  __/ |_) | | | | | (_| | | | | | | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
#     \_| |_/\___/ \__,_|___/\___|_|\_\___|\___| .__/|_|_| |_|\__, | |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
#                                              | |             __/ |                               __/ |                              
#                                              |_|            |___/                               |___/                               
# ''')
#     screenDetailText = "This screen is [" + str(curses.LINES) + "] high and [" + str(curses.COLS) + "] across."
#     startingXPos = int ( (curses.COLS - len(screenDetailText))/2 )
#     stdscr.addstr(3, startingXPos, screenDetailText)
#     stdscr.addstr(5, curses.COLS - len("Press a key to quit."), "Press a key to quit.")

#     # Actually draws the text above to the positions specified.
#     stdscr.refresh()

#     # Grabs a value from the keyboard without Enter having to be pressed (see cbreak above)
#     stdscr.getch()
#   except Exception as err:
#    # Just printing from here will not work, as the program is still set to
#    # use ncurses.
#    # print ("Some error [" + str(err) + "] occurred.")
#    caughtExceptions = str(err)

#   # BEGIN ncurses shutdown/deinitialization...
#   # Turn off cbreak mode...
#   curses.nocbreak()

#   # Turn echo back on.
#   curses.echo()

#   # Restore cursor blinking.
#   curses.curs_set(True)

#   # Turn off the keypad...
#   # stdscr.keypad(False)

#   # Restore Terminal to original state.
#   curses.endwin()

#   # END ncurses shutdown/deinitialization...

#   # Display Errors if any happened:
#   if "" != caughtExceptions:
#    print ("Got error(s) [" + caughtExceptions + "]")

# if __name__ == "__main__":
#   main(sys.argv[1:])
# import pandas as pd
# import mysql.connector
# connector = mysql.connector.connect(
#     host = "localhost",
#     username = "root",
#     password = "!Kno!#@%[]k",
#     database = "housekeepingmngmnt",
#     autocommit = True,
# )


# if(connector.is_connected()):
#     print("Database connected")
# else:
#     print("Connection falied")

# sql_cursor = connector.cursor()

# # sql_cursor.execute("SELECT NOW()")
# # getDate = sql_cursor.fetchall()[0][0]
# # print(getDate)
# sql_cursor.execute("SELECT * FROM userdetails;")
# getdect= sql_cursor.fetchall()
# df = pd.read_sql('SELECT * FROM userdetails;', con=connector)
# print(df)

# importing the module
# import pandas as pd
#import numpy
  
# # creating a DataFrame
# dict = {'Name' : ['Martha', 'Tim', 'Rob', 'Georgia'],
#         'Maths' : [87, 91, 97, 95],
#         'Science' : [83, 99, 84, 76]}
# df = pd.DataFrame(dict)
  
# # displaying the DataFrame
# df.style
# print(df)

# import tabulate

# table = [["Sreejesh",7],["BABU",6],["Sui",3]]
# headers = ["Users", "Meal"]
# print(tabulate.tabulate(table, headers, tablefmt="rounded_grid"))

# x = 'a'*5
# print(x)
# y = [x[a] for a,b in enumerate(x) if a%2==0]
# print(y)
# z = len(y)
# print(z)

# # define a function to calculate the golden ratio
# def golden_ratio(n):
#   return (1 + (5 ** 0.5)) / 2

# # calculate the golden ratio
# ratio = golden_ratio(5)

# # print the golden ratio
# print(ratio)

a = "2222"
f = ["Year ,0,2 at All the best"]
a = a.split("2")
print(a)
b = a[0] + ". " +a[1] +". "+a[3]
print(b)
