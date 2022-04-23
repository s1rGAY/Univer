from typing import Text
from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# custom module
from controllers import TournamentController


class MyApp(App):
    def __init__(self, controller: TournamentController):
        self.general_properties = {
            "COLUMNS": 7,
            "ROWS": 5,
            "CURRENT": 1,
            "count": 0, # для корректного вывода виджетов
            'rightDoubleButton': None,
            'leftDoubleButton': None,
            'SEARCH': {
                'search_1th': { #  (Столбец, Элемент)
                    "input_column": None,
                    "input_elem": None
                },
                'search_2th': { #  (Столбец, Элемент)
                    "input_fio": None,
                    "search_button": None
                },
                'search_3th': { #  (Столбец, Элемент)
                    "input_min": None,
                    "input_max": None,
                    "search_button": None
                },
            },
            'DELETE': {
                'delete_1th': { #  (Столбец, Элемент)
                    "input_column": None,
                    "input_elem": None
                },
                'delete_2th': { #  (Столбец, Элемент)
                    "input_fio": None,
                    "delete_button": None
                },
                'delete_3th': { #  (Столбец, Элемент)
                    "input_min": None,
                    "input_max": None,
                    "delete_button": None
                },
            },
            'ADD': {
                "add_button": None,
                "input_1": None,
                "input_2": None,
                "input_3": None,
                "input_4": None,
                "input_5": None,
                "input_3_1": None,
                "dropDown": None,
            },
            'SAVE': {
                'input_way': None, # (путь,название файла)
                'file_name': None, # (путь,название файла)
                'save_data': None, # (путь,название файла)

            },
            'OPEN': {
                'input_path': None, # (название файла)
                'open_data': None # кнопка
            },
            "SETTINGS": {
                "justBack": None,
                "clearFiltres": None,
                "refreshTable": None,
                "logStatus": None, 
            },
            'bxMain': None,
            'bxSettings': None,
            'bxTableHeader': None,
            'bxTableAction':None,
            'bxTablebutton': None,
            'gridTable': None,
        }
        super().__init__()
        self.controller = controller
        controller.init_viewer(self.general_properties)
        self.general_properties["count"] = 0
        self.general_properties["COLUMNS"] = 7
        self.general_properties["ROWS"] = 5
        self.general_properties["CURRENT"] = 1
        self.general_properties["bxMain"] = BoxLayout(orientation="vertical")
        self.general_properties["bxTableHeader"] = BoxLayout(orientation="horizontal", size_hint=(1, 0.2))
        self.general_properties["bxTableAction"] = BoxLayout(orientation="horizontal", size_hint=(1, 0.1))
        self.general_properties["bxTablebutton"] = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.general_properties["gridTable"] = GridLayout(cols=7, rows=7)
        self.general_properties["bxSettings"] = BoxLayout(size_hint = (1, 0.085))
        self.general_properties["ADD"]["dropDown"] = DropDown()


    def getProperties(self):
      return self.general_properties

    def build(self):
        self.settingButton()
        self.general_properties["bxMain"].add_widget(self.general_properties["bxSettings"])

        header = [Label(text="Номер поезда"), Label(text="Станция\nотправления"), Label(text="Станция\nприбытия"), Label(text="Дата и\nвремя\nотправления"),
                  Label(text="Дата и\nвремя\nприбытия"), Label(text="Время в\nпути")]
        for i in range(len(header)):
            self.general_properties["bxTableHeader"].add_widget(header[i])
        
        self.base_buttons()  # build buttons
        self.controller.rewrite()
        self.general_properties["bxMain"].add_widget(self.general_properties["bxTableHeader"])
        self.general_properties["bxMain"].add_widget(self.general_properties["gridTable"])
        self.general_properties["bxMain"].add_widget(self.general_properties["bxTableAction"])
        self.general_properties["bxMain"].add_widget(self.general_properties["bxTablebutton"])

  
        return self.general_properties["bxMain"]

    def settingButton(self):
        self.general_properties["SETTINGS"]["clearFiltres"] = Button(size_hint = (0.2, 1), text = "Clear filtres")
        self.general_properties["SETTINGS"]["clearFiltres"].on_press = self.controller.clearFilter
        self.general_properties["SETTINGS"]["refreshTable"] = Button(size_hint = (0.2, 1), text = "Refresh table")
        self.general_properties["SETTINGS"]["refreshTable"].on_press = self.controller.rewrite
        self.general_properties["SETTINGS"]["logStatus"] = Label()

        self.general_properties["bxSettings"].add_widget(self.general_properties["SETTINGS"]["clearFiltres"])
        self.general_properties["bxSettings"].add_widget(self.general_properties["SETTINGS"]["refreshTable"])
        self.general_properties["bxSettings"].add_widget(self.general_properties["SETTINGS"]["logStatus"])

    def base_buttons(self):        
        rightDoubleButton = Button(size_hint=(0.5, 1), text='>>')
        leftDoubleButton = Button(size_hint=(0.5, 1), text='<<')

        rightDoubleButton.on_press = self.controller.rightDoubleClick
        leftDoubleButton.on_press = self.controller.leftDoubleClick

        self.general_properties["rightDoubleButton"] = rightDoubleButton
        self.general_properties["leftDoubleButton"] = leftDoubleButton

        leftButton = Button(text="<")
        leftButton.on_press = self.controller.leftClick

        rightButton = Button(text=">")
        rightButton.on_press = self.controller.rightClick

        # open
        openButton = Button(text='Open')
        openButton.on_press = self.open_button
        # Add
        addButton = Button(text='Add')
        addButton.on_press = self.add_button
        # Save
        saveData = Button(text='Save')
        saveData.on_press = self.save_button
        # delete
        deleteData = Button(text='Delete some info')
        deleteData.on_press = self.del_some
        # search
        searchData = Button(text='Search some info')
        searchData.on_press = self.search_some
        # back
        justBack = Button(text='<-back')
        justBack.on_press = self.back

        self.general_properties["justBack"] = justBack

        TableActionList = [leftButton, leftDoubleButton, rightDoubleButton, rightButton]
        TableButtonList = [justBack, searchData, deleteData, addButton, saveData, openButton]

        for i in range(len(TableActionList)):
            self.general_properties["bxTableAction"].add_widget(TableActionList[i])

        for i in range(len(TableButtonList)):
            self.general_properties["bxTablebutton"].add_widget(TableButtonList[i])

    ##########################################################################################################################
    def adder_on_condition(self, mass):
        for i in range(len(mass)):
            self.condition.add_widget(mass[i])

    def example(self):
        pass
