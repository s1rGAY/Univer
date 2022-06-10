#pragma once

#include <iostream>
#include <math.h>
#include <string>
#include <map>
#include <vector>
#include <cstdlib>
#include "windows.h"
#include <fstream>

using namespace std;

class Tree {
private:
    int n, f;
    vector<int>size;
    vector<int>tree;
public:

    void SetSize(vector<int>& MyVector) {
        size.resize(MyVector.size());
        for (int i = 0; i < MyVector.size(); i++) 
        {
            size[i] = MyVector[i];
        }
        tree.resize(4*MyVector.size());
        return;
    }

    int GetSize() {
        return size.size();
    }


    int View(int i) {
        return size[i];
    }


    void build_sum_tree(int v, int L, int R)
    {
        if (L == R - 1)
        {
            if (L < size.size())
            {
                tree[v] = size[L];
            }
            return;
        }
        int M = (L + R) / 2;
        build_sum_tree(2 * v + 1, L, M);
        build_sum_tree(2 * v + 2, M, R);
        tree[v] = tree[2 * v + 1] + tree[2 * v + 2];
    }


    int64_t get_summary(int v, int L, int R, int l, int r)
    {
        if (r <= L || R <= l) return 0;
        if (l <= L && R <= r) return tree[v];
        int M = (L + R) / 2;
        int64_t first_child = get_summary(2 * v + 1, L, M, l, r);
        int64_t second_child = get_summary(2 * v + 2, M, R, l, r);
        return first_child + second_child;
    }

    void UpdateValue(int L, int R, int x) {
        for (int i = L; i < R; i++)
        {
            size[i] = x;
        };
        build_sum_tree(0, 0, size.size());
    }
};
