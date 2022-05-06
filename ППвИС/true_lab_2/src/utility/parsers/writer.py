#просто поменял имена

import xml.dom.minidom as minidom


class XmlWriter:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.domtree = minidom.Document()
        self.rows = []

    def create_xml_student(self, data: tuple):
        train = self.domtree.createElement('train')

        for value in data:
            temp_child = self.domtree.createElement(value)
            train.appendChild(temp_child)

            node_text = self.domtree.createTextNode(str(data[value]).strip())
            temp_child.appendChild(node_text)
        self.rows.append(train)

    def create_xml_file(self):
        pass_table = self.domtree.createElement('trains')

        for student in self.rows:
            pass_table.appendChild(student)

        self.domtree.appendChild(pass_table)

        self.domtree.writexml(open(self.file_name, 'w'),
                              indent=" ",
                              addindent=" ",
                              newl='\n')
        self.domtree.unlink()
