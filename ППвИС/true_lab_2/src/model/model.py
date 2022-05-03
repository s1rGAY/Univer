#+- Done
import re
import sys
from datetime import datetime


from utility.parsers.reader import XmlReader
from utility.parsers.writer import XmlWriter


#import utility.abstractions.observable as Observable
#import utility.abstractions.observer as Observer

class ModelComponent():
    _not_filtered = []

    def __init__(self, table):
        self.table = table

    #НЕ ПРОВЕРЯЛ, но по идее остаётся без изменений
    def read_data(self, path):
        try:
            handler = XmlReader()
            handler.parser.setContentHandler(handler)
            handler.parser.parse('src/data/' + path)

            for data in handler.table_data:
                self.add_new_student(data)
        except Exception as e:
            print(e)
            pass

    #НЕ ПРОВЕРЯЛ, но по идее остаётся без изменений
    @staticmethod
    def create_empty_file(path):
        try:
            with open(path, 'w'):
                pass
            return True
        except Exception as e:
            return False

    #НЕ ПРОВЕРЯЛ, но по идее должно остаться таким же
    def write_data_to_file(self, path: str):
        path = 'src/data/' + path
        if self.create_empty_file(path):
            dom = XmlWriter(path)
            data_dict = {}
            for row in self.table.row_data:
                data_dict['Train number'] = row[0]
                data_dict['Departure station'] = row[1]
                data_dict['Arival station'] = row[2]
                data_dict['Date and time of departure'] = row[3]
                data_dict['Date and time of arrival'] = row[4]
                data_dict['Time travel'] = row[5]
                dom.create_xml_student(data_dict)

            dom.create_xml_file()

    #Done   
    def add_new_student(self, row):
        try:
            total = row[len(row)-1] - row[len(row)-2]

            self.table.row_data.insert(
                len(self.table.row_data),
                (
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    total
                )
            )
        except ValueError as v:
            pass

    #ПОЗЖЕ НАДО ВЫПИЛИТЬ
    @staticmethod
    def get_second_name(name: str):
        return name.split()[1]

    def refresh_students(self):
        try:
            self.table.row_data += self._not_filtered
        except ValueError as v:
            pass

        self._not_filtered = []

    #В частных запросах РАБОТАЕТ, но нужен фикс времени в пути
    def select_students(self, filters: list):
        selected_students = []

        for row in self.table.row_data:
            
            #Селекция по номеру поезда
            if filters[0] != '':
                if row[0] != int(filters[0]):
                    selected_students.append(tuple(row))

            #Селекция по станции отправления
            if filters[1] !='':
                if row[1] != filters[1]: #если станция не совпадает -> оставляем поезд
                    selected_students.append(tuple(row))
            
            #Селекция по станции прибытия
            if filters[2] !='':
                if row[2] != filters[2]: #если станция не совпадает -> оставляем поезд
                    selected_students.append(tuple(row))
            
            #Селекция по времени отправления(нижний предел)
            if filters[3] !='':
                if row[3] >= datetime.strptime(filters[3], "%d/%m/%Y %H:%M:%S"): #если станция не совпадает -> оставляем поезд
                    selected_students.append(tuple(row))

            #Селекция по времени прибытия(нижний предел)
            if filters[4] !='':
                if row[4] >= datetime.strptime(filters[4], "%d/%m/%Y %H:%M:%S"): #если станция не совпадает -> оставляем поезд
                    selected_students.append(tuple(row))

            #НУЖЕН ФИКС
            #Селекция по времени в пути(верхний предел)
            if filters[5] !='':
                if row[5] <= datetime.strptime(filters[5], "%d/%m/%Y %H:%M:%S"): #если станция не совпадает -> оставляем поезд
                    selected_students.append(tuple(row))
            '''# group search
            if filters[1] != '' and row[1] != filters[1]:
                selected_students.append(tuple(row))

            # boundaries search
            upper = None
            lower = None
            if filters[2]:
                try:
                    lower = int(filters[2])
                except Exception as e:
                    pass

            if filters[3]:
                try:
                    upper = int(filters[3])
                except Exception as e:
                    pass
            '''
            '''current_value = int(row[12])  И НАХУЙ ЭТО НАДО ?
            if lower and lower > current_value:
                selected_students.append(tuple(row))

            if upper and upper < current_value:
                selected_students.append(tuple(row))'''

        return selected_students

    #По идее работает, если работает select_students
    def filter_students(self, filters: list):
        self._not_filtered = self.select_students(filters=filters)
        for row in self._not_filtered:
            try:
                self.table.row_data.remove(row)
            except Exception as e:
                pass

    #Вроде как работает, тк является просто проверкой на пустоту фильтра
    @staticmethod
    def empty_filters(filters):
        for filt in filters:
            if filt != '':
                return False

        return True

    #Работает
    def delete_students(self, filters):
        deleted_count = 0 #кол-во удаленных "поездов"
        if self.empty_filters(filters): #проверка по каким фильтрам удаляем
            return deleted_count
        students = self.select_students(filters=filters)
        for row in self.table.row_data[:]:
            if row not in students:
                try:
                    self.table.row_data.remove(row)
                    deleted_count += 1
                except Exception as e:
                    pass
        return deleted_count
