#pragma once
#include <string>

using namespace std;

class Furniture {
public:

	Furniture(const string& type, const unsigned int& price, const string& color);
	Furniture();

	virtual string get_subject_passport() const = 0;

	string get_color() const;
	int get_price() const;
	string get_type() const;

private:
	string priv_fild;
protected:
	string type;
	unsigned int price;
	string color;
};