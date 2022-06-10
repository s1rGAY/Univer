import re
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from xml_parser import *
from is_graph_planar import *

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1300)
Config.set('graphics', 'height', 800)

from kivy.uix.textinput import TextInput

globals = Globals()

Builder.load_string('''
<ItemTextInput@TextInput>:
    multiline: False
    background_color: 'white'
    halign: 'left'
    cursor_blink: True
    cursor_color: 'white'
    foreground_color: 'black'
    font_size: '14'
<ItemButton@Button>:
    font_size: 12
    color: 'black'
    background_color: .24, .50, .80, 1
    background_normal: ''
<ItemLabel@Label>:
    color: 'white'
    halign:'center'
    valign:'middle'
    text_size:self.size

<Table>:
    status:status
    graphname:graphname
    newgraph:newgraph
    
    
    edges:edges
    nodes:nodes
    matrixx:matrixx
    graphinfo:graphinfo
    
    
    workedges:workedges
    workvertex:workvertex
    
    
    addarc:addarc
    vertexfirst:vertexfirst
    orientation:orientation
    vertexsecond:vertexsecond
    delarc:delarc
    
    
    addvertex:addvertex
    color:color
    delvertex:delvertex
    
    decfirst:decfirst
    decsecond:decsecond
    
    vecfirst:vecfirst
    vecsecond:vecsecond
    
    textvertex:textvertex
    textvertexdel:textvertexdel
    
    FloatLayout:
     
        ItemTextInput: 
            id:graphname
            hint_text:'имя графа'
            size_hint: .1, .05
            pos: 0, 760
            
        ItemButton:
            text: 'поиск'
            size_hint: .1, .05
            pos: 0, 710
            on_press:
                root.change_graph()
                root.clear_matrix()
                root.del_info_graph()
                root.update()
                
        ItemButton:
            text: 'информация о графе'
            size_hint: .1, .05
            pos: 0, 660
            on_press:
                root.clear_matrix()
                root.show_matrix()
                root.radius_diameter()
                root.planar()
        
        ItemButton:
            text: 'удалить граф'
            size_hint: .1, .05
            pos: 0, 610
            on_press:
                root.del_info_graph()
                root.del_graph()
                root.clear_matrix()
        
        ItemButton:
            text: 'добавить граф'
            size_hint: .1, .05
            pos: 0, 560
            on_press:
                root.add_graph()
            
        ItemTextInput: 
            id:newgraph
            hint_text:'имя графа'
            size_hint: .1, .05
            pos: 0, 510
        
          
        ItemLabel:
            id:status
            text: 'статус'
            size_hint: .1, .05
            pos: 0, 460
        
        ItemButton:
            text: 'декартовое *'
            size_hint: .1, .05
            pos: 0, 410
            on_press:
                root.composition()
                
        
        ItemTextInput: 
            id:decfirst
            hint_text:'имя графа'
            size_hint: .1, .05
            pos: 0, 360
            
        ItemTextInput: 
            id:decsecond
            hint_text:'имя графа'
            size_hint: .1, .05
            pos: 0, 310
        
        ItemButton:
            text: 'векторное *'
            size_hint: .1, .05
            pos: 0, 260
            on_press:
                root.composition_del()
        
        ItemTextInput: 
            id:vecfirst
            hint_text:'имя графа'
            size_hint: .1, .05
            pos: 0, 210
            
        ItemTextInput: 
            id:vecsecond
            hint_text:'имя графа'
            size_hint: .1, .05
            pos: 0, 160
            
        ItemButton:
            text: 'сделать планарным'
            size_hint: .1, .05
            pos: 0, 110
            on_press:
                root.make_it_planar()
                root.del_info_graph()
                root.clear_matrix()
                root.update()
            
        
        BoxLayout:
            id:edges
            orientation: 'vertical'
            size_hint: .4, .25
            pos:140,600
            
            Label:
                text:'edges:'
                halign:'center'
                valign:'middle'
                text_size:self.size
           
        
        BoxLayout:
            id:nodes
            orientation: 'vertical'
            size_hint: .4, .25
            pos:140,400
            
            Label:
                text:'nodes:'
                halign:'center'
                valign:'middle'
                text_size:self.size
            
            
        BoxLayout:
            id:matrixx
            orientation: 'vertical'
            size_hint: .4, .25
            pos:140,200
            
            Label:
                text:'matrix:'
                halign:'center'
                valign:'middle'
                text_size:self.size
           
            
        BoxLayout:
            id:graphinfo
            orientation: 'vertical'
            size_hint: .4, .25
            pos:140,0
            
            Label:
                text:'graph info:'
                halign:'center'
                valign:'middle'
                text_size:self.size
            
        GridLayout:
            id:workedges
            rows: 2
            cols: 5
            spacing: 3
            size_hint: .4, .25
            pos: 720, 500
            
            ItemButton:
                text:'Добавить  дугу'
                on_press:
                    root.add_arc()
                    root.del_info_graph()
                    root.clear_matrix()
                    root.update()
            Widget:
            Widget:
            Widget:
            ItemButton:
                text:'Удалить  дугу'
                on_press:
                    root.del_arc()
                    root.del_info_graph()
                    root.clear_matrix()
                    root.update()
                
            ItemTextInput:
                id:addarc
                hint_text:'имя дуги'
            ItemTextInput:
                id:vertexfirst
                hint_text:'из вершины'
            ItemTextInput:
                id:orientation
                hint_text:'=(>)'
            ItemTextInput:
                id:vertexsecond
                hint_text:'в вершину'
            ItemTextInput:
                id:delarc
                hint_text:'имя дуги'
        
        ItemButton:
            text: 'изм.текст вершины'
            size_hint: .1, .05
            pos: 920, 400
            on_press:
                root.change_text()
                root.del_info_graph()
                root.update()
                
        ItemTextInput: 
            id:textvertex
            hint_text:'имя вершины'
            size_hint: .1, .05
            pos: 920, 350
            
        ItemTextInput: 
            id:textvertexdel
            hint_text:'текст'
            size_hint: .15, .05
            pos: 1050, 350
        
        GridLayout:
            id: workvertex
            rows: 2
            cols: 3
            spacing: 3
            size_hint: .4, .25
            pos: 720, 100
            
            ItemButton:
                text:'Добавить вершину'
                on_press:
                    root.add_vertex()
                    root.del_info_graph()
                    root.clear_matrix()
                    root.update()
            Widget:
            ItemButton:
                text:'Удалить вершину'
                on_press:
                    root.del_vertex()
                    root.del_info_graph()
                    root.clear_matrix()
                    root.update()
            ItemTextInput:
                id:addvertex
                hint_text:'имя вершины'
            ItemTextInput:
                id:color
                hint_text:'цвет'
            ItemTextInput:
                id:delvertex
                hint_text:'имя вершины'
            
''')


