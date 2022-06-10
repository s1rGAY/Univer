#pragma once
#include "Furniture.h"

class Chair : private Furniture {
public:
	Chair(const int& price, const string& color,const int& number_of_legs);
	Chair();
	
	string get_subject_passport()const override;

protected:
	int number_of_legs;
};
