#pragma once

#include "Furniture.h"

class Armchair : virtual public Furniture {
public:
	Armchair(const int& price, const string& color);
	Armchair();

	virtual string get_subject_passport()const override;

	void seat();

protected:
	bool footrest;
};