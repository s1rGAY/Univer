// ОАИП Lab1.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
// Вариант 13
/*Написать программу обработки файла типа запись, содержащую следующие пункты меню:
«Создание»-сколько студентов создаем,
«Просмотр»-вывод,
«Коррекция» (добавление новых данных или редактирование старых)
добавление нового студента,
редактирование отметок и тд
 «Решение индивидуального задания».
Каждая запись должна содержать следующую информацию о студентах:
– фамилия и инициалы;
– год рождения;
– номер группы;
– оценки за семестр: по физике, математике;
– средний балл.
Организовать ввод исходных данных, средний балл рассчитать по введенным оценкам.
Содержимое всего файла и результаты решения индивидувльного задания записать в текстовый файл.
*/
//Вычислить общий средний балл студентов интересующей вас группы и распечатать список студентов этой группы, имеющих средний балл выше общего.


#include <iostream>
#include <fstream>
#include <istream>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <vector>
#include <map>
#include <cstdint>

using namespace std;

struct Student_data {
    string Initails;
    int birth;
    int group;
    int math;
    int physics;
    double average;
};

void Clearing(string File_Name){
    ofstream fout(File_Name,ios_base::trunc);
    fout.close();
};
//Completed

void Record (vector<struct Student_data>Data,string File_Name){
    ofstream timing;
    timing.open(File_Name, ios_base::out);
    for (int i=0; i<Data.size();i++){
        timing<<"Student("<<i+1<<") "
        <<Data[i].Initails<<","
        <<Data[i].birth<<","
        <<Data[i].group<<","
        <<Data[i].math<<","
        <<Data[i].physics<<","
        <<Data[i].average<<";"<<endl;
    }
    timing.close();
}
//Completed

vector<struct Student_data> Synchronization (vector<struct Student_data>Data,string File_Name){
    ifstream recording (File_Name,ios_base::in);
    char* str = new char[1024];
    
    int s=0;
    while (!recording.eof()) {
        recording.getline(str, 1024, '\n');
        s++;
    }
    recording.close();
    s -= 1;//тк getline считает +1 строку от заполненых
    Data.resize(s);
    int i = 0;

    ifstream record (File_Name,ios_base::in);
    while(!record.eof()&&i!=Data.size()){      
        string value;    

        getline(record,value,' ');
        getline(record,Data[i].Initails,',');

        getline(record,value,',');
        Data[i].birth=stoi(value);

        getline(record,value,','); //stoi out of range!
        Data[i].group=stoi(value);

        getline(record,value,',');
        Data[i].math=stoi(value);

        getline(record,value,',');
        Data[i].physics=stoi(value);

        getline(record,value,';');
        Data[i].average=stoi(value);
        i++;
    }
    record.close();
    return Data;
};  
//Completed

vector<struct Student_data> File_work(string File_Name,vector<struct Student_data>Data){
    ifstream file;
    file.open(File_Name);
    if(!file){ //если file=false создаем файл
        ofstream created_file(File_Name);
        created_file.close();
    }
    else{
        Data=Synchronization(Data, File_Name);
        file.close();//если file=true просто закрываем поток
    }
    return Data;
};
//Completed

vector<struct Student_data> Сreate(vector<struct Student_data>Data,string File_Name) {
    ofstream timing;
    timing.open(File_Name, ios::app);
    
    cout << "How many students do you want to create?" << endl;
    int number_of_students;
    cin >> number_of_students;

    int i=Data.size(); 
    Data.resize(i+number_of_students);

    for (i; i < Data.size(); i++) { //3 ,3 => ошибка   for (i; i < number_of_students; i++)   Data.size()
        
        cout<<"Student number : "<<i+1<<endl;
        cout << "Please, enter Name : ";
        cin >> Data[i].Initails;
        cout << "Please, enter Bitrh : ";
        cin >> Data[i].birth;
        cout << "Please, enter group : ";
        cin >> Data[i].group;
        cout << "Please, enter MATH mark : ";
        cin >> Data[i].math;
        cout << "Please, enter PHYSICS mark : ";
        cin >> Data[i].physics;
        Data[i].average = (static_cast<double>(Data[i].math+Data[i].physics)/2);
        timing<<"Student("<<i+1<<") " //раньше ("<<i+1<<") ,"
        <<Data[i].Initails<<","
        <<Data[i].birth<<","
        <<Data[i].group<<","
        <<Data[i].math<<","
        <<Data[i].physics<<","
        <<Data[i].average<<";"<<endl; 
    }
    timing.close();
    return Data;
};
//Completed

