#include "pch.h"
#include "/Users/patge/source/repos/Project1/Project1/Dictionary.h"

TEST(SizeTests, one_get)
{
	Dictionary temp_dict;
	ASSERT_EQ(0, temp_dict.get_size());
}
TEST(SizeTests, a_lot_get)
{
	Dictionary temp_dict;
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	temp_dict += p1;
	ASSERT_EQ(1, temp_dict.get_size());
	pair < string, string > p2 = make_pair("SECOND INPUT", "SECOND OUTPUT");
	temp_dict += p2;
	ASSERT_EQ(2, temp_dict.get_size());
}
TEST(SizeTests,third_test)
{
	Dictionary temp_dict;
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	temp_dict += p1;
	ASSERT_EQ(1, temp_dict.get_size());
	temp_dict -= p1.first;
	ASSERT_EQ(0, temp_dict.get_size());
	pair < string, string > p2 = make_pair("SECOND INPUT", "SECOND OUTPUT");
	temp_dict += p2;
	ASSERT_EQ(1, temp_dict.get_size());
}

TEST(FileTests, input_test)
{
	Dictionary test_dict;
	test_dict.database_input("C:\\Users\\patge\\source\\repos\\Project1\\Project1\\E");
	ASSERT_EQ((4392/2), test_dict.get_size());
}
TEST(FileTests, exept_test)
{
	Dictionary test_dict;
	ASSERT_ANY_THROW(test_dict.database_input("TEST_FILE"));//данного файла не существует
}

TEST(Operators, word_add)
{
	Dictionary test_dict;
	ASSERT_EQ(0, test_dict.get_size());
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	pair < string, string > p2 = make_pair("SECOND INPUT", "SECOND OUTPUT");
	pair < string, string > p3 = make_pair("THIRD INPUT", "THIRD OUTPUT");
	pair < string, string > p4 = make_pair("FOUTH INPUT", "FOUTH OUTPUT");
	pair < string, string > p5 = make_pair("FIFTH INPUT", "FIFTH OUTPUT");

	test_dict += p1;
	ASSERT_EQ(1, test_dict.get_size());
	test_dict += p2;
	ASSERT_EQ(2, test_dict.get_size());
	test_dict += p3;
	ASSERT_EQ(3, test_dict.get_size());
	test_dict += p4;
	ASSERT_EQ(4, test_dict.get_size());
	test_dict += p5;
	ASSERT_EQ(5, test_dict.get_size());
}
TEST(Operators, word_add_without_exeption)
{
	Dictionary test_dict;
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	test_dict += p1;
	ASSERT_NO_THROW(test_dict += p1);
}
TEST(Operators, word_add_char)
{
	char* a = "FIRST INPUT";
	char* b = "FIRST OUTPUT";
	char* c = "SECOND OUTPUT";
	char* d = "SECOND OUTPUT";


	Dictionary test_dict;
	ASSERT_EQ(0, test_dict.get_size());
	pair < char*, char* > p1 = make_pair(a, b);
	pair < char*, char* > p2 = make_pair(c, d);
	test_dict += p1;
	ASSERT_EQ(1, test_dict.get_size());
	test_dict += p2;
	ASSERT_EQ(2, test_dict.get_size());
	ASSERT_EQ("FIRST OUTPUT", test_dict[p1.first]);
	ASSERT_EQ("SECOND OUTPUT", test_dict[p2.first]);
}
TEST(Operators, word_add_char_without_exep)
{
	char* a = "FIRST INPUT";
	char* b = "FIRST OUTPUT";
	char* c = "SECOND OUTPUT";
	char* d = "SECOND OUTPUT";


	Dictionary test_dict;
	ASSERT_EQ(0, test_dict.get_size());
	pair < char*, char* > p1 = make_pair(a, b);
	pair < char*, char* > p2 = make_pair(c, d);
	ASSERT_NO_THROW(test_dict += p1);
	ASSERT_NO_THROW(test_dict += p2);
}


