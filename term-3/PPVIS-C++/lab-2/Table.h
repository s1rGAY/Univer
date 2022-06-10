#pragma once

#include "Furniture.h"
using namespace std;

class Table : protected Furniture
{
public:
	Table(const int& price, const string& color, const int& number_of_legs);
	Table();
	string get_subject_passport()const override;
protected:
	int length;
};