#????????????????????????????????????????????????????????????????????????????????????????????????????????????
    def search_some(self):
        self.back()
        self.condition = BoxLayout(size_hint=(1, 0.1))

        Search_1 = Button(text='По номеру поезда')
        Search_1.on_press = self.search_1

        Search_2 = Button(text='По дате отправления')
        Search_2.on_press = self.search_2

        Search_3 = Button(text='По времени отправления')
        Search_3.on_press = self.search_3

        Search_4 = Button(text='По времени прибытия')
        Search_4.on_press = self.search_3

        Search_5 = Button(text='По станции отправления')
        Search_5.on_press = self.search_3

        Search_6 = Button(text='По станции прибытия')
        Search_6.on_press = self.search_3

        Search_7 = Button(text='По времени в пути')
        Search_7.on_press = self.search_3


        self.adder_on_condition([Search_1,Search_2,Search_3])
        self.general_properties["bxMain"].add_widget(self.condition)
        self.general_properties["count"] += 1

    def search_1(self):
        self.back()
        self.condition = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        input_column = Button(text='ID')
        input_elem = TextInput(hint_text='value')

        self.general_properties["SEARCH"]["search_1th"]["input_column"] = input_column
        self.general_properties["SEARCH"]["search_1th"]["input_elem"] = input_elem
        dropdown = DropDown()

        compare = {
          "ID": "id",
          "Название турнира": "name_tournament",
          "Дата проведения": "date",
          "Название вида спорта": "type_tournament",
          "ФИО победителя": "fio",
          "Размер призовых турнира": "price_tournament",
          "Название турнира": "name_tournament",
          "Заработок победителя (60% от размера призовых)": "price",
        }

        for index in compare:
          btn = Button(text=index, size_hint_y=None, height=44)
          btn.bind(on_release=lambda btn: dropdown.select(btn.text))
          dropdown.add_widget(btn)

        input_column.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(input_column, 'text', x))
        
        search_1th = Button(text="Search")
        search_1th.on_press = self.controller.filterDataSearch_1

        self.adder_on_condition([input_column, input_elem, search_1th])
        self.general_properties["bxMain"].add_widget(self.condition)
        self.controller.rewrite()
        self.general_properties["count"] += 1

    def search_2(self):
        self.back()
        self.condition = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        input_fio = TextInput(hint_text='some')
        search_button = Button(text="Search")

        self.general_properties["SEARCH"]["search_2th"]["input_fio"] = input_fio
        self.general_properties["SEARCH"]["search_2th"]["search_button"] = search_button

        search_button.on_press = self.controller.filterDataSearch_2

        self.adder_on_condition([input_fio, search_button])
        self.general_properties["bxMain"].add_widget(self.condition)
        self.controller.rewrite()
        self.general_properties["count"] += 1

    def search_3(self):
        self.back()
        self.condition = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        input_min = TextInput(hint_text='Нижний предел')
        input_max = TextInput(hint_text='Верхний предел')

        self.general_properties["SEARCH"]["search_3th"]["input_min"] = input_min
        self.general_properties["SEARCH"]["search_3th"]["input_max"] = input_max

        search_3th = Button(text="Search")

        search_3th.on_press = self.controller.filterDataSearch_3

        self.general_properties["SEARCH"]["search_3th"]["search_button"] = search_3th

        # search.on_press = self.search_on_press

        self.adder_on_condition([input_min, input_max, search_3th])
        self.general_properties["bxMain"].add_widget(self.condition)
        self.controller.rewrite()
        self.general_properties["count"] += 1

    def add_button(self):
        self.back()
        self.condition = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        boxTypeTournament = BoxLayout(orientation = "vertical")

        self.general_properties["ADD"]["add_button"] = Button(text="Add")

        self.general_properties["ADD"]["add_button"].on_press = self.controller.insertData

        self.general_properties["ADD"]["input_1"] = TextInput(hint_text = "Номер поезда")
        self.general_properties["ADD"]["input_2"] = TextInput(hint_text = 'Станция отправления')
        self.general_properties["ADD"]["input_3"] = TextInput(hint_text = "Станция прибытия")
        self.general_properties["ADD"]["input_3_1"] = TextInput(hint_text = 'Дата и время\n отпарвления')
        self.general_properties["ADD"]["input_4"] = TextInput(hint_text = "Дата и время\n прибытия")
        #self.general_properties["ADD"]["input_5"] = TextInput(hint_text = "Price")

        self.general_properties["ADD"]["dropDown"].bind(on_select=lambda instance, x: setattr(self.general_properties["ADD"]["input_3"], 'text', x))
        self.general_properties["ADD"]["input_3_1"].bind(on_release=self.general_properties["ADD"]["dropDown"].open)

        boxTypeTournament.add_widget(self.general_properties["ADD"]["input_3"])
        boxTypeTournament.add_widget(self.general_properties["ADD"]["input_3_1"])

        self.condition.add_widget(self.general_properties["ADD"]["input_1"] )
        self.condition.add_widget(self.general_properties["ADD"]["input_2"] )
        self.condition.add_widget(boxTypeTournament)
        self.condition.add_widget(self.general_properties["ADD"]["input_4"] )
        #self.condition.add_widget(self.general_properties["ADD"]["input_5"] )
        self.condition.add_widget(self.general_properties["ADD"]["add_button"])

        self.general_properties["bxMain"].add_widget(self.condition)
        self.controller.rewrite()
        self.general_properties["count"] += 1