TEST(Operators, word_del)
{
	Dictionary test_dict;
	ASSERT_EQ(0, test_dict.get_size());
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	pair < string, string > p2 = make_pair("SECOND INPUT", "SECOND OUTPUT");
	pair < string, string > p3 = make_pair("THIRD INPUT", "THIRD OUTPUT");
	pair < string, string > p4 = make_pair("FOUTH INPUT", "FOUTH OUTPUT");
	pair < string, string > p5 = make_pair("FIFTH INPUT", "FIFTH OUTPUT");

	test_dict += p1;
	test_dict += p2;
	test_dict += p3;
	test_dict += p4;
	test_dict += p5;

	ASSERT_EQ(5, test_dict.get_size());
	test_dict -= p5.first;
	ASSERT_EQ(4, test_dict.get_size());
	test_dict -= p4.first;
	ASSERT_EQ(3, test_dict.get_size());
	test_dict -= p3.first;
	ASSERT_EQ(2, test_dict.get_size());
	test_dict -= p2.first;
	ASSERT_EQ(1, test_dict.get_size());
	test_dict-= p1.first;
	ASSERT_EQ(0, test_dict.get_size());
}
TEST(Operators, word_del_exeption)
{
	Dictionary test_dict;
	ASSERT_EQ(0, test_dict.get_size());
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	pair < string, string > p2 = make_pair("SECOND INPUT", "SECOND OUTPUT");
	test_dict += p1;
	ASSERT_ANY_THROW(test_dict[p2.first]);
}

TEST(Operators, empty_equal)
{
	Dictionary first_test_dict,sec_test_dict;
	ASSERT_EQ(true, first_test_dict == sec_test_dict);
}
TEST(Operators, no_empty_equal)
{
	Dictionary first_test_dict, sec_test_dict;

	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	pair < string, string > p2 = make_pair("SECOND INPUT", "SECOND OUTPUT");
	pair < string, string > p3 = make_pair("THIRD INPUT", "THIRD OUTPUT");
	pair < string, string > p4 = make_pair("FOUTH INPUT", "FOUTH OUTPUT");

	first_test_dict += p1;
	sec_test_dict += p2;
	ASSERT_EQ(true, first_test_dict == sec_test_dict);
	first_test_dict += p3;
	sec_test_dict += p4;
	ASSERT_EQ(true, first_test_dict == sec_test_dict);
	sec_test_dict -= p4.first;
	ASSERT_EQ(false, first_test_dict == sec_test_dict);
}
TEST(Operators, empty_no_equal)
{
	Dictionary first_test_dict, sec_test_dict;
	ASSERT_EQ(false, first_test_dict != sec_test_dict);
}
TEST(Operators, no_empty_no_equal)
{
	Dictionary first_test_dict, sec_test_dict;
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	pair < string, string > p2 = make_pair("SECOND INPUT", "SECOND OUTPUT");

	first_test_dict += p1;
	sec_test_dict += p2;
	ASSERT_EQ(false, first_test_dict != sec_test_dict);

	first_test_dict -= p1.first;
	ASSERT_EQ(true, first_test_dict != sec_test_dict);
}

TEST(Operators, find_opeartor_one)
{
	Dictionary test_dict;
	ASSERT_EQ(0, test_dict.get_size());
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	test_dict += p1;
	ASSERT_EQ(p1.second, test_dict[p1.first]);
}
TEST(Operators, find_operator_a_lot)
{
	Dictionary test_dict;
	ASSERT_EQ(0, test_dict.get_size());
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	pair < string, string > p2 = make_pair("SECOND INPUT", "SECOND OUTPUT");
	pair < string, string > p3 = make_pair("THIRD INPUT", "THIRD OUTPUT");
	pair < string, string > p4 = make_pair("FOUTH INPUT", "FOUTH OUTPUT");
	pair < string, string > p5 = make_pair("FIFTH INPUT", "FIFTH OUTPUT");
	test_dict += p1;
	test_dict += p2;
	test_dict += p3;
	test_dict += p4;
	test_dict += p5;
	ASSERT_EQ(p1.second, test_dict[p1.first]);
	ASSERT_EQ(p2.second, test_dict[p2.first]);
	ASSERT_EQ(p3.second, test_dict[p3.first]);
	ASSERT_EQ(p4.second, test_dict[p4.first]);
	ASSERT_EQ(p5.second, test_dict[p5.first]);
}
TEST(Operators, find_operator_exeption)
{
	Dictionary test_dict;
	ASSERT_EQ(0, test_dict.get_size());
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	pair < string, string > p2 = make_pair("SECOND INPUT", "SECOND OUTPUT");
	pair < string, string > p3 = make_pair("THIRD INPUT", "THIRD OUTPUT");
	pair < string, string > p4 = make_pair("FOUTH INPUT", "FOUTH OUTPUT");
	pair < string, string > p5 = make_pair("FIFTH INPUT", "FIFTH OUTPUT");
	ASSERT_ANY_THROW(test_dict[p1.first]);
	ASSERT_ANY_THROW(test_dict[p2.first]);
	ASSERT_ANY_THROW(test_dict[p3.first]);
	ASSERT_ANY_THROW(test_dict[p4.first]);
	ASSERT_ANY_THROW(test_dict[p5.first]);
}

