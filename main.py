import sys


try:
    from cryptography.fernet import Fernet
except:
    print('please install cryptography with this command : pip install cryptography')
    sys.exit(0)

try:
    from colorama import Fore
except:
    print('please install cryptography with this command : pip install colorama')
    sys.exit(0)
try:
    from win10toast import ToastNotifier
except:
    print('please install cryptography with this command : pip install win10toast')
    sys.exit(0)

try:
    import requests
except:
    print('please install cryptography with this command : pip install win10toast')
    sys.exit(0)

try:
    import win32api
except:
    print('please install cryptography with this command : pip install pywin32')
    sys.exit(0)

try:
    import elevate
except:
    print('please install cryptography with this command : pip install elevate')
    sys.exit(0)

from menu import main_menu

main_menu()