# Создайте класс для всех экранов, в которые вы можете включить
# полезные методы, специфичные для этого экрана

class Table(Screen):
    edges_list = []
    vertex_list = []
    matrix = []
    matrix_label = []
    eccentricity = [100] * 100
    info = []
    hamiltonian_cycle = []
    hamiltonian_cycle_del = []
    result = None
    bad_minor = None

    def change_graph(self):
        self.del_info_graph()
        try:
            for i in range(len(globals.name)):
                if self.graphname.text == globals.name[i]:
                    globals.current_graph = i
                    globals.bool = True
                    self.status.text = 'Граф найден'
            if globals.bool:
                globals.bool = None
            else:
                raise ValueError
        except(ValueError):
            self.status.text = 'Граф не найден'
            globals.current_graph = None

    def update(self):
        i_edges = -1
        it_edges = 0
        it_path = 0

        i_vertex = -1

        if globals.current_graph is not None:

            edges_path = globals.edges_path[globals.current_graph]
            edges_path = edges_path.split(sep=',')

            edges_name = globals.edges_name[globals.current_graph]
            edges_name = edges_name.split(sep=',')

            vertex_name = globals.vertex[globals.current_graph]
            vertex_name = vertex_name.split(sep=',')

            vertex_text = globals.text[globals.current_graph]
            vertex_text = vertex_text.split(sep=',')

            vertex_color = globals.color[globals.current_graph]
            vertex_color = vertex_color.split(sep=',')

            if globals.edges_name[globals.current_graph] != '':
                for i in range(len(edges_name)):
                    i_edges += 1
                    Table.edges_list.append(Label(
                        text=edges_name[it_edges] + ' : ' + edges_path[it_edges + it_path] + edges_path[
                            it_edges + it_path + 1] + edges_path[
                                 it_edges + it_path + 2]))
                    it_edges += 1
                    it_path += 2
                    self.edges.add_widget(Table.edges_list[i_edges])

            i_edges += 1
            Table.edges_list.append(Label(text='count:{} '.format(len(edges_name))))
            self.edges.add_widget(Table.edges_list[i_edges])

            if globals.vertex[globals.current_graph] != '':
                for i in range(len(vertex_name)):
                    i_vertex += 1
                    Table.vertex_list.append(
                        Label(text=vertex_name[i_vertex] + '(' + vertex_color[i_vertex] + ')' + '(' + "text:{}".format(
                            vertex_text[i]) + ')'))
                    self.nodes.add_widget(Table.vertex_list[i_vertex])

            i_vertex += 1
            Table.vertex_list.append(Label(text='count:{}'.format(len(vertex_name))))
            self.nodes.add_widget(Table.vertex_list[i_vertex])

    def del_info_graph(self):
        try:
            for i in range(len(Table.edges_list)):
                self.edges.remove_widget(Table.edges_list[i])
            Table.edges_list.clear()
            for i in range(len(Table.vertex_list)):
                self.nodes.remove_widget(Table.vertex_list[i])
            Table.vertex_list.clear()
        except(IndexError):
            pass

    def del_graph(self):
        if globals.current_graph is not None:
            XmlParser.remove_graph(globals.current_graph)
            globals.current_graph = None
            self.status.text = 'граф удалён'
        else:
            self.status.text = 'найдите граф'
        globals.stabilization()

    def add_graph(self):
        try:
            if self.newgraph.text == '':
                self.status.text = 'введите имя графа'
                raise IndexError
            elif re.search(r'[^a-zA-Z0-9_.+-]', self.newgraph.text):
                self.status.text = 'используйте латиницу'
                raise IndexError
            else:
                for i in range(len(globals.name)):
                    if self.newgraph.text == globals.name[i]:
                        self.status.text = 'такой граф уже есть '
                        raise IndexError

            XmlParser.add_graph(self.newgraph.text)
            self.status.text = 'граф добален'
            globals.stabilization()

        except IndexError:
            pass

    def add_vertex(self):
        try:
            if globals.current_graph == None:
                self.status.text = 'найдите нужный граф'
                raise ValueError

            vertex_name = globals.vertex[globals.current_graph]
            vertex_name = vertex_name.split(sep=',')

            vertex_color = globals.color[globals.current_graph]
            vertex_color = vertex_color.split(sep=',')

            vertex_text = globals.text[globals.current_graph]
            vertex_text = vertex_text.split(sep=',')

            if self.addvertex.text == '':
                self.status.text = 'введите имя вершины'
                raise ValueError

            if re.search(r'[^a-zA-Z0-9_.+-]', self.addvertex.text):
                self.status.text = 'используйте латиницу'
                raise ValueError

            for i in range(len(vertex_name)):
                if self.addvertex.text == vertex_name[i]:
                    self.status.text = 'такая вершина уже есть '
                    raise ValueError

            if re.search(r'[^a-zA-Z0-9_.+-]', self.color.text):
                self.status.text = 'используйте латиницу'
                raise ValueError
            else:
                if self.color.text == '':
                    self.color.text = 'no color'
                ver_del = ','.join(vertex_name)
                col_del = ','.join(vertex_color)
                ver_del = ver_del + ',' + self.addvertex.text
                col_del = col_del + ',' + self.color.text
                ver_tex = ','.join(vertex_text)
                ver_tex = ver_tex + ',' + ' '
                globals.stabilization()
                XmlParser.add_vertex(globals.current_graph, ver_del, col_del, ver_tex)
                globals.stabilization()
                self.status.text = 'вершина добавлена'


        except ValueError:
            pass

    def del_vertex(self):
        try:
            if globals.current_graph == None:
                self.status.text = 'найдите нужный граф'
                raise ValueError

            bl = True
            it = None

            vertex_name = globals.vertex[globals.current_graph]
            vertex_name = vertex_name.split(sep=',')

            vertex_color = globals.color[globals.current_graph]
            vertex_color = vertex_color.split(sep=',')

            edges_path = globals.edges_path[globals.current_graph]
            edges_path = edges_path.split(sep=',')

            edges_name = globals.edges_name[globals.current_graph]
            edges_name = edges_name.split(sep=',')

            vertex_text = globals.text[globals.current_graph]
            vertex_text = vertex_text.split(sep=',')

            if self.delvertex.text == '':
                self.status.text = 'введите имя вершины'
                raise ValueError

            if re.search(r'[^a-zA-Z0-9_.+-]', self.delvertex.text):
                self.status.text = 'используйте латиницу'
                raise ValueError

            for i in range(len(vertex_name)):
                if self.delvertex.text == vertex_name[i]:
                    it = i
                    bl = False
                    break

            if bl:
                self.status.text = 'такой вершины нет'
                raise ValueError

            del vertex_name[it]
            del vertex_color[it]
            del vertex_text[it]

            i_del_ed = 0
            i_del_pt = 0

            for ed in range(len(edges_name)):

                for ed_pt in range(0, 1):
                    type = ed + i_del_ed
                    if self.delvertex.text == edges_path[type + i_del_pt]:
                        del edges_path[type + i_del_pt]
                        del edges_path[type + i_del_pt]
                        del edges_path[type + i_del_pt]
                        del edges_name[type]
                        i_del_ed -= 1
                    elif self.delvertex.text == edges_path[type + i_del_pt + 2]:
                        del edges_path[type + i_del_pt]
                        del edges_path[type + i_del_pt]
                        del edges_path[type + i_del_pt]
                        del edges_name[type]
                        i_del_ed -= 1
                    else:
                        i_del_pt += 2

            ver_del = ','.join(vertex_name)
            col_del = ','.join(vertex_color)
            ed_del = ','.join(edges_name)
            ed_pat_del = ','.join(edges_path)
            ver_tex = ','.join(vertex_text)
            globals.stabilization()
            XmlParser.add_vertex(globals.current_graph, ver_del, col_del, ver_tex)
            XmlParser.add_edges(globals.current_graph, ed_del, ed_pat_del)
            self.status.text = 'вершина удалена'
            globals.stabilization()

        except ValueError:
            pass

    def add_arc(self):
        try:
            if globals.current_graph == None:
                self.status.text = 'найдите нужный граф'
                raise ValueError

            it = None
            bl = True

            edges_path = globals.edges_path[globals.current_graph]
            edges_path = edges_path.split(sep=',')

            edges_name = globals.edges_name[globals.current_graph]
            edges_name = edges_name.split(sep=',')

            vertex_name = globals.vertex[globals.current_graph]
            vertex_name = vertex_name.split(sep=',')

            if self.addarc.text == '':
                self.status.text = 'введите имя дуги'
                raise ValueError

            if self.vertexfirst.text == '':
                self.status.text = 'введите имя 1 вершины'
                raise ValueError

            if self.vertexsecond.text == '':
                self.status.text = 'введите имя 2 вершины'
                raise ValueError

            if self.orientation.text == '=':
                pass
            elif self.orientation.text == '=>':
                pass
            else:
                self.status.text = 'отношение может быть =(>)'
                raise ValueError

            if re.search(r'[^a-zA-Z0-9_.+-]', self.addarc.text):
                self.status.text = 'используйте латиницу'
                raise ValueError

            if re.search(r'[^a-zA-Z0-9_.+-]', self.vertexfirst.text):
                self.status.text = 'используйте латиницу'
                raise ValueError

            if re.search(r'[^a-zA-Z0-9_.+-]', self.vertexsecond.text):
                self.status.text = 'используйте латиницу'
                raise ValueError

            for i in range(len(edges_name)):
                if self.addarc.text == edges_name[i]:
                    self.status.text = 'такая дуга уже есть'
                    raise ValueError

            for i in range(len(vertex_name)):
                print(vertex_name[i])
                if self.vertexfirst.text == vertex_name[i]:
                    bl = False

            if bl:
                self.status.text = 'вершины 1 нет в графе'
                raise ValueError

            bl = True

            for i in range(len(vertex_name)):
                if self.vertexsecond.text == vertex_name[i]:
                    bl = False

            if bl:
                self.status.text = 'вершины 2 нет в графе'
                raise ValueError

            ed_del = ','.join(edges_name)
            ed_pat_del = ','.join(edges_path)
            ed_del = ed_del + ',' + self.addarc.text
            ed_pat_del = ed_pat_del + ',' + self.vertexfirst.text + ',' + self.orientation.text + ',' + self.vertexsecond.text

            XmlParser.add_edges(globals.current_graph, ed_del, ed_pat_del)
            self.status.text = 'дуга добавлена'
            globals.stabilization()

        except ValueError:
            pass

    def del_arc(self):
        try:
            if globals.current_graph == None:
                self.status.text = 'найдите нужный граф'
                raise ValueError

            bl = True
            it = None
            type = None

            edges_path = globals.edges_path[globals.current_graph]
            edges_path = edges_path.split(sep=',')

            edges_name = globals.edges_name[globals.current_graph]
            edges_name = edges_name.split(sep=',')

            if self.delarc.text == '':
                self.status.text = 'введите имя дуги'
                raise ValueError

            if re.search(r'[^a-zA-Z0-9_.+-]', self.delarc.text):
                self.status.text = 'используйте латиницу'
                raise ValueError

            for i in range(len(edges_name)):
                if self.delarc.text == edges_name[i]:
                    it = i
                    bl = False
                    break

            if bl:
                self.status.text = 'такой дуги нет'
                raise ValueError

            del edges_name[it]

            if it == 0:
                type = -1
            elif it == 1:
                type = 2
            elif it == 2:
                type = 5
            elif it == 3:
                type = 8
            elif it == 4:
                type = 11
            elif it == 5:
                type = 14
            elif it == 6:
                type = 17
            elif it == 7:
                type = 20
            elif it == 8:
                type = 23
            elif it == 9:
                type = 26
            elif it == 10:
                type = 29
            elif it == 11:
                type = 32
            elif it == 12:
                type = 35
            elif it == 13:
                type = 38
            elif it == 14:
                type = 41
            elif it == 15:
                type = 44
            elif it == 16:
                type = 47
            elif it == 17:
                type = 50
            elif it == 18:
                type = 53
            elif it == 19:
                type = 56
            elif it == 20:
                type = 59
            elif it == 21:
                type = 62

            del edges_path[type + 1]
            del edges_path[type + 1]
            del edges_path[type + 1]

            ed_del = ','.join(edges_name)
            ed_pat_del = ','.join(edges_path)
            globals.stabilization()

            XmlParser.add_edges(globals.current_graph, ed_del, ed_pat_del)
            self.status.text = 'дуга удалена'
            globals.stabilization()

        except ValueError:
            pass

    def matrix_transcendence(self):
        try:

            Table.matrix.clear()
            if globals.current_graph == None:
                self.status.text = 'найдите нужный граф'
                raise ValueError

            vertex_name = globals.vertex[globals.current_graph]
            vertex_name = vertex_name.split(sep=',')

            edges_path = globals.edges_path[globals.current_graph]
            edges_path = edges_path.split(sep=',')

            col = -1
            value_start = 1
            vale_end = -1
            value_or = 1
            id_start = None
            id_end = None

            for i in range(len(vertex_name)):
                a = []
                for j in range(1, len(edges_path), 3):
                    a.append(0)
                for j_t in range(0, 1):
                    Table.matrix.append(a)

            for j in range(1, len(edges_path), 3):
                col += 1
                if edges_path[j] == '=':
                    for i_s in range(len(vertex_name)):
                        if edges_path[j - 1] == vertex_name[i_s]:
                            id_start = i_s
                    for i_n in range(len(vertex_name)):
                        if edges_path[j + 1] == vertex_name[i_n]:
                            id_end = i_n
                    for i in range(len(vertex_name)):
                        if i == id_start:
                            Table.matrix[i][col] = value_or
                        elif i == id_end:
                            Table.matrix[i][col] = value_or
                        else:
                            Table.matrix[i][col] = 0
                elif edges_path[j] == '=>':
                    for i_s in range(len(vertex_name)):
                        if edges_path[j - 1] == vertex_name[i_s]:
                            id_start = i_s
                            break
                    for i_n in range(len(vertex_name)):
                        if edges_path[j + 1] == vertex_name[i_n]:
                            id_end = i_n
                            break
                    for i in range(len(vertex_name)):
                        if i == id_start:
                            Table.matrix[i][col] = value_start
                        elif i == id_end:
                            Table.matrix[i][col] = vale_end
                        else:
                            Table.matrix[i][col] = 0

            print('matrix of graph')
            print(Table.matrix)

        except ValueError:
            pass

    def show_matrix(self):
        try:
            if globals.current_graph == None:
                self.status.text = 'найдите нужный граф'
                raise ValueError

            self.matrix_transcendence()
            i_m = -1
            text = ''
            edges_name = globals.edges_name[globals.current_graph]
            edges_name = edges_name.split(sep=',')

            vertex_name = globals.vertex[globals.current_graph]
            vertex_name = vertex_name.split(sep=',')

            for row in range(len(vertex_name)):
                for col in range(len(edges_name)):
                    if col + 1 != len(edges_name):
                        text = text + str(Table.matrix[row][col]) + ','
                    else:
                        text = text + str(Table.matrix[row][col])
                    if col == len(edges_name) - 1:
                        i_m += 1
                        Table.matrix_label.append(Label(text=text))
                        self.matrixx.add_widget(Table.matrix_label[i_m])
                        text = ''
        except ValueError:
            pass

    def clear_matrix(self):
        try:
            for i in range(len(Table.matrix_label)):
                self.matrixx.remove_widget(Table.matrix_label[i])
            Table.matrix_label.clear()
            for i in range(len(Table.info)):
                self.graphinfo.remove_widget(Table.info[i])
            Table.info.clear()
        except(IndexError):
            pass

    def radius_diameter(self):
        try:
            if globals.current_graph == None:
                self.status.text = 'найдите нужный граф'
                raise ValueError

            edges_name = globals.edges_name[globals.current_graph]
            edges_name = edges_name.split(sep=',')

            vertex_name = globals.vertex[globals.current_graph]
            vertex_name = vertex_name.split(sep=',')


            globals.Columns = len(edges_name)
            globals.Lines = len(vertex_name)


            diameter = 0
            radius = 100
            for i in range(0, globals.Lines):
                Table.eccentricity[i] = 0
            for i in range(0, globals.Lines):
                globals.visit[i] = 0
            for vertex in range(0, globals.Lines):
                for i_t in range(0, globals.Lines):
                    globals.timer[i_t] = 100
                globals.root = vertex
                dfs(vertex)
                for i in range(0, globals.Lines):
                    if globals.timer[i] == 100:
                        globals.timer[i] = 0
                for k in range(0, globals.Lines):
                    if Table.eccentricity[globals.root] < globals.timer[k]:
                        Table.eccentricity[globals.root] = globals.timer[k]

            for i in range(0, globals.Lines):
                if diameter < Table.eccentricity[i]:
                    diameter = Table.eccentricity[i]

            for i in range(0, globals.Lines):
                if radius > Table.eccentricity[i]:
                    radius = Table.eccentricity[i]

            i_i = -1

            for i in range(0, globals.Lines):
                i_i += 1
                Table.info.append(Label(text='экстренситет вершины  {}:{}'.format(i + 1, Table.eccentricity[i])))
                self.graphinfo.add_widget(Table.info[i_i])

            for i in range(0, globals.Lines):
                if Table.eccentricity[i] == radius:
                    i_i += 1
                    Table.info.append(Label(text='центр графа: {}'.format(vertex_name[i])))
                    self.graphinfo.add_widget(Table.info[i_i])

            i_i += 1
            Table.info.append(Label(text='радиус {}'.format(radius)))
            self.graphinfo.add_widget(Table.info[i_i])

            i_i += 1
            Table.info.append(Label(text='диаметр {}'.format(diameter)))
            self.graphinfo.add_widget(Table.info[i_i])

            if len(Table.hamiltonian_cycle) == 0:
                i_i += 1
                Table.info.append(Label(text='гамильтов цикл: None'.format(diameter)))
                self.graphinfo.add_widget(Table.info[i_i])
            else:
                i_i += 1
                for i in range(len(Table.hamiltonian_cycle)):
                    vertex = vertex_name[Table.hamiltonian_cycle[i]]
                    Table.hamiltonian_cycle[i] = vertex
                Table.info.append(Label(text='гамильтов цикл: {}'.format(Table.hamiltonian_cycle)))
                self.graphinfo.add_widget(Table.info[i_i])

            print('this is hamilton cycle')
            print(Table.hamiltonian_cycle)

            del Table.eccentricity

            Table.eccentricity = [100] * 100
            globals.stabilization_matrix()
            Table.hamiltonian_cycle.clear()
            Table.hamiltonian_cycle_del.clear()

        except ValueError:
            pass

    def composition(self):
        try:
            names_new = []
            color_new = []
            arc_new = []
            new_arc_path = []
            text_new = []

            for i in range(len(globals.name)):
                if self.decfirst.text == globals.name[i]:
                    globals.graph_1 = i
                    globals.bool = True

            if globals.bool:
                globals.bool = None
            else:
                self.status.text = 'Граф 1 не найден'
                raise ValueError

            for i in range(len(globals.name)):
                if self.decsecond.text == globals.name[i]:
                    globals.graph_2 = i
                    globals.bool = True

            if globals.bool:
                globals.bool = None
            else:
                self.status.text = 'Граф 2 не найден'
                raise ValueError

            edges_path_1 = globals.edges_path[globals.graph_1]
            edges_path_1 = edges_path_1.split(sep=',')

            vertex_name_1 = globals.vertex[globals.graph_1]
            vertex_name_1 = vertex_name_1.split(sep=',')

            edges_path_2 = globals.edges_path[globals.graph_2]
            edges_path_2 = edges_path_2.split(sep=',')

            vertex_name_2 = globals.vertex[globals.graph_2]
            vertex_name_2 = vertex_name_2.split(sep=',')

            if len(vertex_name_1) != len(vertex_name_2):
                self.status.text = 'кол. вер. не одинаковое'
                raise ValueError

            for i in range(len(vertex_name_2)):
                for i_t in range(len(vertex_name_1)):
                    names_new.append(vertex_name_1[i_t] + '-' + vertex_name_2[i])

            for i in range(len(names_new)):
                color_new.append('no color')

            for i in range(len(names_new)):
                text_new.append(' ')

            it = len(vertex_name_1) - len(vertex_name_1) * 2

            # first graph
            for num in range(0, len(vertex_name_2)):
                it += len(vertex_name_1)

                for i in range(1, len(edges_path_1), 3):

                    for val in range(len(vertex_name_1)):
                        if edges_path_1[i - 1] == vertex_name_1[val]:
                            globals.start = names_new[it + val]

                    for val in range(len(vertex_name_1)):
                        if edges_path_1[i + 1] == vertex_name_1[val]:
                            globals.end = names_new[it + val]

                    new_arc_path.append(globals.start)
                    new_arc_path.append('=>')
                    new_arc_path.append(globals.end)

            it_2 = len(vertex_name_2)

            # second graph
            for num in range(0, len(vertex_name_1)):
                globals.g_it += 1

                for i in range(1, len(edges_path_2), 3):

                    for val in range(len(vertex_name_2)):
                        if edges_path_2[i - 1] == vertex_name_2[val]:
                            val = val * it_2 + globals.g_it

                            globals.start = names_new[val]

                    for val in range(len(vertex_name_2)):
                        if edges_path_2[i + 1] == vertex_name_2[val]:
                            val = val * it_2 + globals.g_it

                            globals.end = names_new[val]

                    new_arc_path.append(globals.start)
                    new_arc_path.append('=>')
                    new_arc_path.append(globals.end)

            for i in range(1, len(new_arc_path), 3):
                globals.arc += 1
                arc_new.append('edge{}'.format(globals.arc))

            print(color_new)
            print(names_new)
            print(new_arc_path)
            print(arc_new)
            name = self.decfirst.text + self.decsecond.text + 'd'

            ver_del = ','.join(names_new)
            col_del = ','.join(color_new)
            arc_del = ','.join(arc_new)
            ver_tex = ','.join(text_new)
            path = ','.join(new_arc_path)

            XmlParser.add_graph(name, col_del, ver_del, arc_del, path, ver_tex)
            globals.stabilization()

            self.status.text = 'создан граф {}'.format(name)

            globals.g_it = -1
            globals.arc = 0

        except ValueError:
            pass

    def composition_del(self):
        try:
            names_new = []
            color_new = []
            arc_new = []
            new_arc_path = []
            text_new = []

            for i in range(len(globals.name)):
                if self.vecfirst.text == globals.name[i]:
                    globals.graph_1 = i
                    globals.bool = True

            if globals.bool:
                globals.bool = None
            else:
                self.status.text = 'Граф 1 не найден'
                raise ValueError

            for i in range(len(globals.name)):
                if self.vecsecond.text == globals.name[i]:
                    globals.graph_2 = i
                    globals.bool = True

            if globals.bool:
                globals.bool = None
            else:
                self.status.text = 'Граф 2 не найден'
                raise ValueError

            edges_path_1 = globals.edges_path[globals.graph_1]
            edges_path_1 = edges_path_1.split(sep=',')

            vertex_name_1 = globals.vertex[globals.graph_1]
            vertex_name_1 = vertex_name_1.split(sep=',')

            edges_path_2 = globals.edges_path[globals.graph_2]
            edges_path_2 = edges_path_2.split(sep=',')

            vertex_name_2 = globals.vertex[globals.graph_2]
            vertex_name_2 = vertex_name_2.split(sep=',')

            if len(vertex_name_1) != len(vertex_name_2):
                self.status.text = 'кол. вер. не одинаковое'
                raise ValueError

            for i in range(len(vertex_name_2)):
                for i_t in range(len(vertex_name_1)):
                    names_new.append(vertex_name_1[i_t] + '-' + vertex_name_2[i])

            for i in range(len(names_new)):
                color_new.append('no color')

            for i in range(len(names_new)):
                text_new.append(' ')

            it = len(vertex_name_1) - len(vertex_name_1) * 2

            # first graph
            for num in range(0, len(vertex_name_2)):
                it += len(vertex_name_1)

                for i in range(1, len(edges_path_1), 3):

                    for val in range(len(vertex_name_1)):
                        if edges_path_1[i - 1] == vertex_name_1[val]:
                            globals.start = names_new[it + val]

                    for val in range(len(vertex_name_1)):
                        if edges_path_1[i + 1] == vertex_name_1[val]:
                            globals.end = names_new[it + val]

                    new_arc_path.append(globals.start)
                    new_arc_path.append('=>')
                    new_arc_path.append(globals.end)

            it_2 = len(vertex_name_2)

            # second graph
            for num in range(0, len(vertex_name_1)):
                globals.g_it += 1

                for i in range(1, len(edges_path_2), 3):

                    for val in range(len(vertex_name_2)):
                        if edges_path_2[i - 1] == vertex_name_2[val]:
                            val = val * it_2 + globals.g_it

                            globals.start = names_new[val]

                    for val in range(len(vertex_name_2)):
                        if edges_path_2[i + 1] == vertex_name_2[val]:
                            val = val * it_2 + globals.g_it

                            globals.end = names_new[val]

                    new_arc_path.append(globals.start)
                    new_arc_path.append('=>')
                    new_arc_path.append(globals.end)

            for i in range(1, len(new_arc_path), 3):
                globals.arc += 1
                arc_new.append('edge{}'.format(globals.arc))

            print(color_new)
            print(names_new)
            print(new_arc_path)
            print(arc_new)
            name = self.vecfirst.text + self.vecsecond.text + 'v'

            ver_del = ','.join(names_new)
            col_del = ','.join(color_new)
            arc_del = ','.join(arc_new)
            ver_tex = ','.join(text_new)
            path = ','.join(new_arc_path)

            XmlParser.add_graph(name, col_del, ver_del, arc_del, path, ver_tex)
            globals.stabilization()

            self.status.text = 'создан граф {}'.format(name)

            globals.g_it = -1
            globals.arc = 0

        except ValueError:
            pass

    def planar(self):
        try:

            if globals.current_graph == None:
                self.status.text = 'найдите нужный граф'
                raise ValueError

            Table.result = None
            Table.bad_minor = None

            edges_path = globals.edges_path[globals.current_graph]
            edges_path = edges_path.split(sep=',')

            G = nx.Graph()
            for i in range(1, len(edges_path), 3):
                G.add_edge(edges_path[i - 1], edges_path[i + 1])

            Table.result = is_planar(G)[0]
            Table.bad_minor = is_planar(G)[1]

            i_i = len(Table.info)
            Table.info.append(Label(text='Планарность графа: {}'.format(Table.result)))
            self.graphinfo.add_widget(Table.info[i_i])

            print('проблемы планарности')
            print(Table.bad_minor)
            nx.draw(G, with_labels=True)
            plt.show()

        except ValueError:
            pass

    def make_it_planar(self):
        try:

            if globals.current_graph == None:
                self.status.text = 'найдите нужный граф'
                raise ValueError

            Table.result = None
            Table.bad_minor = None

            vertex_name = globals.vertex[globals.current_graph]
            vertex_name = vertex_name.split(sep=',')

            vertex_color = globals.color[globals.current_graph]
            vertex_color = vertex_color.split(sep=',')

            vertex_text = globals.text[globals.current_graph]
            vertex_text = vertex_text.split(sep=',')

            edges_path = globals.edges_path[globals.current_graph]
            edges_path = edges_path.split(sep=',')

            edges_name = globals.edges_name[globals.current_graph]
            edges_name = edges_name.split(sep=',')

            G = nx.Graph()
            for i in range(1, len(edges_path), 3):
                G.add_edge(edges_path[i - 1], edges_path[i + 1])

            Table.result = is_planar(G)[0]
            Table.bad_minor = is_planar(G)[1]

            if is_planar(G)[0]:
                self.status.text = 'граф и так планарный '
                raise ValueError

            for i in range(len(vertex_name)):
                if Table.bad_minor[1] == vertex_name[i]:
                    self.delvertex.text = vertex_name[i]
                    self.del_vertex()
                    break

            self.status.text = 'граф стал планарным'

        except ValueError:
            pass

    def change_text(self):
        try:
            if globals.current_graph == None:
                self.status.text = 'найдите нужный граф'
                raise ValueError

            bl = True
            it = None

            vertex_name = globals.vertex[globals.current_graph]
            vertex_name = vertex_name.split(sep=',')

            vertex_text = globals.text[globals.current_graph]
            vertex_text = vertex_text.split(sep=',')

            if self.textvertex.text == '':
                self.status.text = 'введите имя вершины'
                raise ValueError

            if re.search(r'[^a-zA-Z0-9_.+-]', self.textvertex.text):
                self.status.text = 'используйте латиницу'
                raise ValueError

            for i in range(len(vertex_name)):
                if self.textvertex.text == vertex_name[i]:
                    it = i
                    bl = False
                    break

            if bl:
                self.status.text = 'такой вершины нет'
                raise ValueError

            vertex_text[it] = self.textvertexdel.text

            ver_tex = ','.join(vertex_text)
            globals.stabilization()
            XmlParser.change_text(globals.current_graph, ver_tex)
            self.status.text = 'текст изменён'
            globals.stabilization()

        except ValueError:
            pass


