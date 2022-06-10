/*Написать программу по 
созданию, 
просмотру с конца и 
решению поставленной в лаб. работе № 2 
задачи для двунаправленных линейных списков.
*/

/*решению поставленной в лаб. работе № 2 задачи
13. В созданном списке определить максимальное значение и удалить его.*/

#include <iostream>

using namespace std;



class Double_Linked_List
{
private:
    int Size;
    struct Node
    {
        int data;
        Node *pNext,*pPrev; //указатели на пердыдущий и следующий элементы типа Node
        Node(int data=0, Node *pNext=nullptr,Node *pPrev=nullptr) //по умолчанию pNext и pPrev никуда не указывают
        {
            this->data=data;
            this->pNext= pNext;
            this->pPrev=pPrev;
        }
    };
public: 
	void show(Double_Linked_List& My_List);
    Double_Linked_List();
    ~Double_Linked_List();
    int& operator[](const int index);
    int GetSize(){return Size;};
    void clear();
    void pop_front();

    void task();
    void removeAt(int index);
    void push_front(int data);
    void push_back(int data);
    Node *head,*tail;
};

Double_Linked_List::Double_Linked_List()
{
    Size=0;
    head=nullptr;//тк список пуст
    tail=nullptr;
}
Double_Linked_List::~Double_Linked_List()
{
    clear();
}
int& Double_Linked_List::operator[](const int index)
{
    int counter=0;
    Node *current = this->head;
    while(current!=nullptr)
    {
        if(counter==index)
        {
            return current->data;
        }
        current=current->pNext;
        counter++;
    }
}
void Double_Linked_List::clear()
{
    while(Size)
    {
        pop_front();
    }
}
void Double_Linked_List::pop_front()
{
    Node *temp=head;
    head=head->pNext;
    delete temp;
    Size--;
}

void Double_Linked_List::push_back(int data)
{
    if(head==nullptr)//проверяем существует ли первый элемент
    {
        head = new Node(data); //создаем первый элемент
        tail = head; // тк элемент является единствнным ,то он же и будет последним
    }
    else
    {
        Node *current = tail;//временный указатель на хвост

        tail= new Node(data);//создаем новый tail;

        tail->pPrev=current;//присваиваем указатель на предыдущий элемент нового хвоста (им является прошлый tail)
        tail->pNext=nullptr;//у нового хвоста указатель равен nullptr
        current->pNext=tail;//к строму хвосту привязываем координаты нового

    }
    Size++;
}
void Double_Linked_List::push_front(int data)
{
    head = new Node(data, head);//??????????????????
    Size++;
}


void Double_Linked_List::task()
{
	int con = 0,index=0;

	Node* current = this->head;
	int dat = current->data;

	while (current != NULL) 
	{
		if (current->data >= dat) 
		{
			dat = current->data;
			index = con;
		}
		current = current->pNext;
		con++;
	}
	cout << "Index of the largest element : " << index << endl
		<< "Element : " << dat << endl;
	removeAt(index);
    return;    
}
void Double_Linked_List::removeAt(int index)
{
    index++;
    //Если удаляем первый элемент, то могут быть такие варианты
    //В списке есть только первый, в списке есть несколько элементов
    //Поэтому разбиваем логику выполнения
    if ((index == 1) and (head->pNext)) {                     //Если удаляем первый, но есть и другие, то
        Node * temp = head;	                        //Указываем, что нам нужно начало списка
        head = head->pNext;	                            //Сдвигаем начало на следующий за началом элемент
        head->pPrev = NULL;	                            //Делаем так, чтоб предыдущий началу элемент был пустым
        delete temp;		                            //Удаляем удаляемое начало
        Size--;		                                //Обязательно уменьшаем счетчик
        return;		                                //И выходим из функции
    }
    else if ((index == 1) and (head == tail)) {            //Если удаляем первый, но в списке только 1 элемент

        head->pNext = NULL;	                            //обнуляем все что нужно
        tail = NULL;
        delete head;		                            //Удаляем указатель на начало
        Size = 0;		                                //Обязательно обозначаем, что в списке ноль элементов
        return;			                                //и выходим из функции
    }

    //Также может быть, что удаляемый элемент является последним элементом списка
    if (index == Size) {
        Node* temp = tail;	                            //Указываем, что нам нужен хвост
        tail = tail->pPrev;	                                //Отодвигаем хвост немного назад
        tail->pNext = NULL;	                                //Обозначаем, что впереди за хвостом пусто
        delete temp;	                                    //Очищаем память от бывшего хвоста
        Size--;		                                    //Обязательно уменьшаем счетчик элементов
        return;		                                    //И выходим из функции
    }

    //Если же удаляемый элемент лежит где-то в середине списка, то тогда его можно удалить

    Node* temp = head, * temp2;                        //temp-Удаляемый элемент, temp2 нужен, чтобы не потерять данные

        //cout<<count_<<"\n";
    for (int i = 0; i < index - 1; i++) temp = temp->pNext;  //Идем к адресу удаляемого элемента

    temp2 = temp;	                                //Временно запоминаем адрес удаляемого элемента
    temp2->pPrev->pNext = temp->pNext;	            //Записываем данные, что следующий за перед сейчас удаляемым элементом - это следующий от удаляемого
    temp2->pNext->pPrev = temp->pPrev;               //а предыдущий для следующего - это предыдущий для удаляемого
    delete temp;                               //теперь смело можно освободить память, удалив адрес на начало удаляемого элемента
    Size--;                                         //Обязательно уменьшаем число элементов в списке.
}


void Double_Linked_List::show(Double_Linked_List &My_List)
{
		int f;
		cout << endl << "how do you want to see the list" << endl
			<< "Beginning - 1" << endl
			<< "End-2" << endl;


		cin >> f;
		cout << endl;

		if (f == 1)
		{
			Node* time = My_List.head;
			while (time->pNext!=NULL)
			{
				cout << time->data<< " "<<endl;
				time = time->pNext;
			}
			cout << time->data << " " << endl;
		}
		else
		{
			Node* time = My_List.tail;
			while (time->pPrev != NULL)
			{
				cout << time->data << " " << endl;
				time = time->pPrev;
			}
			cout << time->data << " " << endl;
		}
}


int main()
{
	srand(time(NULL));
	Double_Linked_List My_List;
	int c = 10;
	while (c)
	{
		int random_number = (-10) + rand() % 20;
		cout << random_number << " ";
		My_List.push_back(random_number);
		c--;
	}
	cout << endl;
	int choice;
	do
	{
		cout << "What do you want to do?" << endl
			<< "Enter 1 if you want to add element to the list" << endl
			<< "Enter 2 if you want to remove the largest item in the list" << endl
			<< "Enter 3 if you want to see your list" << endl
			<< "Enter 4 if you want to log out" << endl
			<< "ENTER : ";
		cin >> choice;
		switch (choice)
		{
		case 1:
		{
			cout << endl << "Pleas, enter your element : ";
			int element,f;
			cin >> element;
			cout<<endl<<"Beginning - 1"<<endl
				<<"End - 2"<<endl;
			cin>>f;
			if (f==1)
			{
				My_List.push_front(element);
			}
			else
			{
				My_List.push_back(element);
			}
			break;
		}
		case 2:
			My_List.task();
			break;
		case 3:
			My_List.show(My_List);
			break;
		}
	} while (choice != 4);
	return 0;
}

