import re
import sys


from utility.parsers.reader import XmlReader
from utility.parsers.writer import XmlWriter


import utility.abstractions.observable as Observable
import utility.abstractions.observer as Observer


class ModelComponent():
    _not_filtered = []

    def __init__(self, table):
        self.table = table

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

    @staticmethod
    def create_empty_file(path):
        try:
            with open(path, 'w'):
                pass
            return True
        except Exception as e:
            return False

    def write_data_to_file(self, path: str):
        path = 'src/data/' + path
        if self.create_empty_file(path):
            dom = XmlWriter(path)
            data_dict = {}
            for row in self.table.row_data:
                data_dict['name'] = row[0]
                data_dict['group'] = row[1]
                data_dict['semester_1'] = row[2]
                data_dict['semester_2'] = row[3]
                data_dict['semester_3'] = row[4]
                data_dict['semester_4'] = row[5]
                data_dict['semester_5'] = row[6]
                data_dict['semester_6'] = row[7]
                data_dict['semester_7'] = row[8]
                data_dict['semester_8'] = row[9]
                data_dict['semester_9'] = row[10]
                data_dict['semester_10'] = row[11]
                dom.create_xml_student(data_dict)

            dom.create_xml_file()

    def add_new_student(self, row):
        try:
            total = 0
            for i in range(2, len(row)):
                total += int(row[i])

            self.table.row_data.insert(
                len(self.table.row_data),
                (
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                    str(total)
                )
            )
        except ValueError as v:
            pass

    @staticmethod
    def get_second_name(name: str):
        return name.split()[1]

    def refresh_students(self):
        try:
            self.table.row_data += self._not_filtered
        except ValueError as v:
            pass

        self._not_filtered = []

    def select_students(self, filters: list):
        selected_students = []

        for row in self.table.row_data:
            # search by second name even through first name also given
            if filters[0] != '':
                last_name = self.get_second_name(row[0])
                filter_last_name = filters[0]
                if last_name != filter_last_name:
                    selected_students.append(tuple(row))

            # group search
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

            current_value = int(row[12])
            if lower and lower > current_value:
                selected_students.append(tuple(row))

            if upper and upper < current_value:
                selected_students.append(tuple(row))

        return selected_students

    def filter_students(self, filters: list):
        self._not_filtered = self.select_students(filters=filters)
        for row in self._not_filtered:
            try:
                self.table.row_data.remove(row)
            except Exception as e:
                pass

    @staticmethod
    def empty_filters(filters):
        for filt in filters:
            if filt != '':
                return False

        return True

    def delete_students(self, filters):
        deleted_count = 0
        if self.empty_filters(filters):
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
