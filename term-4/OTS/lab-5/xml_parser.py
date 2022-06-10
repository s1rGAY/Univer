import xml.etree.ElementTree as ET

file = '/home/siarhei/Programming/IIT/laB-5-OTS/OTS_4_term/Laboratory work 5/graph.xml'
tree = ET.parse(file)
root = tree.getroot()


class Globals:

    def __init__(self):
        self.name = XmlParser.find_names(root)
        self.text = XmlParser.find_text(root)
        self.color = XmlParser.find_color(root)
        self.vertex = XmlParser.find_vertex(root)
        self.edges_name = XmlParser.find_edges_name(root)
        self.edges_path = XmlParser.find_edges_path(root)
        self.current_graph = None
        self.bool = None
        self.Columns = None
        self.Lines = None
        self.timer = [100] * 100
        self.visit = [100] * 100
        self.root = None
        self.graph_1 = None
        self.graph_2 = None
        self.start = None
        self.end = None
        self.g_it = -1
        self.arc = 0

    def stabilization(self):
        self.name = XmlParser.find_names(root)
        self.color = XmlParser.find_color(root)
        self.text = XmlParser.find_text(root)
        self.vertex = XmlParser.find_vertex(root)
        self.edges_name = XmlParser.find_edges_name(root)
        self.edges_path = XmlParser.find_edges_path(root)
        self.Columns = len(self.edges_name)
        self.Lines = len(self.vertex)

    def stabilization_matrix(self):
        self.Columns = None
        self.Lines = None
        del self.visit
        del self.timer
        self.timer = [100] * 100
        self.visit = [100] * 100
        self.root = None


class XmlParser:

    @staticmethod
    def find_names(root):
        names = []
        for elem in root.findall('graph'):
            names.append(elem.get('name_graph'))
        return names

    @staticmethod
    def find_text(root):
        text = []
        for elem in root.findall('graph'):
            text.append(elem.get('text'))
        return text

    @staticmethod
    def find_color(root):
        color = []
        for elem in root.findall('graph'):
            color.append(elem.get('color'))
        return color

    @staticmethod
    def find_vertex(root):
        vertex = []
        for elem in root.findall('graph'):
            vertex.append(elem.get('vertex'))
        return vertex

    @staticmethod
    def find_edges_name(root):
        edges_name = []
        for elem in root.findall('graph'):
            edges_name.append(elem.get('edges_name'))
        return edges_name

    @staticmethod
    def find_edges_path(root):
        edges_path = []
        for elem in root.findall('graph'):
            edges_path.append(elem.get('edges_path'))
        return edges_path

    @staticmethod
    def add_graph(name, color='no color,no color', vertex='node1,node2', edges_name='edge1',
                  edges_path='node1,=>,node2', text=' , '):
        global file
        global root
        global tree
        data = ET.Element('graphs')
        item = ET.SubElement(data, 'graph')
        item.set('name_graph', name)
        item.set('text', text)
        item.set('color', color)
        item.set('vertex', vertex)
        item.set('edges_name', edges_name)
        item.set('edges_path', edges_path)
        root.append(item)
        tree.write(file)  # перезапись

    @staticmethod
    def remove_graph(number):
        global file
        root.remove(root[number])
        tree.write(file)

    @staticmethod
    def add_vertex(current_graph, vertex, color, text):
        root[current_graph].set('vertex', vertex)
        root[current_graph].set('color', color)
        root[current_graph].set('text', text)
        tree.write(file)  # перезапись

    @staticmethod
    def add_edges(current_graph, edges, edges_path):
        root[current_graph].set('edges_name', edges)
        root[current_graph].set('edges_path', edges_path)
        tree.write(file)  # перезапись

    @staticmethod
    def change_text(current_graph, text):
        root[current_graph].set('text', text)
        tree.write(file)  # перезапись
