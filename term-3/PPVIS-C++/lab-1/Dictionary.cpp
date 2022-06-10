#include "Dictionary.h"

using namespace std;

struct Dictionary::node
{
    map<string, string> data;
    node* left;
    node* right;
};

Dictionary::node* Dictionary::make_empty(node* t)
{
    if (t == NULL)
        return NULL;
    {
        make_empty(t->left);
        make_empty(t->right);
        delete t;
    }
    return NULL;
}

Dictionary::node* Dictionary::insert(const string& eng, const string& rus, node* t)
{
    if (t == NULL)
    {
        t = new node;
        t->data[eng] = rus;
        t->left = t->right = NULL;
        return t;
    }
    else if (eng < t->data.begin()->first)
        t->left = insert(eng, rus, t->left);
    else if (eng > t->data.begin()->first)
        t->right = insert(eng, rus, t->right);
    return t;
}

Dictionary::node* Dictionary::find_min(node* t)
{
    if (t == NULL)
        return NULL;
    else if (t->left == NULL)
        return t;
    else
        return find_min(t->left);
}

Dictionary::node* Dictionary::find_max(node* t)
{
    if (t == NULL)
        return NULL;
    else if (t->right == NULL)
        return t;
    else
        return find_max(t->right);
}

Dictionary::node* Dictionary::remove(string del_word, node* t)
{
    node* temp;
    if (t == NULL)
        return NULL;
    else if (del_word < t->data.begin()->first)
        t->left = remove(del_word, t->left);
    else if (del_word > t->data.begin()->first)
        t->right = remove(del_word, t->right);
    else if (t->left && t->right)
    {
        temp = find_min(t->right);
        t->data = temp->data;
        t->right = remove(t->data.begin()->first, t->right);
    }
    else
    {
        temp = t;
        if (t->left == NULL)
            t = t->right;
        else if (t->right == NULL)
            t = t->left;
        delete temp;
    }

    return t;
}

void Dictionary::size_calculation(node* t, uint16_t& temp_count)
{
    if (t == NULL)
    {
        return;
    }
    size_calculation(t->left, temp_count);
    temp_count++;
    /*cout << t->data.begin()->first << " "
    << t->data.begin()->second << endl;*/
    size_calculation(t->right, temp_count);
}

Dictionary::node* Dictionary::find(node* t, string search_word)
{
    if (t == NULL)
        return NULL;
    else if (search_word < t->data.begin()->first)
        return find(t->left, search_word);
    else if (search_word > t->data.begin()->first)
        return find(t->right, search_word);
    else
        return t;
}

void Dictionary::filling_from_database(string database_name)
{
    database_name += ".txt";
    ifstream in(database_name);

    if (in.is_open())
    {
        string first_temp_str, sec_temp_str;
        while (!in.eof())
        {
            getline(in, first_temp_str);
            getline(in, sec_temp_str);
            root = insert(first_temp_str, sec_temp_str, root);
        }
    }
    else
    {
        throw("Error : unable to open file");
    }

    in.close();
}

Dictionary::node* Dictionary::copy(const node* other)
{
    /*node* newTree = nullptr;
    if (other == nullptr)
        return newTree;
    else
    {
        newTree = new node;
        newTree->data = other->data;
        newTree->left = copy(other->left);
        newTree->right = copy(other->right);
    }*/
    if (other == NULL)
        return NULL;

    node* newnode = new node;
    newnode->data = other->data;
    newnode->left = copy(other->left);
    newnode->right = copy(other->right);

    return newnode;

}

Dictionary::Dictionary()
{
    root = NULL;
}

Dictionary::Dictionary(string eng, string rus)
{
    root = new node;
    root->data[eng] = rus;
    root->left = root->right = NULL;
}

Dictionary::Dictionary(pair<string, string> eng_rus)
{
    root = new node;
    root->data[eng_rus.first] = eng_rus.second;
    root->left = root->right = NULL;
}

Dictionary::~Dictionary()
{
    root = make_empty(root);
}

Dictionary::Dictionary(Dictionary& other)
{
    this->root = copy(other.root);
}

void Dictionary::database_input(string base_name)
{
    filling_from_database(base_name);
}

int Dictionary::get_size()
{
    uint16_t temp_count = 0;
    size_calculation(root, temp_count);
    return(temp_count);
}

void Dictionary::operator+=(pair<string, string> eng_rus)
{
    root = insert(eng_rus.first, eng_rus.second, root);
}

void Dictionary::operator-=(const string eng_del_word)
{
    node* temp_node;
    temp_node = find(root, eng_del_word);
    if (temp_node->data.begin()->first == eng_del_word)
        root = remove(eng_del_word, root);
    else
        throw("I CANT FIND THIS WORD!");
}

void Dictionary::operator[](const pair<string, string> eng_new_rus)
{
    node* temp_node;
    temp_node = find(root, eng_new_rus.first);
    if (temp_node->data.begin()->second != eng_new_rus.second)
        temp_node->data.begin()->second = eng_new_rus.second;
    else
        throw("Words are the same!");
    
}

string Dictionary::operator[](const string search_eng_word)
{
    node* temp_node;
    temp_node = find(root, search_eng_word);
    if (temp_node != NULL)
    {
        return (temp_node->data.begin()->second);
    }
    else
    {
        throw("Sorry, i can't find this word! :(");
    }
}

istream& operator>>(std::istream &in, Dictionary& your_dict)
{
    string eng_word,rus_word;
    in >> eng_word;
    in >> rus_word;
    pair<string, string> temp_pair (eng_word, rus_word);
    your_dict+=temp_pair;
    return in;
}

ostream& operator<<(std::ostream& out, const Dictionary& your_dict)
{
    out << "Root of your dict - "
        << your_dict.root->data.begin()->first << " : "
        << your_dict.root->data.begin()->second << ", in memory cell:"
        << your_dict.root << endl;
    return out;
}

void Dictionary::operator =(const Dictionary& other)
{
    this->root = copy(other.root);
}

bool operator==(Dictionary& first_dict, Dictionary& second_dict)
{
    return(first_dict.get_size() == second_dict.get_size());
}

bool operator!=(Dictionary& first_dict, Dictionary& second_dict)
{
    return !(first_dict == second_dict);
}