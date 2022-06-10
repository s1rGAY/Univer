#include <iostream>
#include <vector>
#include<fstream>
#include<queue>
#include<string>
using namespace std;

#include "cpp/sc_addr.hpp"
#include "cpp/sc_memory.hpp"
#include "cpp/sc_iterator.hpp"


const std::unique_ptr<ScMemoryContext> context(new ScMemoryContext(sc_access_lvl_make_max,"name"));
ScAddr graph, rrel_arcs, rrel_nodes, father;


void print_element(const std::unique_ptr<ScMemoryContext>& context, ScAddr element)
{
    ScType type;
    type = context->GetElementType(element);

    if (type.IsNode() == ScType::Node)
    {
        std::string data;
        data = context->HelperGetSystemIdtf(element);
        std::cout << data;
    }
    else
    {
        ScAddr elem1, elem2;
        elem1 = context->GetEdgeSource(element);
        elem2 = context->GetEdgeTarget(element);
        std::cout << "(";
        print_element(context, elem1);
        std::cout << " -> ";
        print_element(context, elem2);
        std::cout << ")";
    }
}
bool find_vertex_in_set (const std::unique_ptr<ScMemoryContext>& context,ScAddr element, ScAddr set)
{
    bool find = false;
    ScIterator3Ptr location = context->Iterator3(set,ScType::EdgeAccessConstPosPerm,ScType(0));

    while (location->Next())
    {
        ScAddr loc = location->Get(2);

        if (loc != element)
        {
            find = false;
            continue;
        }
        else
        {
            find = true;
            break;
        }
    }
    return find;
}
void get_edge_vertexes (const std::unique_ptr<ScMemoryContext>& context,ScAddr edge, ScAddr &v1, ScAddr &v2)
{
    v1 = context->GetEdgeSource(edge);
    v2 = context->GetEdgeTarget(edge);
}
void print_graph (const std::unique_ptr<ScMemoryContext>& context)
{

    ScAddr arcs, nodes, v1, v2, printed_vertex;
    bool find;
    printed_vertex = context->CreateNode(ScType::Const);

    print_element(context, graph);
    std::cout << std::endl << "----------------------" << std::endl;

    ScIterator5Ptr it = context->Iterator5(graph,ScType::EdgeAccessConstPosPerm,ScType(0),ScType::EdgeAccessConstPosPerm,rrel_arcs);

    if (it->Next())
    {
        arcs = it->Get(2);

        ScIterator3Ptr arcs_it = context->Iterator3(arcs,ScType::EdgeAccessConstPosPerm,ScType(0));

        while (arcs_it->Next())
        {

            ScAddr t_arc = arcs_it->Get(2);

            get_edge_vertexes (context,t_arc, v1, v2);

            print_element(context, v1);
            std::cout << " -- ";
            print_element(context, v2);
            std::cout << std::endl;

            if (!find_vertex_in_set(context,v1, printed_vertex))
            {
                context->CreateEdge(ScType::EdgeAccessConstPosPerm,printed_vertex, v1);
            }
            if (!find_vertex_in_set(context,v2, printed_vertex))
            {
                context->CreateEdge(ScType::EdgeAccessConstPosPerm,printed_vertex, v2);
            }
        }
    }

    it = context->Iterator5(graph,ScType::EdgeAccessConstPosPerm,ScType(0),ScType::EdgeAccessConstPosPerm,rrel_nodes);

    if (it->Next())
    {
        nodes = it->Get(2);

        ScIterator3Ptr nodes_it = context->Iterator3(nodes,ScType::EdgeAccessConstPosPerm,ScType(0));


        while (nodes_it->Next())
        {

            ScAddr t_node = nodes_it->Get(2);

            find = find_vertex_in_set(context,t_node, printed_vertex);

            if (!find)
            {
                print_element(context, t_node);
                std::cout << std::endl;
            }
        }
    }
}


void test_run(const std::unique_ptr<ScMemoryContext>& context, std::string number_test)
{
    father = context->CreateNode(ScType::Const);

    std::string gr = "graph";
    gr.append(number_test);
    graph = context->HelperResolveSystemIdtf(gr);
    rrel_arcs = context->HelperResolveSystemIdtf("rrel_arcs");
    rrel_nodes = context->HelperResolveSystemIdtf("rrel_nodes");
    print_graph(context);

    // is cactus check
}


