#pragma once

#include "Armchair.h"
#include "Bed.h"
#include <iostream>

class Armchair_bed : public Bed, public Armchair {

public:

	Armchair_bed(const int& price, const string& color);

	virtual string get_subject_passport()const override; //тут прикол короче

protected:

private:

};