def end_of_edge(j, number_of_vertex):
    for i in range(0, globals.Lines):
        if Table.matrix[i][j] == -1:
            return i
        elif Table.matrix[i][j] == 1 and i != number_of_vertex:
            return i
    print('не удалось получить данные из матрицы')
    exit(0)


def dfs(number_of_vertex, time=0):
    if number_of_vertex not in Table.hamiltonian_cycle_del:
        Table.hamiltonian_cycle_del.append(number_of_vertex)

    if len(Table.hamiltonian_cycle_del) == globals.Lines and len(Table.hamiltonian_cycle) == 0:
        for i in Table.hamiltonian_cycle_del:
            Table.hamiltonian_cycle.append(i)

    queue = []  # вершины куда пойдём
    globals.visit[number_of_vertex] = True  # вершины где мы были
    if globals.timer[number_of_vertex] > time:
        globals.timer[number_of_vertex] = time
    for i in range(0, globals.Columns):
        if Table.matrix[number_of_vertex][i] == 1:
            end_of_edges = end_of_edge(i, number_of_vertex)
            if not globals.visit[end_of_edges]:
                queue.append(end_of_edges)

    if number_of_vertex in Table.hamiltonian_cycle_del and len(queue) == 0:
        Table.hamiltonian_cycle_del.remove(number_of_vertex)

    if len(queue) == 0:
        return
    while len(queue) != 0:
        next_vertex = queue[0]
        del queue[0]
        dfs(next_vertex, time + 1)
        if number_of_vertex in Table.hamiltonian_cycle_del and len(queue) == 0:
            Table.hamiltonian_cycle_del.remove(number_of_vertex)
        globals.visit[next_vertex] = False
    if number_of_vertex == globals.root:
        return

        # ScreenManager управляет перемещением между экранами


class ScreenManagerMy(ScreenManager):
    pass


screen_manager = ScreenManager()

# Добавьте экраны к менеджеру, а затем укажите имя
# используется для переключения экранов

screen_manager.add_widget(Table(name="screen_one"))


# Создать класс приложения

class ScreenApp(App):

    def build(self):
        return screen_manager


# запустить приложение
if __name__ == "__main__":
    sample_app = ScreenApp()

    sample_app.run()
