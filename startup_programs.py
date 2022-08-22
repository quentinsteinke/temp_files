import os
import time

discord = "C:\\Users\\Quentin Steinke\\AppData\\Local\\Discord\\app-1.0.9006\\Discord.exe"
outlook = "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
teams = "C:\\Users\\Quentin Steinke\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
code = "code"
blender = "blender"

# Progams
programs = [
    discord,
    teams,
    outlook,
    #code,
    chrome,
    blender,
    ]

# Launching programs one by one
for pro in programs:
    if pro == teams:
        os.system('"' + pro + '"')
        time.sleep(2)
    else:
        os.system('"' + pro + '"')
        time.sleep(2)
#    print("start " + pro)