int my_func() {
    ifstream in("1.txt");
    int n;
    in >> n;
    vector<vector<int> > g(n);
    for (int i = 0; i < n; i++) {
        int m;
        in >> m;
        vector<int> t(m);
        for (int j = 0; j < m; j++) {
            in >> t[j];
        }
        g[i] = t;
    }

    vector<int> ext(n);
    for (int i = 0; i < n; i++) {
        queue <int> q;
        vector<int> t(n, 0);
        vector<int> visit(n, 0);
        q.push(i);
        t[i] = 0;
        int time = 0;
        visit[i] = true;
        while (!q.empty()) {
            int v = q.front();
            for (int j = 0; j < g[v].size(); j++) {
                int u = g[v][j];
                if (visit[u] == 0) {
                    visit[u] = 1;
                    q.push(u);
                    t[u] = t[v] + 1;
                    time = max(time, t[u]);
                }
            }
            q.pop();
        }
        ext[i] = time;
    }

    int maks = 0;
    for (int i = 0; i < ext.size(); i++)
        if (ext[i] > maks)maks = ext[i];
    vector<int> per;
    for (int i = 0; i < ext.size(); i++) {
        if (ext[i] == maks)per.push_back(i);
    }
    vector<int> way_length;

    for (int i = 0; i < per.size() - 1; i++) {
        queue <int> q;
        vector<int> t(n, 0);
        vector<int> visit(n, 0);
        q.push(per[i]);
        t[per[i]] = 0;
        int time = 0;
        visit[per[i]] = true;
        while (!q.empty()) {
            int v = q.front();
            for (int j = 0; j < g[v].size(); j++) {
                int u = g[v][j];
                if (visit[u] == 0) {
                    visit[u] = 1;
                    q.push(u);
                    t[u] = t[v] + 1;
                    time = max(time, t[u]);
                }
            }
            q.pop();
        }
        for (int j = i + 1; j < per.size(); j++) {
            way_length.push_back(t[per[j]]);
        }
    }
    int min = 65535;
    double average = 0;
    for (int i = 0; i < way_length.size(); i++)
    {
        if (way_length[i] < min)min = way_length[i];
        average += way_length[i];
    }
    average /= way_length.size();
    cout << "Min = " << min << '\n';
    cout << "Average = " << average << '\n';
    return 0;
}
void first_try() {
    //считываю из файла данные, как это происходит в ostis???
    ifstream in("1.txt");
/*
6
1 3
1 3
1 3
4 0 1 2 4
2 3 5
1 4
*/

    int n;//количество вершин в графе
    in >> n;
    vector<vector<int> > g(n); //задает список смежности, где
    // № строки - название вершины
    // потом идет количество инцидентных вершин
    // потом сами вершины
    //заполнение вектора данными из файла с графом, по идее в ostis это не надо
    for (int i = 0; i < n; i++) {

        int m; //колличесво операций в данный строчке в txt : (4) 0 1 2 4
        in >> m;

        vector<int> t(m);
        for (int j = 0; j < m; j++) {
            in >> t[j]; //заполение временного веткора данными 4 (0 1 2 4)
        }
        g[i] = t;
    }
    //цикл для заполнения списка смежности

    vector<int> ext(n); //все эксцентриситеты


    for (int i = 0; i < n; i++) {
        queue <int> q;
        vector<int> t(n, 0);
        vector<int> visit(n, 0);//множество посещённых вершин

        q.push(i);

        t[i] = 0; //зануляем значение для вершины i
        int time = 0;
        visit[i] = true; //отмечаем, что прошли вершину i

        while (!q.empty()) {
            int v = q.front(); //берётся первый или самый старый элемент очереди

            for (int j = 0; j < g[v].size(); j++) { //итерируемся по вершине V
                int u = g[v][j]; //берём вершину берём из вершины V смежную ей вершину J

                if (visit[u] == 0) { //если она не отмечена ,как посещённая, выполняем расчеты
                    visit[u] = 1; //отмечаем её посещенной, тк её посещаем в данной итерации

                    q.push(u);//???????? зачем добавляем вершину в очередь ?
                    t[u] = t[v] + 1;//???????????

                    time = max(time, t[u]);
                    //если путь рассматриваемый в данной итерации больше,чем уже имеющееся значаение=>
                    //=> теперь он является эксцентриситетом
                }
            }
            q.pop(); //удаляем первую вершину из очереди тк для неё произвели расчеты
        }
        ext[i] = time; //добавление эксцентриситета для вершины i
    }


    //высчитываем максимальный эксцентриситет ( записать через max() )
    int maks = 0;
    for (int i = 0; i < ext.size(); i++)
        if (ext[i] > maks)maks = ext[i];


    vector<int> per;//вектор для периферийных вершин
    for (int i = 0; i < ext.size(); i++) {
        if (ext[i] == maks)per.push_back(i);
    }
    //заполнение периферийных вершин в вектор ?!

    /*
        Считаем эксцентриситеты
        Выбираем максимальные, кидаем номера этих вершин в per
        И снова обходом в ширину находим расстояния между периферийными
        Закидываем эти расстояния в массив way_length
     */
    vector<int> way_length;
    for (int i = 0; i < per.size() - 1; i++) {
        queue <int> q;
        vector<int> t(n, 0);
        vector<int> visit(n, 0);
        q.push(per[i]);
        t[per[i]] = 0;
        int time = 0;
        visit[per[i]] = true;
        while (!q.empty()) {
            int v = q.front();
            for (int j = 0; j < g[v].size(); j++) {
                int u = g[v][j];
                if (visit[u] == 0) {
                    visit[u] = 1;
                    q.push(u);
                    t[u] = t[v] + 1;
                    time = max(time, t[u]);
                }
            }
            q.pop();
        }
        for (int j = i + 1; j < per.size(); j++) {
            way_length.push_back(t[per[j]]);
        }
    }

    //расчет среднего и минимального (ничего интересного)
    {
        int min = 65535;
        double average = 0;
        for (int i = 0; i < way_length.size(); i++) {
            if (way_length[i] < min)min = way_length[i];
            average += way_length[i];
        }
        average /= way_length.size();
        cout << "Min = " << min << '\n';
        cout << "Average = " << average << '\n';
    }


    return;
}

