from random import randint
from utility.parsers.writer import XmlWriter

import names


class XmlGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_xml_file(count_of_students):
        path = 'src/data.xml'
        data_dict = {}
        with open(path, 'w') as file:
            writer = XmlWriter(path)
            for _ in range(count_of_students):
                data_dict['name'] = names.get_full_name()
                data_dict['group'] = str(randint(100000, 999999))
                data_dict['semester_1'] = str(randint(1, 20))
                data_dict['semester_2'] = str(randint(1, 20))
                data_dict['semester_3'] = str(randint(1, 20))
                data_dict['semester_4'] = str(randint(1, 20))
                data_dict['semester_5'] = str(randint(1, 20))
                data_dict['semester_6'] = str(randint(1, 20))
                data_dict['semester_7'] = str(randint(1, 20))
                data_dict['semester_8'] = str(randint(1, 20))
                data_dict['semester_9'] = str(randint(1, 20))
                data_dict['semester_10'] = str(randint(1, 20))
                writer.create_xml_student(data_dict)
        writer.create_xml_file()


def main():
    XmlGenerator.generate_xml_file(40)


if __name__ == "__main__":
    main()
