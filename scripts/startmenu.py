# importing the module
import os

# sets the text colour to green
os.system("tput setaf 2")

print("Launching Terminal User Interface")

# sets the text color to red
os.system("tput setaf 1")

print("\t\tWELCOME TO Arch start menu\t\t\t")

# sets the text color to white
os.system("tput setaf 7")

print("\t-------------------------------------------------")
print("Entering local device")
while True:
    print("""
        1.Geen scherm verbonden (refresh) 
        2.Verbonden aan Philips op kantoor
        3.Verbonden aan LG 4K Thuis
        4.Verbonden aan LG 4K Thuis, Dual monitor
        5.Config i3
        6.Config polybar
        7.Start X (with i3)
        8.Edit this menu
        9.Exit""")

    ch = int(input("Enter your choice: "))

    if(ch == 1):
        print("System started, welcome")
        os.system("/usr/bin/i3-msg restart")
        exit()

    elif ch == 2:
        os.system("sh ~/scripts/monitor_kantoor.sh")

    elif ch == 3:
        os.system("sh ~/scripts/LG4Konly_home_xrandr.sh")

    elif ch == 4:
        os.system("sh ~/scripts/LG4K_home_xrandr.sh")

    elif ch == 5:
        os.system("vim ~/.i3/config")

    elif ch == 6:
        os.system("vim ~/.config/polybar/config")

    elif ch == 7:
        os.system("startx")

    elif ch == 8:
        os.system("vim ~/scripts/startmenu.py")

    elif ch == 9:
        print("Exiting application")
        exit()
    else:
        print("Invalid entry")

#    input("Press enter to continue")
    os.system("clear")
