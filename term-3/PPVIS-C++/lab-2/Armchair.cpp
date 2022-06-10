#include "Armchair.h"
#include <iostream>

Armchair::Armchair(const int& price, const string& color)
{
	this->type = "Armchair";
	this->price = price;
	this->color = color;
}

Armchair::Armchair()
{
	this->color = "None";
	this->price = 0;
	this->type = "Armchair";
}

string Armchair::get_subject_passport() const
{
	if (footrest) {
		return ("Price : " + to_string(this->price) + ".\n" + "Type : " + this->type + ".\n"
			+ "Color : " + this->color + ".\n" + "Footrest : YES" + ".\n");
	}


	return ("Price : " + to_string(this->price) + ".\n" + "Type : " + this->type + ".\n"
		+ "Color : " + this->color + ".\n" + "Footrest : NO" + ".\n");
}

void Armchair::seat()
{
	cout << "You can seat here!" << endl;
}
