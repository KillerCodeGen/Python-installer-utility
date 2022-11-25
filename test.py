#Python file used for testing code snippets
import requests
import os

URL = "https://gigenet.dl.sourceforge.net/project/mingw/Installer/mingw-get-setup.exe"

response = requests.get(URL)

open("mingw.exe", "wb").write(response.content)

os.system("mingw.exe")