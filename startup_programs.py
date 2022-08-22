import os

discord = R"'C:\Users\Quentin Steinke\AppData\Local\Discord\app-1.0.9006\Discord.exe'"
outlook = R"'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE'"
teams = R"'C:\Users\Quentin Steinke\AppData\Local\Microsoft\Teams\current\Teams.exe'"
chrome = R"'C:\Program Files\Google\Chrome\Application\chrome.exe'"
code = "code"
blender = "blender"

# Progams
programs = [
    #blender,
    discord,
    #code,
    #outlook,
    #teams,
    #chrome,
    ]

# Launching programs one by one
for pro in programs:
    os.system("start " + pro)
#    print("start " + pro)
