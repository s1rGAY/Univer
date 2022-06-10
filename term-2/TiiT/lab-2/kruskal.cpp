/*
Входной файл: input.txt
Выходной файл: output.txt
Время на тест: 1 секунда
Ограничение на память: 16 МБ
----------------------------------------------------------------------------
Задан связный неориентированный взвешенный граф G. 
В графе возможно наличие нескольких ребер между одной и той же парой вершин. 
Найдите вес минимального остовного дерева в графе G. 
----------------------------------------------------------------------------
Первая строка входного файла содержит целое число N (1 ≤ N ≤ 10000) - количество вершин графа. 
Вторая строка входного файла содержит целое число M (1 ≤ M ≤ 100000) - количество ребер графа. 

В каждой из следующих M строк содержатся ровно три числа a, b, c (1 ≤ a, b ≤ N, 1 ≤ c ≤ 100000). 
Эти числа описывают ребро, соединяющее вершины с номерами a и b и имеющее вес c. 
Вершины нумеруются последовательными натуральными числами от 1 до N.
*/
//из-за срочности выполнения задния
//код может быть корявым (goto and etc)

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <numeric>
#include <ctime>

using namespace std;

class Graph
{
private:
    int Kruskal_algorithm(uint16_t N)
    {
        Sort();
        vector<uint16_t>Tops;//вектор содержащий все использованные вершины
        vector<uint32_t>Summ;//вектор содержащий цену включенных ребер
        vector<vector<int>>Mnozestva;//мои множества
        Mnozestva.resize(1);


        int i = 0;
        while (Tops.size()!=(N) /*&& Mnozestva.size()!=2*/)
        {
            tryAgain:
            if(find(Tops.begin(),Tops.end(),My_Data[i].my_pair.first) == Tops.end())//Заходим в if, если первая вершина не использовалась
            {

                if(find(Tops.begin(),Tops.end(),My_Data[i].my_pair.second) == Tops.end())//Заходим в if, если вторая вершина не использовалась
                {
                    Mnozestva.resize(Mnozestva.size()+1);//создаем новое множество
                    Mnozestva[Mnozestva.size()-1].push_back(My_Data[i].my_pair.first);//добавляем в наше только что созданое множество вершины
                    Mnozestva[Mnozestva.size()-1].push_back(My_Data[i].my_pair.second);


                    Tops.push_back(My_Data[i].my_pair.first);//добавляю вершины в глобальный массив вершин
                    Tops.push_back(My_Data[i].my_pair.second);
                    Summ.push_back(My_Data[i].c);//добавляю вес ребра к сумме      
                }
                //Done

                else
                //Первая вершина не использовалась ,а вторая использовалась
                {
                    int H=0;
                    while(find(Mnozestva[H].begin(),Mnozestva[H].end(),My_Data[i].my_pair.second)==Mnozestva[H].end())
                    {
                        H++;//находим какому множеству принадлежит вторая вершина
                    }
                    Mnozestva[H].push_back(My_Data[i].my_pair.first);//Добавляю вершину к множеству
                    Tops.push_back(My_Data[i].my_pair.first);//Добавляю мою вершину к глобальному массиву использованных вершин
                    Summ.push_back(My_Data[i].c);//добавляю вес ребра к сумме
                }
                //Done
            }
            //Done

            else//первая вершина использовалась
            {
                if(find(Tops.begin(),Tops.end(),My_Data[i].my_pair.second) == Tops.end())//Заходим в if, если вторая вершина не использовалась
                {
                    int K=0;
                    while(find(Mnozestva[K].begin(),Mnozestva[K].end(),My_Data[i].my_pair.first)==Mnozestva[K].end())
                    {
                        K++;
                    }
                    Mnozestva[K].push_back(My_Data[i].my_pair.second);
                    Tops.push_back(My_Data[i].my_pair.second);
                    Summ.push_back(My_Data[i].c);
                }
                //Done

                else//если вторая вершина тоже использовалась
                {
                    int X=0;
                    while(find(Mnozestva[X].begin(),Mnozestva[X].end(),My_Data[i].my_pair.second)==Mnozestva[X].end())
                    {
                        X++;//находим какому множеству принадлежит вторая вершина
                    }

                    if(find(Mnozestva[X].begin(),Mnozestva[X].end(),My_Data[i].my_pair.first)==Mnozestva[X].end())//если первая верина не принадлежит этому множеству
                    {
                        int G=0;

                        while(find(Mnozestva[G].begin(),Mnozestva[G].end(),My_Data[i].my_pair.first)==Mnozestva[G].end())
                        {
                            G++;//находим какому множеству принадлежит первая вершина
                        }
                        
                        Summ.push_back(My_Data[i].c);
                        for(int j=0;j<Mnozestva[X].size();j++)
                        {
                            //копируем второе в первое
                            Mnozestva[G].push_back(Mnozestva[X][j]);
                        }
                        //удаляю скопированное множество
                        Mnozestva.erase(Mnozestva.begin()+ X);
                    }
                    else
                    {
                        //получим цикл =>ничего не делаем
                    }
                }
            }
            i++;
        }
        if (Mnozestva.size() != 2) { goto tryAgain; };
        //считаем сумму
        int D;
        D=accumulate(Summ.begin(),Summ.end(),0);
        return(D);
    }

    struct Data
    {
        pair<uint16_t,uint16_t>my_pair;
        uint32_t c=0;
    };

    void Sort()
    {
        sort(My_Data.begin(),My_Data.end(),[](const Data&a, const Data&b){return a.c < b.c;});
        cout << "SORTING COMPLETED" << endl;
        cout << endl;
        return;
    }
    //Done

    vector<struct Data>My_Data;


public:

    void SetSize(uint32_t rib)
    {
        My_Data.resize(rib); //изменяю размерость вектора сразу на все ребра
    }
    //Done
    
    void Input(uint16_t a,uint16_t b,uint32_t c,uint32_t i)
    {   
        My_Data[i].my_pair={a,b};
        My_Data[i].c=c;
        return;
    }
    //Done
    
    int MinimalSumTree(int16_t N)
    {
        return(Kruskal_algorithm(N));
    }
    //Done
};


int main()
{
    Graph My_Graph;
    string time;

    ifstream input("13.in");
    getline(input,time,'\n');
    uint16_t N = stoi(time);//вершины

    getline(input,time,'\n');
    uint32_t rib=stoi(time); //ребра

    if(rib!=0)
    {
        My_Graph.SetSize(rib);
    }
    else
    {
        cout<<"0";
        return 0;
    }


    for(uint32_t i=0;i<rib;i++)
    {
        getline(input,time,' ');
        uint16_t a=stoi(time);

        getline(input,time,' ');
        uint16_t b=stoi(time);

        getline(input,time,'\n');
        uint32_t c=stoi(time);        
        My_Graph.Input(a,b,c,i);
    }

    cout<<My_Graph.MinimalSumTree(N);
    return 0;
}

