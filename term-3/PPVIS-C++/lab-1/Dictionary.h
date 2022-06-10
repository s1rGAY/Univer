#pragma once

/*!
    \file
    \brief Заголовочный файл с описанием класса
*/

#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <ctime>
#include <vector>
#include <stdexcept>
using namespace std;

/*!
    \brief Класс словаря
    \author Siarhei Rassafonau
    \version 2.6
    \date Сентябрь 2021 года
    \details Архитектура данного словаря строится на основе бинарного дерева
    \warning Добавление в дерево(словарь) производится при помощи лексикографичекого сравнения слов    
*/
class Dictionary {
private:
    struct node;
    node* root;

    /// \brief производит полную очистку словаря
    node* make_empty(node* t);
    
    /// \brief производит вставку нового элемента в словарь
    node* insert(const string& eng, const string& rus, node* t);
    
    /// \brief производит рекурсивный поиск минимального лексикографического значения и возвращает указатель на данный узел 
    node* find_min(node* t);
    /// \brief производит рекурсивный поиск максимального лексикографического значения и возвращает указатель на данный узел
    node* find_max(node* t);    

    /// \brief производит удаления конкретного элемента(англ. слово и его перевод) по значению англ. слова  из словаря
    node* remove(string del_word, node* t);
     
    /// \briefИспользуя алгоритм прямого обхода дерева, считает количество элементов в нём.
    void size_calculation(node* t, uint16_t& temp_count);
    
    /// \brief Рекурсивно производит поиск узла в котором находится искомое слово. Возвращает найденный узел. 
    node* find(node* t, string search_word);
    
    /// \brief Считывает данные из файла и при помощи функции insert заполняет словарь. А так же пердуперждает, если файл не удалось прочесть
    /*!
    Данные в файле должны быть представлены в следующем виде :
    английское слово
    перевод английского слова на русский
    */
    void filling_from_database(string database_name);

    //рекурсивно копирует
    node* copy(const node* other);

public:
    /// \brief Конструктор по умолчанию.
    /// <summary>
    /// \details Устанавливает первончальное значение для корня.
    /// \code
    /// root = NULL.
    /// \endcode
    /// </summary>
    Dictionary();

    /// \brief Конструктор словаря.
    /// <summary>
    /// \details Создает словарь с изначальными данными.
    /// </summary>
    /// <param name="eng"> английское слово</param>
    /// <param name="rus"> перевод английского слова</param>
    Dictionary(string eng, string rus);

    //// \brief Конструктор словаря.
    /// <summary>
    /// \details Создает словарь с изначальными данными.
    /// </summary>
    /// <param name="eng_rus"> пара состаящая из английского слова и его перевода</param>
    Dictionary(pair<string, string> eng_rus);

    /// \brief Конструктор копирования.
    /// <summary>
    /// \details Производит копированние объекта переданного объекта при помощи приватной функции copy.
    /// \code
    /// this->root = copy(other.root);
    /// \endcode
    /// </summary>
    /// <param name="other"> копируемый словарь</param>
    Dictionary(Dictionary& other);

    /// \brief Деструктор.
    /// <summary>
    /// \details Производит очистку при помощи приватной функции make_empty.
    /// \code
    ///  root = make_empty(root);
    /// \endcode
    /// </summary> 
    ~Dictionary();

    /// \brief Выполняет заполнение словаря из файла.
    /// <summary>
    /// \details Заполнение производится при помощи приватрной функции filling_from_database.
    /// </summary>
    /// <param name="base_name"> название файла без формата</param>
    void database_input(string base_name);

    /// \brief Возвращает размер имещегося словаря.
    /// <summary>
    /// \details Для получения размера использует приватную функцию size_calculation .
    /// </summary>
    /// <returns> Возвращает целое число, которое является размером словаря</returns>
    int get_size();

    /// \brief Производит добавление новых слов в словарь используя оператор >>.
    /// <summary>
    /// \details Данный оператор на вход принимает два слова разделённых пробелам и добавляет данную пару в словарь.
    /// </summary>
    /// <param name="your_dict"> имя словаря в который производится добавление</param>
    friend istream& operator>>(std::istream& in, Dictionary& your_dict);

    /// \brief Данный оператор производит вывод данных о корне словаря.
    /// <summary>
    /// \details Вывод происходит в данной форме :  Английское слово : перевод , ячейка в памяти.
    /// </summary>
    /// <param name="your_dict"> словарь о котором будет выведена информация</param>
    friend ostream& operator<<(std::ostream& out, const Dictionary& your_dict);

    /// \brief Оператор присваивания.
    /// <summary>
    /// \details Производит присваивание значения для переданного объекта.
    /// </summary>
    /// <param name="your_dict"> объект из которого присваивают информацию</param>
    void operator=(const Dictionary& other);

    /// \brief Производит сравнение размеров словарей.
    /// <summary>
    /// \details Возваращает true, если размеры словарей равны, в противном случае возвращает false.
    /// </summary>
    /// <param name="first_dict"> имя первого словаря</param>
    /// <param name="seccond_dict"> имя второго словаря</param>
    /// <returns>Возваращает true, если размеры словарей равны, в противном случае возвращает false</returns>
    friend bool operator== (Dictionary& first_dict, Dictionary& second_dict);

    /// \brief Производит сравнение словарей на основе перегрузки оператора == .
    /// <summary>
    /// \code
    /// return !(first_dict == seccond_dict);
    /// \endcode
    /// </summary>
    /// <param name="first_dict">имя первого словаря</param>
    /// <param name="seccond_dict">имя второго словаря</param>
    /// <returns>Возваращает false, если размеры словарей равны, в противном случае возвращает true</returns>
    friend bool operator!= (Dictionary& first_dict, Dictionary& seccond_dict);

    /// \brief Добавление английского слова и его перевода в словарь.
    /// <summary> 
    /// \details Для добавления используется приватная функция insert.
    /// </summary>
    /// <param name="eng_rus"> пара, в которой первый элемент - английское слово, а второй - его перевод на русский язык</param>
    void operator +=(pair<string, string> eng_rus);

    /// \brief Удаление английского слова и его перевода из словаря.
    /// <summary> 
    /// \details Для удаления используется приватная функция remove.
    /// </summary>
    /// <param name="eng_del_word"> английское слово, которое необходимо удалить</param>
    void operator -=(const string eng_del_word);

    /// \brief Обновление русского перевода для английского слова. 
    /// <summary>
    /// \details При помощи приватной функции find ищет узел в котором хранится слово и его перевод. После нахождения обновляет перевод.
    /// </summary>
    /// <param name="eng_new_rus"> пара в которой первым элементом является английское слово, а вторым его новый перевод на русский язык</param>
    void operator [](const pair<string, string>eng_new_rus);

    /// \brief Поиск перевода английского слова.
    /// <summary>
    /// \details Поиск производится при помощи приватной функции find.
    /// </summary>
    /// <param name="search_eng_word"> анлглийское слово, чей перевод надо найти</param>
    string operator [](const string search_eng_word);
};