#???????????????????????????????????????????????????????????????????????????????????????????????????????
    def del_some(self):
        self.back()
        self.condition = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        Del_1 = Button(text='По номеру поезда')
        Del_1.on_press = self.del_1

        Del_2 = Button(text='По времени отправления')
        Del_2.on_press = self.del_2

        Del_2 = Button(text='По времени прибытия')
        Del_2.on_press = self.del_2

        Del_3 = Button(text='По станции отправления')
        Del_3.on_press = self.del_3

        Del_3 = Button(text='По станции прибытия')
        Del_3.on_press = self.del_3

        Del_3 = Button(text='По времени в пути')
        Del_3.on_press = self.del_3

        self.adder_on_condition([Del_1, Del_2, Del_3])
        self.general_properties["bxMain"].add_widget(self.condition)
        self.general_properties["count"] += 1

    def del_1(self):
        self.back()
        self.condition = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        input_column = Button(text='ID')
        input_elem = TextInput(hint_text='value')

        self.general_properties["DELETE"]["delete_1th"]["input_column"] = input_column
        self.general_properties["DELETE"]["delete_1th"]["input_elem"] = input_elem
        dropdown = DropDown()

        compare = {
          "ID": "id",
          "Название турнира": "name_tournament",
          "Дата проведения": "date",
          "Название вида спорта": "type_tournament",
          "ФИО победителя": "fio",
          "Размер призовых турнира": "price_tournament",
          "Название турнира": "name_tournament",
          "Заработок победителя (60% от размера призовых)": "price",
        }

        for index in compare:
          btn = Button(text=index, size_hint_y=None, height=44)
          btn.bind(on_release=lambda btn: dropdown.select(btn.text))
          dropdown.add_widget(btn)

        input_column.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(input_column, 'text', x))
        
        search_1th = Button(text="Delete")
        search_1th.on_press = self.controller.filterDataDelete_1

        self.adder_on_condition([input_column, input_elem, search_1th])
        self.general_properties["bxMain"].add_widget(self.condition)
        self.controller.rewrite()
        self.general_properties["count"] += 1


    def del_2(self):
        self.back()
        self.condition = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        input_fio = TextInput(hint_text='some')
        search_button = Button(text="Delete")

        self.general_properties["DELETE"]["delete_2th"]["input_fio"] = input_fio
        self.general_properties["DELETE"]["delete_2th"]["delete_button"] = search_button

        search_button.on_press = self.controller.filterDataDelete_2

        self.adder_on_condition([input_fio, search_button])
        self.general_properties["bxMain"].add_widget(self.condition)
        self.controller.rewrite()
        self.general_properties["count"] += 1


    def del_3(self):
        self.back()
        self.condition = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        input_min = TextInput(hint_text='Нижний предел')
        input_max = TextInput(hint_text='Верхний предел')

        self.general_properties["DELETE"]["delete_3th"]["input_min"] = input_min
        self.general_properties["DELETE"]["delete_3th"]["input_max"] = input_max

        search_3th = Button(text="Delete")

        search_3th.on_press = self.controller.filterDataDelete_3

        self.general_properties["DELETE"]["delete_3th"]["delete_button"] = search_3th

        # search.on_press = self.search_on_press

        self.adder_on_condition([input_min, input_max, search_3th])
        self.general_properties["bxMain"].add_widget(self.condition)
        self.controller.rewrite()
        self.general_properties["count"] += 1

    def back(self):
        if self.general_properties["count"] != 0:
            self.general_properties["bxMain"].remove_widget(self.condition)
            self.general_properties["count"] -= 1
        else:
          pass

    def save_button(self):
        self.back()
        self.condition = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        input_way = TextInput(hint_text='Путь (home/.../)')
        file_name = TextInput(hint_text='Название файла (<...>.<format>)')
        save_data = Button(size_hint=(0.5, 1), text="Save data")

        self.general_properties["SAVE"]["input_way"] = input_way
        self.general_properties["SAVE"]["file_name"] = file_name
        self.general_properties["SAVE"]["save_data"] = save_data

        self.general_properties["SAVE"]["save_data"].on_press = self.controller.saveData

        self.adder_on_condition([input_way, file_name, save_data])
        self.general_properties["bxMain"].add_widget(self.condition)
        self.controller.rewrite()
        self.general_properties["count"] += 1

    def open_button(self):
        self.back()
        self.condition = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        file_name = TextInput(hint_text='Путь к файлу (home/.../<name>.<format>)')
        open_data = Button(size_hint=(0.5, 1), text="Open data")

        self.general_properties["OPEN"]["input_path"] = file_name
        self.general_properties["OPEN"]["open_data"] = open_data

        self.general_properties["OPEN"]["open_data"].on_press = self.controller.openFile

        self.condition.add_widget(file_name)
        self.condition.add_widget(open_data)

        self.general_properties["bxMain"].add_widget(self.condition)
        self.controller.rewrite()
        self.general_properties["count"] += 1