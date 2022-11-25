import argparse
import time
import os
import installer_functions

prog_name = "WIP Program"

parser = argparse.ArgumentParser(description='A simple python tool to install tools that all developers should/need to use')

parser.add_argument('install_type', help='Choose an install type, developer tools, language compilers and interpreters, linux commands on windows, or all(More install modes to come)')

args = parser.parse_args()

#print(args.install_type)

if os.name == "nt":
    if args.install_type == "developer tools":
        installer_functions.do_nt_install("dev_tools")
    elif args.install_type == "language compilers and interpreters":
        installer_functions.do_nt_install("lcai")
    elif args.install_type == "linux commands on windows":
        installer_functions.do_nt_install("lcow")
    elif args.install_type == "all":
        installer_functions.do_nt_install("all")
    else:
        print("Not a valid install type, please run " + prog_name + " -h for more information")
else:
    print("Only works on windows for now, linux support coming soon, never will come to mac os.")