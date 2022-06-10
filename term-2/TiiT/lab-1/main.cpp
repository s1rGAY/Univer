
#include "Header.h"

int main()
{
    ifstream read;
    read.open("input.txt");

    ofstream record;
    record.open("output.txt", ios::app);

    string f, inp;

    getline(read, f, ' ');
    int g = stoi(f);

    Tree MyTree;

    vector<int>MyVector;
    MyVector.resize(g);

    for (int i = 0; i < MyVector.size(); i++)
    {
        getline(read, inp, ' ');
        MyVector[i] = stoi(inp);
    }
    

    MyTree.SetSize(MyVector);



    MyTree.build_sum_tree(0, 0, MyTree.GetSize());

    cout << "Everything is OK";



    bool b = false;
    do
    {
        cout << "CHANGE - 1;" << endl <<
            "GET SAMMARY - 2;" << endl <<
            "YOUR ARRAY - 3" << endl <<
            "EXIT - 4" << endl <<
            "Your choice : ";
        string type;
        getline(read, type, ' ');

        if (type == "1")
        {
            cout << "Enter segment boundaries (L,R)";
            int l, r, x;
            getline(read, inp, ' ');
            l = stoi(inp);
            getline(read, inp, ' ');
            r = stoi(inp);
            getline(read, inp, ' ');
            x = stoi(inp);

            --l;
            MyTree.UpdateValue(l, r, x);
        }
        else if (type == "2")
        {
            cout << "Enter segment boundaries (L,R)";
            int l, r;
            getline(read, inp, ' ');
            l = stoi(inp);
            getline(read, inp, ' ');
            r = stoi(inp);

            --l;
            int h = MyTree.get_summary(0, 0, MyTree.GetSize(), l, r);
            record << "SUMMARY:" << h << '\n';
        }
        else if (type == "3")
        {
            record << "ARRAY:";
            for (int i = 0; i < g; i++)
            {
                int j = MyTree.View(i);
                record << j << " ";
            }
            record << '\n';
        }
        else if (type == "4") {
            record.close();
            read.close();
            b = true;
        }
    } while (!b);
    return 0;
}