TEST(Assignment_operator, with_empty_dict)
{
	Dictionary first_test_dict, second_test_dict;
	ASSERT_NO_THROW(first_test_dict=second_test_dict);
}
TEST(Assignment_operator, common_assigment)
{
	Dictionary first_test_dict, second_test_dict;
	first_test_dict.database_input("C:\\Users\\patge\\source\\repos\\Project1\\Project1\\E");
	second_test_dict = first_test_dict;
	ASSERT_EQ(true, first_test_dict.get_size()==second_test_dict.get_size());
}
TEST(Assignment_operator, value_check)
{
	Dictionary first_test_dict, second_test_dict;
	first_test_dict.database_input("C:\\Users\\patge\\source\\repos\\Project1\\Project1\\E");
	ASSERT_EQ((4392 / 2), first_test_dict.get_size());
	second_test_dict = first_test_dict;
	ASSERT_EQ(true, first_test_dict["a trifle"] == second_test_dict["a trifle"]);
}

TEST(Operators, translation_update)
{
	Dictionary test_dict;
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	test_dict += p1;
	p1.second = "NEW MEANING";
	test_dict[p1];
	ASSERT_EQ(p1.second, test_dict[p1.first]);
}
TEST(Operators, translation_update_exeption)
{
	Dictionary test_dict;
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	test_dict += p1;
	const auto p2 = p1;
	ASSERT_ANY_THROW(test_dict[p2]);
}

TEST(Distructor, common_test)
{
	Dictionary test_dict;
	pair < string, string > p1 = make_pair("FIRST INPUT", "FIRST OUTPUT");
	pair < string, string > p2 = make_pair("SECOND INPUT", "SECOND OUTPUT");
	pair < string, string > p3 = make_pair("THIRD INPUT", "THIRD OUTPUT");
	pair < string, string > p4 = make_pair("FOUTH INPUT", "FOUTH OUTPUT");
	pair < string, string > p5 = make_pair("FIFTH INPUT", "FIFTH OUTPUT");
	test_dict += p1;
	test_dict += p2;
	test_dict += p3;
	test_dict += p4;
	test_dict += p5;
	ASSERT_EQ(5, test_dict.get_size());
	test_dict.~Dictionary();
	ASSERT_EQ(0, test_dict.get_size());
}
TEST(Distructor, for_empty_tree)
{
	Dictionary test_dict;
	ASSERT_EQ(0, test_dict.get_size());
	ASSERT_NO_THROW(test_dict.~Dictionary());
	ASSERT_EQ(0, test_dict.get_size());
}

TEST(Constructor, Default_constructor)
{
	Dictionary test_dict;
	ASSERT_EQ(0, test_dict.get_size());
}
TEST(Constructor, two_string)
{
	Dictionary test_dict("Fist_word", "Second_word");
	ASSERT_EQ(1, test_dict.get_size());
	ASSERT_EQ("Second_word", test_dict["Fist_word"]);
}
TEST(Constructor, pair)
{
	pair<string, string>p1 = make_pair("Fist_word", "Second_word");
	Dictionary test_dict(p1);
	ASSERT_EQ(1, test_dict.get_size());
	ASSERT_EQ("Second_word", test_dict["Fist_word"]);
}

TEST(Copy_Consructor, check_size)
{
	Dictionary first_test_dict;
	pair<string, string>p1 = make_pair("Fist_word", "Second_word");
	first_test_dict+=p1;
	Dictionary(second_test_dict)=first_test_dict;

	ASSERT_EQ(true, first_test_dict.get_size()== second_test_dict.get_size());
}
TEST(Copy_Consructor, check_with_big_file)
{
	Dictionary first_test_dict;
	first_test_dict.database_input("C:\\Users\\patge\\source\\repos\\Project1\\Project1\\E");
	ASSERT_EQ((4392 / 2), first_test_dict.get_size());

	Dictionary(second_test_dict) = first_test_dict;

	ASSERT_EQ(true, first_test_dict.get_size() == second_test_dict.get_size());
}
TEST(Copy_Consructor, correct_value)
{
	Dictionary first_test_dict;
	first_test_dict.database_input("C:\\Users\\patge\\source\\repos\\Project1\\Project1\\E");
	ASSERT_EQ((4392 / 2), first_test_dict.get_size());

	Dictionary(second_test_dict) = first_test_dict;

	ASSERT_EQ(true, first_test_dict["a trifle"] == second_test_dict["a trifle"]);
}



int main(int argc, char* argv[])
{
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}