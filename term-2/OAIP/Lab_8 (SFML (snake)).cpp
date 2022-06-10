#include <SFML/Graphics.hpp>
#include <algorithm>
#include <deque>
#include <time.h>
#include <iostream>
#include <vector>





using namespace sf;
using namespace std;



struct Point
{
	int x, y;
	Point()
	{
		x = y = 0;
	}
	Point(int x, int y)
	{
		this->x = x;
		this->y = y;
	}
};

struct Colors
{
	int x;
	int y;
	int z;

	Colors(int x, int y, int z)
	{
		this->x = x;
		this->y = y;
		this->z = z;
	}
	Colors()
	{
		x = y = z = 0;
	}
};


//параметры для цвета
vector<Colors>Colors_vect;
short int color_one = rand() % 255;
short int color_two = rand() % 255;
short int color_tree = rand() % 255;

//параментры игры
const unsigned short int ROW = 30;//строки 
const unsigned short int COLUMN = 30;//колонки
const unsigned short int TILE_SIZE = 35;//размер окна
const unsigned short int DELAY = 100;//скорость змеи (чем ниже тем больше)
unsigned short int dir = 4; //параметр управляющий направлением змеи [от 0-3] 4-пауза

//параметры окна
RenderWindow win(VideoMode(COLUMN* TILE_SIZE + TILE_SIZE, ROW* TILE_SIZE + TILE_SIZE), "MY GAME SNAKE"); 

//создаем fruct
Point fruct;

//создаем змейю
deque<Point> snakes; //в виде дека (двусторонняя очередь, чтоб добавлять эл-ты быстрее) хронящей поинты


//задаем местоположение фрукта
void SetFruct()
{
	fruct.x = rand() % (COLUMN /*+ 1*/);
	fruct.y = rand() % (ROW /*+ 1*/);
	for (auto snake : snakes)
	{
		if (snake.x == fruct.x && snake.y == fruct.y) //если фрукт выпал на нашу змею, то перемещаем его с неё
		{
			fruct.x = rand() % (COLUMN /*+ 1*/);
			fruct.y = rand() % (ROW /*+ 1*/);
		}
	}
}

//начало игры
void Start()
{
	snakes.clear(); //в начале игры очищаем нашу змею
	Colors_vect.clear();

	snakes.push_back(Point(COLUMN / 2, ROW / 2)); //задаем размер 1 в центре поля

	Colors start(color_one,color_two,color_tree);//создаем первый свет
	Colors_vect.push_back(start);//добавляем его в вектор цветов

	SetFruct();//создаем фрукт
}

//управление
void UpdateKeyboard()
{
	if ((Keyboard::isKeyPressed(Keyboard::A)|| 
		 Keyboard::isKeyPressed(Keyboard::Left)) && dir != 2)
		dir = 0;
	else if ((Keyboard::isKeyPressed(Keyboard::W)||
			  Keyboard::isKeyPressed(Keyboard::Up)) && dir != 3)
		dir = 1;
	else if ((Keyboard::isKeyPressed(Keyboard::D)||
			  Keyboard::isKeyPressed(Keyboard::Right)) && dir != 0)
		dir = 2;
	else if ((Keyboard::isKeyPressed(Keyboard::S)||
			  Keyboard::isKeyPressed(Keyboard::Down)) && dir != 1)
		dir = 3;
	else if (Keyboard::isKeyPressed(Keyboard::Space))
		dir = 4;
}

//условия игры
void UpdateCollision()
{
	//если голова смеи совпадает по координатам с фруктом (рост змеи)
	if (snakes[0].x == fruct.x && snakes[0].y == fruct.y) 
	{
		//добаляем цвет старого фрукта в змею
		Colors temp_color = {color_one,color_two,color_tree};
		Colors_vect.push_back(temp_color);

		//задаем новый фрукт
		SetFruct();
		color_one = rand() % 255;
		color_two = rand() % 255;
		color_tree = rand() % 255;
		snakes.push_back(Point(snakes[snakes.size() - 1].x, snakes[snakes.size() - 1].y));//рост змеии
	}
	
	//конец игры если змея врежется в стенку
	else if (snakes[0].x > COLUMN || snakes[0].x < 0 || snakes[0].y > ROW || snakes[0].y < 0)
	{
		Start();
	}
	
	//конец игры если змея врежется в саму себя
	for (size_t i = 4; i < snakes.size(); ++i)
	{
		if (snakes[0].x == snakes[i].x && snakes[0].y == snakes[i].y)
		{
			Start();
		}
	}
}

//перемещение змеи
void Update()
{
	switch (dir)
	{
	case 0:
		snakes.push_front(Point(snakes[0].x - 1, snakes[0].y));
		snakes.pop_back();
		break;
	case 1:
		snakes.push_front(Point(snakes[0].x, snakes[0].y - 1));
		snakes.pop_back();
		break;
	case 2:
		snakes.push_front(Point(snakes[0].x + 1, snakes[0].y));
		snakes.pop_back();
		break;
	case 3:
		snakes.push_front(Point(snakes[0].x, snakes[0].y + 1));
		snakes.pop_back();
		break;
	}
	UpdateCollision();
}

//прорисовка карты и фрукта
void Draw()
{
	RectangleShape tmp(Vector2f(TILE_SIZE, TILE_SIZE));

	for (size_t i = 0; i <= ROW; ++i)
	{
		//задание цвета квадратных ориентиров
		for (size_t j = 0; j <= COLUMN; ++j)
		{
			tmp.setPosition(j * TILE_SIZE, i * TILE_SIZE);
			if (i % 2 == 0 && j % 2 == 0)
			{
				tmp.setFillColor(Color(0, 50, 0));
				win.draw(tmp);
			}
			else
			{
				tmp.setFillColor(Color(0, 75, 0));
				win.draw(tmp);
			}
		}
	}
	tmp.setFillColor(Color(color_one, color_two, color_tree));//звет фрукта
	tmp.setPosition(fruct.x * TILE_SIZE, fruct.y * TILE_SIZE);
	win.draw(tmp);
}

//прорисовка змеи
void Draw_Snake()
{
	RectangleShape tmp(Vector2f(TILE_SIZE, TILE_SIZE));

	//параметры контура змеи
	tmp.setOutlineThickness(2);//толщина
	tmp.setOutlineColor(Color::Black/*(100, 250, 0)*/);//цвет

	//прорисовка змеи
	int i = 0;
	for (auto snake : snakes)
	{
		tmp.setFillColor(Color(Colors_vect[i].x, Colors_vect[i].y, Colors_vect[i].z));
		tmp.setPosition(snake.x * TILE_SIZE, snake.y * TILE_SIZE);
		win.draw(tmp);
		i++;
	}

}


int main()
{
	win.setVerticalSyncEnabled(true);
	srand(time(NULL));
	Start();
	Clock clock;
	Time time;
	while (win.isOpen())
	{
		Event event;
		while (win.pollEvent(event))
		{
			if (event.type == Event::Closed)
				win.close();
		}
		UpdateKeyboard();
		time = clock.getElapsedTime();
		if (time.asMilliseconds() > DELAY)
		{
			clock.restart();
			Update();
		}
		win.clear();
		Draw();
		Draw_Snake();
		win.display();
	}
	return 0;
}
