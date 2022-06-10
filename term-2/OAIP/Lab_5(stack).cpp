#include <iostream>
#include <sstream>
#include <map>
#include <ctime>
#include <list>

using namespace std;

class Stack {
public:
	Stack();
	~Stack();
	void removeAt(int index);
	int& operator[](const int index);
	void pop_front();
	void clear();
	void push_front(int data);
	int Size() const {
		return size;
	}
	int task();
	void sort_adress();
	void sort_info();
	struct Node { //был class
		Node *pNext;
		int data;
		Node(int data = 0, Node* pNext = nullptr) {
			this->data = data;
			this->pNext = pNext;
		}
	};
	Node* head;
	int size;
};

Stack::Stack()
{
	size = 0;
	head = nullptr;
}
Stack::~Stack(){
	clear();	
}

int& Stack::operator[](const int index){
	Node* current = this->head;
	int count = 0;
	while (current != nullptr) {
		if (count == index) {
			return current->data;
		}
		current = current->pNext;
		count++;
	}
}

void Stack::pop_front(){
	Node* temp = head;
	head = head->pNext;
	delete temp;
	size--;
}

void Stack::clear(){
	while (size) {
		pop_front();
	}
}

void Stack::push_front(int data){
	head = new Node(data,head);
	size++;
}


void Stack::removeAt(int index)
{
	if (index == 0)
	{
		pop_front();
	}
	else
	{
		Node* previous = this->head;
		for (int i = 0; i < index - 1; i++)
		{
			previous = previous->pNext;
		}
		Node* toDelete = previous->pNext;
		previous->pNext = toDelete->pNext;
		delete toDelete;
		size--;
	}
}
//удаляем эл-т по индесу


int Stack::task() {
	int con = 0,index=0;

	Node* current = this->head;
	int dat = current->data;

	while (current != nullptr) {

		if (current->data >= dat) {
			dat = current->data;
			index = con;
		}
		current = current->pNext;
		con++;
	}
	cout << "Index of the largest element : " << index << endl
		<< "Element : " << dat << endl;
	removeAt(index);
	return 0;
}

void Stack::sort_adress(){
	Node* t = NULL, * t1, * r;
	Node** p = &this->head;
	if ((*p)->pNext->pNext == NULL) return;
	do {
		for (t1 = *p; t1->pNext->pNext != t; t1 = t1->pNext)
			if (t1->pNext->data > t1->pNext->pNext->data) {
				r = t1->pNext->pNext;
				t1->pNext->pNext = r->pNext;
				r->pNext = t1->pNext;
				t1->pNext = r;
			}
		t = t1->pNext;
	} while ((*p)->pNext->pNext != t);

}

void Stack::sort_info(){
	Node* t = NULL, * t1;
	Node* p = this->head;
	int r;
	do {
		for (t1 = p; t1->pNext != t; t1 = t1->pNext)
			if (t1->data > t1->pNext->data) {
				r = t1->data;
				t1->data = t1->pNext->data;
				t1->pNext->data = r;
			}
		t = t1;
	} while (p->pNext != t);
}





int main()
{
	srand(time(NULL));
	Stack My_List;
	int c = 20;
	while (c)
	{
		int random_number = (-10) + rand() % 20;
		My_List.push_front(random_number);
		c--;
	}
	//заполняем список
	int choice;
	do
	{
		cout << "What do you want to do?" << endl
			<< "Enter 1 if you want to add element to the list" << endl
			<< "Enter 2 if you want to remove the largest item in the list" << endl
			<< "Enter 3 if you want to see your list" << endl
			<< "Enter 4 if you want to sort your list"<<endl
			<< "Enter 5 if you want to log out" << endl
			<< "ENTER : ";
		cin >> choice;
		switch (choice)
		{
		case 1:
			cout << endl << "Pleas, enter your element : ";
			int element;
			cin >> element;
			My_List.push_front(element);
			break;
		case 2:
			My_List.task();
			break;
		case 3:
			for (int i = 0; i < My_List.Size(); i++)
			{
				cout << My_List[i] << ", ";
			}
			cout << endl;
			break;
		case 4:
			cout << "Sort permutation of addresses-1, exchange of information between the current and the next item -2)" << endl;
			int a;
			cin >> a;
			if (a == 1) 
			{
				cout << "Elements of stack : \n";
				My_List.push_front(2);
				My_List.sort_adress();
				My_List.pop_front();
				for (int i = 0; i < My_List.Size(); ++i) {
					cout << My_List[i] << endl;
				}
				cout << "\n";
			}
			else if (a == 2) 
			{
				cout << "STACK : \n";
				My_List.sort_info();
				for (int i = 0; i < My_List.Size(); ++i) 
				{
					cout << My_List[i] << endl;
				}
			}
			break;
		}
	} while (choice != 5);
	//меню
	return 0;
}
