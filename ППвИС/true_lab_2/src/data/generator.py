#Done
from random import randint
import sys

sys.path.append('/home/siarhei/Programming/IIT/Univer/ППвИС/true_lab_2/src/utility/parsers')

from writer import XmlWriter

import cities_and_data


class XmlGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_xml_file(count_of_trains):
        path = '/home/siarhei/Programming/IIT/Univer/ППвИС/true_lab_2/src/data/data.xml'
        data_dict = {}
        with open(path, 'w') as file:
            writer = XmlWriter(path)
            
            cities = cities_and_data.New_Yourk_cities()
            data = cities_and_data.Data_of_travel()

            for _ in range(count_of_trains):
                data_dict['train_number'] = str(randint(0, 999))
                data_dict['depart_st'] = cities.get_city()
                data_dict['arriv_st'] = cities.get_city()
                data_dict['data_of_departure'] = data.get_dep_data()
                data_dict['data_of_arrival'] = data.get_arr_data()
                writer.create_xml_student(data_dict)
        writer.create_xml_file()


def main():
    XmlGenerator.generate_xml_file(40)


if __name__ == "__main__":
    main()
