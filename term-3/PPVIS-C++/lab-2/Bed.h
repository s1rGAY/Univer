#pragma once

#include "Furniture.h"

class Bed : virtual public Furniture {
public:
	Bed(const int& price, const string& color);
	Bed();
	void sleap();

	virtual string get_subject_passport()const override;

private:

protected:
	int number_of_pillow;
};