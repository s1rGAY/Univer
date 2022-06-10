#include "Chair.h"
#include <string>

Chair::Chair(const int& price, const string& color ,const int& number_of_legs):
Furniture::Furniture("Chair",price, color)
{
	this->number_of_legs = number_of_legs;
}

Chair::Chair()
{
	this->color = "None";
	this->type = "Chair";
	this->price = 0;
}

string Chair::get_subject_passport() const
{
	return ("Price : " + to_string(this->price) + ".\n" + "Type : " + this->type + ".\n"
		+ "Color : " + this->color + ".\n" + "Number of legs : " + to_string(this->number_of_legs) + ".\n");
}