void Viewing(string File_Name) {
    cout<<endl;
    string line;
    ifstream read (File_Name);
    if (read.is_open()){
        while (! read.eof()){
            getline (read,line);
            cout << line << endl;
        }
        read.close();
    }
}
//Completed

vector<struct Student_data> Correction(vector<struct Student_data>Data,string File_Name) {
    Data=Synchronization(Data,File_Name);
    cout<<endl<<"You can : "<<endl<<
    "Correct student data (enter 1) "<<endl<<
    "Add new student (enter 2) "<<endl<<
    "Enter : ";
    int operation,nomber,value,selection;
    cin>>operation;
    string f;

    bool C=false;
    switch (operation){
    case 1:
        cout<<"Please enter nomber of student : ";
        cin>>nomber;
        //Coorect data student data
        
        do{
            cout<<endl<<"What do you want to correct?"<<endl<<endl;
            cout<<"Initails (enter 1)"<<endl
                <<"Bitrh (enter 2)"<<endl
                <<"Group (enter 3)"<<endl
                <<"Math (enter 4)"<<endl
                <<"Physics (enter 5)"<<endl
                <<"Exit = 6"<<endl
                <<"Enter : ";         
            cin >>selection;        
            Clearing(File_Name);
            switch(selection){             
                case 1:
                    cout<<"Enter new value : ";
                    cin>>f;
                    Data[nomber-1].Initails=f;
                break;
                case 2:
                    cout<<"Enter new value : ";
                    cin>>value;
                    Data[nomber-1].birth=value;
                break;
                case 3:
                    cout<<"Enter new value : ";
                    cin>>value;
                    Data[nomber-1].group=value;
                break;
                case 4:
                    cout<<"Enter new value : ";
                    cin>>value;
                    Data[nomber-1].math=value;
                    Data[nomber-1].average=(static_cast<double>(Data[nomber-1].math+Data[nomber-1].physics)/2);
                break;
                case 5:
                    cout<<"Enter new value : ";
                    cin>>value;
                    Data[nomber-1].physics=value;
                    Data[nomber-1].average=(static_cast<double>(Data[nomber-1].math+Data[nomber-1].physics)/2);
                break;
                case 6:
                    C=true;        
                break; 
                default:
                    cout << "Your choice isn't correct" << endl;
                break;
            }
            Record(Data,File_Name);         
        }
        while (!C);
        return Data;      
    break;
    case 2:
        Data=Сreate(Data,File_Name);
    break;
    default:
        cout << "Your choice isn't correct" << endl;
    break;
    }
    return Data;
}
//Completed

void Laba(vector<struct Student_data>Data){   
    int nomber;
    vector<double>Average;
    cout<<endl<<"Enter group number : ";
    cin>>nomber;
    double Group_Average=0;
    map<int,double>Group;
    
    for(int i=0;i<Data.size();i++){
        if(Data[i].group==nomber){
            Group[i]=Data[i].average;
            Group_Average+=Data[i].average;
        }
    }
    /*for (const auto& s: Data){        
        if(Data[i].group=nomber){       
            Group[i]=Data[i].average; 
            Group_Average+=Data[i].average;
        }
        i++;
    }*/

    Group_Average=static_cast<double>(Group_Average/Group.size());
    cout<<"Group Average : "<<Group_Average<<endl;
    cout<<endl;
    cout<<"Nomber of students with average which more than Group Average : ";
    for (int i=0;i<Group.size();i++){
        if(Group[i]>Group_Average){
            cout<<i+1<<"; ";
        }
    }
    cout<<endl;
}
//Completed

int main() {
    string File_Name;
    cout<<"Please, enter the file Name : ";
    cin>>File_Name;
    File_Name+=".txt";

    vector<struct Student_data>Data;

    Data = File_work(File_Name,Data); //проверка существования файла (if flase => его создание)
    //синхронизация с содержимым файла
    
    cout << "What do you want to do?" << endl;
    int choice;
    bool c=false;
    

    do{   
        cout <<endl<< 
        "You can :" << endl <<
        "Create (enter 1)" << endl <<
        "Viewing (enter 2)" << endl <<
        "Correction (enter 3)" << endl <<
        "Laba (enter 4)"<<endl<<
        "Exit = 5"<<endl<<
        "Enter : ";
        cin >> choice;
        switch (choice) {
        case 1:
            Data = Сreate(Data,File_Name);
        break;
        case 2:
            Viewing(File_Name);
        break;
        case 3:
            Data = Correction(Data,File_Name);
        break;
        case 4:
            Laba(Data);
        break;
        case 5:
            c=true;
        default:
            cout << "Your choice isn't correct" << endl;
        break;
        }  
    } 
    while (!c);      
    return 0;
}
//Completed
