import os
import sys
import signal
import time
import requests

mingw_url = "https://gigenet.dl.sourceforge.net/project/mingw/Installer/mingw-get-setup.exe"

def do_nt_install(mode):
    con = input("WARNING! Everything will install to the C: drive, are you sure you want to continue (Y/n)? ")
    
    if con == "N" or con == "n":
        print("Aborting...")
        sys.exit()
    elif con == "Y" or con == "y":
        code_editor = input("What is your preferred code editor: VSCode, Sublime, or Atom? ")
        if mode == "all" or mode == "All":
            nt_install_all(code_editor)
        

def nt_install_all(editor):
    if editor == "Atom" or editor == "atom":
            os.system("cls")
            print("Installing Atom")
            #Install atom
            os.system("winget uninstall -e --id GitHub.Atom")
            
            #Install the JetBrains suite
            os.system("cls")
            print("Installing JetBrains suite")
            os.system("winget uninstall -e --id JetBrains.PyCharm.Community")
            os.system("winget install -e --id JetBrains.IntelliJIDEA.Community")
            os.system("winget install -e --id JetBrains.PHPStorm")
            os.system("winget install -e --id JetBrains.Rider")
            os.system("winget install -e --id JetBrains.RubyMine")
            os.system("winget install -e --id JetBrains.WebStorm")
            os.system("winget install -e --id JetBrains.GoLand")
            
            #Install Docker
            os.system("cls")
            print("Installing docker")
            os.system("winget uninstall -e --id Docker.DockerDesktop")
            
            #Install programming language interpreters and compiles(MinGW requires manual install, dialog will automatically open)
            os.system("cls")
            print("Installing interpreters and compilers(MinGW requires manual install, dialog will automatically open)")
            time.sleep(2)
            #Gets exe data
            response = requests.get(mingw_url)
            #Creates the exe file
            open("mingw.exe", "wb").write(response.content)
            #Runs the exe
            os.system("mingw.exe")
            
    else:
        print("No valid option provided")
        sys.exit()
     
def ctrl_c_handler(signal, frame):
    print("Aborting installation process...")
    os.system("del mingw.exe")
    sys.exit(0)
signal.signal(signal.SIGINT, ctrl_c_handler)