bool find_addr_in_vector(ScAddr elem, vector<ScAddr> your_vect){
    for(int i = 0; i<your_vect.size(); i++){
        if(your_vect[i]==elem){return true;}
    }
    return false;
}

int get_number_of_vertices(string graph_name){
    ScAddr temp_graph = context->HelperResolveSystemIdtf(graph_name); //получение данных о нужном графе
    ScIterator3Ptr nodes_it = context->Iterator3(temp_graph, ScType::EdgeAccessConstPosPerm, ScType(sc_type_node));
    int n=0;
    while(nodes_it->Next()){n++;}
    return n;
}

void first_try_scp(string graph_name) {
    /*
        ScAddr graph = context->HelperResolveSystemIdtf("graph_name");
        ScIterator3Ptr nodes_it = context->Iterator3()
        nodes_it->Next();
        ScAddr a = nodes_it->Get("НОМЕР ЭЛЕМЕНТА, КОТОРЫЙ Я ХОЧУ ПРЛУЧИТЬ В ДАННОМ МАССИВЕ ИТЕРАТОРОВ")


    string graph_name = "test_graph1";
    ScAddr graph = context->HelperResolveSystemIdtf(graph_name); //получение данных о нужном графе

    //получаем инфу о вершинах графа (nodes_it содержит типа ?контейнер? со всеми вершинами)
    ScIterator3Ptr nodes_it = context->Iterator3(graph, ScType::EdgeAccessConstPosPerm, ScType(0));
    //int size = 0;//количество вершин в графе

    vector<vector<ScAddr>> g;//№ в первом векторе - номер вершины, внутри второго вектора - адреса смежных вершин
    vector<ScAddr> names;//вектор с адресами вершин для списка смежности

    int counter = 0;
    while (nodes_it->Next()) {
        names.push_back(nodes_it->Get(0)); //либо 0 либо 2 + чекнуть через show_all_vertex
        //получаем все 5-ти элементные конструкции для одной из вершин и заносим их в it
        ScIterator5Ptr it = context->Iterator5(nodes_it->Get(0), ScType::EdgeAccessConstPosPerm, ScType(0),
                                               ScType::EdgeAccessConstPosPerm, rrel_nodes);
        //проходим по it записывая все смежные вершины в список смежности
        while (it->Next()) {
            g[counter].push_back(it->Get(2));
        }
        counter++;
    }
    return;
}
     */

    ScAddr graph = context->HelperResolveSystemIdtf(graph_name);
    ScIterator3Ptr nodes_it = context->Iterator3(graph, ScType::EdgeAccessConstPosPerm, ScType(sc_type_node));
    cout<<"Количество вершин : "<<get_number_of_vertices(graph_name)<<endl<<endl;
    vector<pair<ScAddr,int>>ext;
    ScIterator3Ptr temp_it = context->Iterator3(graph, ScType::EdgeAccessConstPosPerm, ScType(sc_type_node));
    while (temp_it->Next()){
        ext.push_back(make_pair(temp_it->Get(2),0));
    }
    /*for(int j=0;j<ext.size();j++){
        cout<<"вершина: ";
        print_element(context,ext[j].first);
        cout<<"  эксцентриситет :"<<ext[j].second<<endl;
    }cout<<endl;*/
    while(nodes_it->Next()){
        queue <ScAddr> q;
        q.push(nodes_it->Get(2));//добавляем посещаемую на данный момент вершину в очередь

        vector<ScAddr> visit;//вектор посещённых вершин (изначально он пустой)

        vector<pair<ScAddr,int>> t;
        ScIterator3Ptr new_temp_it = context->Iterator3(graph, ScType::EdgeAccessConstPosPerm, ScType(sc_type_node));
        while (new_temp_it->Next()){t.push_back(make_pair(new_temp_it->Get(2),0));}
        /*for(int a=0;a<t.size();a++){
            if(t[a].first==nodes_it->Get(0)){t[a].second=0;}
        }*/
        /*for(int y=0;y<t.size();y++){
            cout<<"В t содержится вершина :";
            print_element(context,t[y].first);
            cout<<endl;
        }*/
        int time = 0;//эксцентриситет
        visit.push_back(nodes_it->Get(2));
        ScAddr my_vertex = nodes_it->Get(2);
        /*cout<<"Посещённая вершина : ";
        print_element(context,my_vertex);
        cout<<endl;*/
        /*for(int test=0;test<t.size();test++){
            cout<<"Для вершины ";
            print_element(context,t[test].first);
            cout<<"  эксцентриситет - "<<t[test].second;
            cout<<endl;
        }

        for(int h=0;h<t.size();h++){
            cout<<"Смежная вершина :";
            print_element(context,t[h].first);
            cout<<endl;
        }
        it = context->Iterator5(nodes_it->Get(2), ScType::EdgeDCommonConst, ScType(ScType::NodeConst),
           ScType::EdgeAccessConstPosPerm, rrel_nodes);

        for(int a=0;a<t.size();a++){
            if(t[i].first==(nodes_it->Get(0))){t[i].second=0;}
        }
       //зануляем значение для вершины nodes_it  это типа значение для i эксцентриситета(счётчик эксцентриситета)

       visit.push_back(nodes_it->Get(0)); //отмечаем, что прошли вершину i
        */
        while (!q.empty()) {
            ScAddr v = q.front(); //берётся первый или самый старый элемент очереди

            //получаем смежные вершины для v
            vector<ScAddr>adj_vertexes;
            ScIterator5Ptr it = context->Iterator5(v, ScType::Const, ScType(sc_type_node),
                    /*получаем итератор по всем смежным вершинам*/               ScType::Const, graph);
            while(it->Next()){
                adj_vertexes.push_back(it->Get(2));
                //adj_size++;
            }
            it = context->Iterator5(ScType(sc_type_node), ScType::Const, v,
                    /*получаем итератор по всем смежным вершинам*/               ScType::Const, graph);
            while(it->Next()){
                adj_vertexes.push_back(it->Get(0));
                //adj_size++;
            }

            for (int j = 0; j < adj_vertexes.size(); j++) { //итерируемся по вершине V (adj_size)
                ScAddr u = adj_vertexes[j]; //берём вершину берём из вершины V смежную ей вершину J
                /*cout<<"Проходим через смежную вершину :";
                print_element(context,u);
                cout<<endl;*/

                if (find_addr_in_vector(u,visit) == false) { //если она не отмечена ,как посещённая, выполняем расчеты
                    visit.push_back(u); //отмечаем её посещенной, тк её посещаем в данной итерации
                    q.push(u);

                    for(int c=0;c<t.size();c++){
                        if(t[c].first==u){
                            for(int d=0;d<t.size();d++){
                                if(t[d].first==v){
                                    t[c].second=(t[d].second+1);
                                }
                            }
                        }
                        time = max(time, t[c].second);
                    }
                }
            }
            q.pop(); //удаляем первую вершину из очереди тк для неё произвели расчеты
        }
        //cout<<"эксцентриситет для вершины : "<<time<<endl;
        for(int j=0;j<ext.size();j++){
            if(ext[j].first==nodes_it->Get(2)){ext[j].second=time;}
        }
        //ext[i] = time; //добавление эксцентриситета для вершины i
    }


    //высчитываем максимальный эксцентриситет ( записать через max() )
    int maks = 0;
    for (int i = 0; i < ext.size(); i++)
        if (ext[i].second > maks)maks = ext[i].second;

    vector<pair<ScAddr,int>> per;//вектор для периферийных вершин
    for (int i = 0; i < ext.size(); i++) {
        if (ext[i].second == maks)per.push_back(ext[i]);
    }

    vector<int> way_length;

    for (int i = 0; i < per.size() - 1; i++) {
        queue <ScAddr> q;
        q.push(per[i].first);
        vector<ScAddr> visit;
        visit.push_back(per[i].first);

        vector<pair<ScAddr,int>> t;
        ScIterator3Ptr new_temp_it = context->Iterator3(graph, ScType::EdgeAccessConstPosPerm, ScType(sc_type_node));
        while (new_temp_it->Next()){t.push_back(make_pair(new_temp_it->Get(2),0));}
        int time = 0;

        while (!q.empty()) {
            ScAddr v = q.front();

            vector<ScAddr>adj_vertexes;
            ScIterator5Ptr it = context->Iterator5(v, ScType::Const, ScType(sc_type_node),
                    /*получаем итератор по всем смежным вершинам*/               ScType::Const, graph);
            while(it->Next()){
                adj_vertexes.push_back(it->Get(2));
                //adj_size++;
            }
            it = context->Iterator5(ScType(sc_type_node), ScType::Const, v,
                    /*получаем итератор по всем смежным вершинам*/               ScType::Const, graph);
            while(it->Next()){
                adj_vertexes.push_back(it->Get(0));
                //adj_size++;
            }

            for (int j = 0; j < adj_vertexes.size(); j++) {
                ScAddr u = adj_vertexes[j];

                if (find_addr_in_vector(u,visit) == false) {
                    visit.push_back(u);
                    q.push(u);

                    for(int c=0;c<t.size();c++){
                        if(t[c].first==u){
                            for(int d=0;d<t.size();d++){
                                if(t[d].first==v){
                                    t[c].second=(t[d].second+1);
                                }
                            }
                        }
                        time = max(time, t[c].second);
                    }
                }
            }
            q.pop();
        }
        for (int j = i + 1; j < per.size(); j++) {
            for(int k=0;k<t.size();k++){
                if(t[k].first==per[j].first){
                    way_length.push_back(t[k].second);
                }
            }
        }
    }


    uint min = 4294967290;
    double average = 0;
    for (int i = 0; i < way_length.size(); i++) {
        if (way_length[i] < min)min = way_length[i];
        average += way_length[i];
    }
    average /= way_length.size();
    cout << "Min = " << min << '\n';
    cout << "Average = " << average << '\n';
    return;
}

int main(){
    sc_memory_params params;

    sc_memory_params_clear(&params);
    params.repo_path = "/home/siarhei/Programming/IIT/OSTIS/ostis-example-app/ostis-web-platform/kb.bin";
    params.config_file = "/home/siarhei/Programming/IIT/OSTIS/ostis-example-app/ostis-web-platform/config/sc-web.ini";
    params.ext_path = "/home/siarhei/Programming/IIT/OSTIS/ostis-example-app/ostis-web-platform/sc-machine/bin/extensions";
    params.clear = SC_FALSE;

    ScMemory mem;
    mem.Initialize(params);

    const std::unique_ptr<ScMemoryContext> context(new ScMemoryContext(sc_access_lvl_make_max,"name"));
    first_try_scp("test_graph1");
    first_try_scp("test_graph2");
    first_try_scp("test_graph3");
    first_try_scp("test_graph4");
    first_try_scp("test_graph5");
    //first_try_scp("test_graph2");
    //first_try_scp("test_graph3");


    //test_run(context, "1");
    //test_run(context, "2");
    //test_run(context, "3");
    //test_run(context, "4");
    //test_run(context, "5");
    mem.Shutdown(true);
    return 0;
}
