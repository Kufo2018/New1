
#THE CODE BELOW WRITES A PROGRAM THAT SCHEDULES BREAKS
# import webbrowser
# import time
# breaks_used = 0
# break_count = 3
# print("The program started on " + time.ctime())
# while breaks_used < break_count:
#     time.sleep(5)
#     webbrowser.open("https://www.youtube.com/watch?v=-ggGU7sUzlM")
#     breaks_used = breaks_used + 1
#     print("Number of breaks used = " + str(breaks_used))
# else:
#     print("Number of breaks used = " + str(breaks_used) + \n "Break time is over")
#
#
#
#
#
# #webbrowser.open("https://www.youtube.com/watch?v=-ggGU7sUzlM")

#THE PROGRAM BELOW SELECTS LOCATION AND UNSCRAMBLES FILES

import os
def rename_files():
# Get the file names from the folder
    file_list = os.listdir("/home/kuforiji/Downloads/prank/prank")
    print(file_list)
# For each file, rename filename
rename_files()
