import click
import sys
import os
from Lab1.saver import Saver
from models.computer import Computer
from click_shell import shell


@shell(prompt='> ', intro='Launching CLI application...')
@click.option(
    '--use-save',
    default=False,
    help="Set this parameter as 'True' to upload previous session, otherwise 'False'."
)
@click.option(
    '--disable-console',
    default=False,
    help="Set parameter as 'True' to disable console logging, otherwise 'False'."
)
@click.option(
    '--disable-file',
    default=False,
    help="Set this parameter as 'True' to disable file logging, otherwise 'False'."
)
@click.option(
    '--interface-type',
    default='CLI',
    help="Sets type of interface that application will use. Possible parameters are GUI and CLI."
)

def app(use_save, disable_console, disable_file, interface_type):
    pass


def run_cli_interface(model: Computer):
    global computer
    computer = model
    app()


@app.command(help='Print computer info.', name='print-info')
def print_info():
    info = ''
    info += 'Computer name : ' + computer.get_computer_name() + '\n'
    info += 'Logger user. Login - ' + str(computer.get_logged_user().get_all_user_info()[0]) + '; System - ' + str(computer.get_logged_user().get_all_user_info()[2]) + '\n'
    info += 'Computer power status : ' + str(computer.get_power_status()) + '\n'
    print(info)


@app.command(help='ON computer', name='on-computer')
def on_computer():
    if computer.comp_power_status is False:
        computer.turn_computer_power_status()
        print('Computer is ON')
    else:
        print('Already enabled')

@app.command(help='ON computer', name='off-computer')
def off_computer():
    if computer.comp_power_status:
        computer.turn_computer_power_status()
        print('Computer is OFF')
    else:
        print('Already off')

@app.command(help='Change user', name='change-user')
def change_user():
    print('Enter User information : \nLogin - ', end='')
    login = input()
    print('Password - ', end='')
    password = input()
    computer.change_logged_user(login, password)


@app.command(help='Add user', name='add-user')
def add_user():
    login, password, system = None, None, None
    print('Enter new user info : ')
    print('Login - ', end='')
    login = input()
    print('Passowrd - ', end='')
    password = input()
    print('System - ', end='')
    system = input()
    computer.add_user(login, password, system)


@app.command(help='Delete user', name='del-user')
def del_user():
    print('Input user info.\nLogin - ', end='')
    login = input()
    print('Passowrd - ', end='')
    password = input()
    computer.del_user(login, password)


@app.command(help='Enter a command', name='command')
def enter_command():
    print('Command : ', end='')
    computer.enter_command(input())


@app.command(help='Save system state', name='save')
def save_state():
    save = Saver(computer)
    save.save_state(computer)

@app.command(help='Exit', name='exit')
def exit():
    os._exit(0)
