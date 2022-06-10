#include <iostream>
#include <math.h>

using namespace std;

double fun(double x) 
{
	return pow(sin(x),2)-3*(cos(x));
}

double MethodSekuschih(double x1, double x2, double E) 
{
	double res = 0, y = 0;
	do {
		y = res;
		res = x2 - ((x2 - x1) / (fun(x2) - fun(x1))) * fun(x2);
		x1 = x2;
		x2 = res;
	} while (fabs(y - res) > E);
	return	res;
}

int main() {
	int nom = 0;
	setlocale(LC_ALL, "ru");
	double a = -7, b = 3, h = 0.01, eps = 0.001, y;
	cout << "Функция: sin^2(x)-3cos(x)"<<endl;
	for (double x = a; x <= b; x += h) 
	{
		if (fun(x) * fun(x + h) < 0) 
		{
			nom++;
			y = MethodSekuschih(x, x + h, eps);
			cout <<nom<< "-й корень >> " << y << endl;
			cout << "F(" << y << ") = " << fun(y) << endl;;
		}
	}
	if (nom == 0)
	{
		cout << "На отрезке корней нет.\n";
	}
}

