from multiprocessing.sharedctypes import synchronized
from computer import Computer
from parser import Parser
from saver import Saver
from state_synchronization import StateSynchronization

def main():
    PC = []
    while True:
        print('Что делаем?')
        
        print('1 - Добавить компьютер.')

        print('2 - Включить компьютер.')
        print('3 - Выключить компьютер.')
        print('4 - Включен ли компьютер.')

        print('5 - Вывесит имя компьютера.')

        print('6 - Добавить пользователя.')
        print('7 - Удалить пользователя.')
        print('8 - Сменить пользователя.')

        print('9 - Ввести команду для пользователя в системе.')

        print('10 - Свободное месте в харнилище.')

        print('11 - Сохранить состояние системы.')
        print('12 - Загрузить последнее сохраненное состояние.')
        print('13 - Выйти из системы')


        choice = int(input())
        if choice == 1:
            comp_data = []
            print('\nРазмер хранилища : ',end='')
            comp_data.append(int(input()))
            print('Имя компьютера : ',end='')
            comp_data.append(input())
            print('Имя первого пользователя : ',end='')
            comp_data.append(input())
            print('Пароль первого пользователя : ',end='')
            comp_data.append(input())
            print('Операционная система первого пользователя : ',end='')
            comp_data.append(input())
            PC.append(Computer(comp_data[0],comp_data[1],comp_data[2],comp_data[3],comp_data[4]))
            print()
        elif choice == 2:
            if PC[0].get_power_status()==False:
                PC[0].turn_computer_power_status()
            else:
                print('\nУже включен\n')
        elif choice == 3:
            if PC[0].get_power_status()==True:
                PC[0].turn_computer_power_status()
            else:
                print('\nУже выключен\n')
        elif choice == 4:
            print(PC[0].get_power_status())
        elif choice == 5:
            print(PC[0].get_computer_name())
        elif choice == 6:
            comp_data = []
            print('\nИмя пользователя :',end='')
            comp_data.append(input())
            print('\nПароль пользователя',end='')
            comp_data.append(input())
            print('\nОперационная система пользователя',end='')
            comp_data.append(input())
            PC[0].add_user(comp_data[0],comp_data[1],comp_data[2])
        elif choice == 7:
            PC[0].del_user()
        elif choice == 8:
            PC[0].change_logged_user()
        elif choice == 9:
            print('\nВведите команду : ')
            PC[0].enter_command()
        elif choice == 10:
            print('\nFree space : '+str(PC[0].free_user_memory()))
        elif choice == 11:
            Saver(PC[0])
        elif choice == 12:
            sync = StateSynchronization('/home/siarhei/Programming/IIT/Univer/ППвИС/Computers_data')
            PC.append(sync.upload_state())
        elif choice == 13:
            break

main()