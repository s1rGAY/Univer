#include "Table.h"

Table::Table(const int& price, const string& color, const int& length) :
Furniture::Furniture("Table", price, color)
{
	this->length = length;
}

Table::Table()
{
	this->color = "None";
	this->type = "Table";
	this->price = 0;
	this->length = 0;
}

string Table::get_subject_passport() const
{
	return ("Price : " + to_string(this->price) + ".\n" + "Type : " + this->type + ".\n"
		+ "Color : " + this->color + ".\n" + "Length : " + to_string(this->length) + ".\n");
}
