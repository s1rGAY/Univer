import click
import console
import os
from sys import exit
from models.computer import Computer
from utility.logger import Logger
from utility.restore import RestoreService
from utility.snapshot import SnapshotService
from gui import run_gui_interface

os.environ["KIVY_NO_ARGS"] = "1"

Logger.setup()


# настрока CLI
@click.command()
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

def main(use_save, disable_console, disable_file, interface_type='gui'):
    # настройка логгера и сервисов
    interface_type = 'gui'
    # трогать не надо
    logger = Logger(disable_console, disable_file)  # что делает логер ? (машины нет)
    snapshot_service: SnapshotService = SnapshotService()  # сэйвер ?(создает в себе модел машины)
    restore_service: RestoreService = RestoreService()  # держ в себе параметры сейва?

    if use_save:
        computer = restore_service.restore_computer(logger)  # востановление системы ?
        if computer is None:
            computer = Computer(logger)  # Создание новой машины
    else:
        computer = Computer(logger = logger)  # если не юзаем сэйв => создаем по дефолтам? ПЕРЕСОБРАТЬ COMPUTER

    # начать отслеживать новый или уже созданный автомобиль
    # юзает обсервер в себе
    computer.subscribe(snapshot_service)

    if interface_type.lower() == 'gui':
        run_gui_interface(computer, logger)
    elif interface_type.lower() == 'cli':
        console.run_cli_interface(computer)
    else:
        print('Unavailable format.')
        exit()


if __name__ == '__main__':
    main()
