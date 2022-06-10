#include "Bed.h"
#include <iostream>

Bed::Bed(const int& price, const string& color) :
Furniture::Furniture("Bed", price, color)
{
	this->price = price;
	this->color = color;
	this->type = "Bed";
}

Bed::Bed()
{
	this->color = "None";
	this->price = 0;
	this->type = "Bed";
}

void Bed::sleap()
{
	cout << "You can sleep here!" << endl;
}

string Bed::get_subject_passport() const
{
	return ("Price : " + to_string(this->price) + ".\n" + "Type : " + this->type + ".\n"
		+ "Color : " + this->color + ".\n" + "Number of pillow : " + to_string(this->number_of_pillow) + ".\n");;
}

