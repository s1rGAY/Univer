#include "Furniture.h"
using namespace std;

Furniture::Furniture()
{
	type = 'None';
	price = 0;
	color = 'None';
}

Furniture::Furniture(const string& type, const unsigned int& price,const string& color)
{
	this->type = type;
	this->price = price;
	this->color = color;
}


string Furniture::get_subject_passport() const
{
	return ("Price : " + to_string(this->price) + ".\n" + "Type : " + this->type + ".\n"
		+ "Color : " + this->color + ".\n");
}


string Furniture::get_color() const
{
	return string(this->color);
}
int Furniture::get_price() const
{
	return (this->price);
}
string Furniture::get_type() const
{
	return string(this->type);
}


