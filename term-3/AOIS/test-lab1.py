import unittest

from lab1 import convert, float_sum
from lab1 import sum_of_positive
from lab1 import input_data

from lab1 import to_straight_code
from lab1 import to_reverse_code
from lab1 import to_additional_code

from lab1 import straight_code_operation
from lab1 import reverse_code_operation
from lab1 import additional_code_operation

from lab1 import multiplication
from lab1 import division
from lab1 import to_float

class TestConvert(unittest.TestCase):
    def test_value(self):
        self.assertAlmostEqual(convert(0,2,10),'0')
        self.assertAlmostEqual(convert(1,2,10),'1')
        self.assertAlmostEqual(convert(10,2,10),'1010')
        self.assertAlmostEqual(convert(100,2,10),'1100100')
        self.assertAlmostEqual(convert(32767,2,10),'111111111111111')

class Test_sum_of_positive(unittest.TestCase):
    def test_value(self):
        self.assertAlmostEqual(sum_of_positive(0,0),['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'])
        self.assertAlmostEqual(sum_of_positive(0,1),['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'])
        self.assertAlmostEqual(sum_of_positive(1,0),sum_of_positive(0,1))
        self.assertAlmostEqual(sum_of_positive(1,1),['0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0'])
        self.assertAlmostEqual(sum_of_positive(5,5),['0','0','0','0','0','0','0','0','0','0','0','0','1','0','1','0'])
        self.assertAlmostEqual(sum_of_positive(1000,1000),['0','0','0','0','0','1','1','1','1','1','0','1','0','0','0','0'])

class Test_to_straight_code(unittest.TestCase):
    def test_value(self):
        self.assertAlmostEqual(to_straight_code(0),['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'])
        self.assertAlmostEqual(to_straight_code(1),['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'])
        self.assertAlmostEqual(to_straight_code(-1),['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'])
        self.assertAlmostEqual(to_straight_code(2),['0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0'])
        self.assertAlmostEqual(to_straight_code(-2),['1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0'])
        self.assertAlmostEqual(to_straight_code(3),['0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1'])
        self.assertAlmostEqual(to_straight_code(-3),['1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1'])
        self.assertAlmostEqual(to_straight_code(5),['0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','1'])
        self.assertAlmostEqual(to_straight_code(-5),['1','0','0','0','0','0','0','0','0','0','0','0','0','1','0','1'])
        self.assertAlmostEqual(to_straight_code(10),['0','0','0','0','0','0','0','0','0','0','0','0','1','0','1','0'])
        self.assertAlmostEqual(to_straight_code(-10),['1','0','0','0','0','0','0','0','0','0','0','0','1','0','1','0'])
        self.assertAlmostEqual(to_straight_code(100),['0','0','0','0','0','0','0','0','0','1','1','0','0','1','0','0'])
        self.assertAlmostEqual(to_straight_code(-100),['1','0','0','0','0','0','0','0','0','1','1','0','0','1','0','0'])
        self.assertAlmostEqual(to_straight_code(500),['0','0','0','0','0','0','0','1','1','1','1','1','0','1','0','0'])
        self.assertAlmostEqual(to_straight_code(-500),['1','0','0','0','0','0','0','1','1','1','1','1','0','1','0','0'])
        self.assertAlmostEqual(to_straight_code(2000),['0','0','0','0','0','1','1','1','1','1','0','1','0','0','0','0'])
        self.assertAlmostEqual(to_straight_code(-2000),['1','0','0','0','0','1','1','1','1','1','0','1','0','0','0','0'])
        self.assertAlmostEqual(to_straight_code(32767),['0','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'])
        self.assertAlmostEqual(to_straight_code(-32767),['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'])

class Test_to_reverse_code(unittest.TestCase):
    def test_value(self):
        self.assertAlmostEqual(to_reverse_code(0),['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'])
        self.assertAlmostEqual(to_reverse_code(1),to_straight_code(1))
        self.assertAlmostEqual(to_reverse_code(-1),['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0'])

        self.assertAlmostEqual(to_reverse_code(2),to_straight_code(2))
        self.assertAlmostEqual(to_reverse_code(-2),['1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','1'])

        self.assertAlmostEqual(to_reverse_code(5),to_straight_code(5))
        self.assertAlmostEqual(to_reverse_code(-5),['1','1','1','1','1','1','1','1','1','1','1','1','1','0','1','0'])

        self.assertAlmostEqual(to_reverse_code(10),to_straight_code(10))
        self.assertAlmostEqual(to_reverse_code(-10),['1','1','1','1','1','1','1','1','1','1','1','1','0','1','0','1'])

        self.assertAlmostEqual(to_reverse_code(100),to_straight_code(100))
        self.assertAlmostEqual(to_reverse_code(-100),['1','1','1','1','1','1','1','1','1','0','0','1','1','0','1','1'])

        self.assertAlmostEqual(to_reverse_code(32767),to_straight_code(32767))
        self.assertAlmostEqual(to_reverse_code(-32767),['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'])

class Test_to_additional_code(unittest.TestCase):
    def test_value(self):
        self.assertAlmostEqual(to_additional_code(0),['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'])
        self.assertAlmostEqual(to_additional_code(1),to_straight_code(1))
        self.assertAlmostEqual(to_additional_code(-1),['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'])

        self.assertAlmostEqual(to_additional_code(2),to_straight_code(2))
        self.assertAlmostEqual(to_additional_code(-2),['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0'])

        self.assertAlmostEqual(to_additional_code(5),to_straight_code(5))
        self.assertAlmostEqual(to_additional_code(-5),['1','1','1','1','1','1','1','1','1','1','1','1','1','0','1','1'])

        self.assertAlmostEqual(to_additional_code(10),to_straight_code(10))
        self.assertAlmostEqual(to_additional_code(-10),['1','1','1','1','1','1','1','1','1','1','1','1','0','1','1','0'])

        self.assertAlmostEqual(to_additional_code(100),to_straight_code(100))
        self.assertAlmostEqual(to_additional_code(-100),['1','1','1','1','1','1','1','1','1','0','0','1','1','1','0','0'])

        self.assertAlmostEqual(to_additional_code(32767),to_straight_code(32767))
        self.assertAlmostEqual(to_additional_code(-32767),['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'])
        
class Test_straight_code_operation(unittest.TestCase):
    def test_positive_value(self):
        self.assertAlmostEqual(straight_code_operation(0,0),sum_of_positive(0,0))
        self.assertAlmostEqual(straight_code_operation(1,1),sum_of_positive(1,1))
        self.assertAlmostEqual(straight_code_operation(100,100),sum_of_positive(100,100))
    def test_negative_value(self):
        self.assertAlmostEqual(straight_code_operation(-1,-1),to_straight_code(-2))
        self.assertAlmostEqual(straight_code_operation(-100,-100),to_straight_code(-200))
    def test_first_pos(self):
        self.assertAlmostEqual(straight_code_operation(1,-1),sum_of_positive(0,0))
        self.assertAlmostEqual(straight_code_operation(10,-9),to_straight_code(1))
        self.assertAlmostEqual(straight_code_operation(50,-49),to_straight_code(1))     
        self.assertAlmostEqual(straight_code_operation(5,-10),to_straight_code(-5))
        self.assertAlmostEqual(straight_code_operation(50,-100),to_straight_code(-50))
    def test_sec_pos(self):
        self.assertAlmostEqual(straight_code_operation(-1,1),sum_of_positive(0,0))
        self.assertAlmostEqual(straight_code_operation(-10,9),to_straight_code(-1))
        self.assertAlmostEqual(straight_code_operation(-50,49),to_straight_code(-1))     
        self.assertAlmostEqual(straight_code_operation(-5,10),to_straight_code(5))
        self.assertAlmostEqual(straight_code_operation(-50,100),to_straight_code(50))
    def test_all_neg(self):
        self.assertAlmostEqual(straight_code_operation(-1,-1),to_straight_code(-2))
        self.assertAlmostEqual(straight_code_operation(-10,-10),to_straight_code(-20))
        self.assertAlmostEqual(straight_code_operation(-50,-50),to_straight_code(-100))
        self.assertAlmostEqual(straight_code_operation(-1000,-1000),to_straight_code(-2000))

class Test_reverse_code_operation(unittest.TestCase):
    def test_positive_value(self):
        self.assertAlmostEqual(reverse_code_operation(0,0),sum_of_positive(0,0))
        self.assertAlmostEqual(reverse_code_operation(1,1),sum_of_positive(1,1))
        self.assertAlmostEqual(reverse_code_operation(100,100),sum_of_positive(100,100))
    
    def test_negative_value(self):
        self.assertAlmostEqual(reverse_code_operation(-1,-1),to_reverse_code(-2))
        self.assertAlmostEqual(reverse_code_operation(-100,-100),to_reverse_code(-200))
    def test_first_pos(self):
        self.assertAlmostEqual(reverse_code_operation(2,-1),to_reverse_code(1))
        self.assertAlmostEqual(reverse_code_operation(10,-9),to_reverse_code(1))
        self.assertAlmostEqual(reverse_code_operation(50,-49),to_reverse_code(1))     
        self.assertAlmostEqual(reverse_code_operation(5,-10),to_reverse_code(-5))
        self.assertAlmostEqual(reverse_code_operation(50,-100),to_reverse_code(-50))
    def test_sec_pos(self):
        self.assertAlmostEqual(reverse_code_operation(-2,1),to_reverse_code(-1))
        self.assertAlmostEqual(reverse_code_operation(-10,9),to_reverse_code(-1))
        self.assertAlmostEqual(reverse_code_operation(-50,49),to_reverse_code(-1))     
        self.assertAlmostEqual(reverse_code_operation(-5,10),to_reverse_code(5))
        self.assertAlmostEqual(reverse_code_operation(-50,100),to_reverse_code(50))
    def test_all_neg(self):
        self.assertAlmostEqual(reverse_code_operation(-1,-1),to_reverse_code(-2))
        self.assertAlmostEqual(reverse_code_operation(-10,-10),to_reverse_code(-20))
        self.assertAlmostEqual(reverse_code_operation(-50,-50),to_reverse_code(-100))
        self.assertAlmostEqual(reverse_code_operation(-1000,-1000),to_reverse_code(-2000))

class Test_additional_code_operation(unittest.TestCase):
    def test_positive_value(self):
        self.assertAlmostEqual(additional_code_operation(0,0),sum_of_positive(0,0))
        self.assertAlmostEqual(additional_code_operation(1,1),sum_of_positive(1,1))
        self.assertAlmostEqual(additional_code_operation(100,100),sum_of_positive(100,100))
    
    def test_negative_value(self):
        self.assertAlmostEqual(additional_code_operation(-1,-1),to_additional_code(-2))
        self.assertAlmostEqual(additional_code_operation(-100,-100),to_additional_code(-200))
    def test_first_pos(self):
        self.assertAlmostEqual(additional_code_operation(2,-1),to_additional_code(1))
        self.assertAlmostEqual(additional_code_operation(10,-9),to_additional_code(1))
        self.assertAlmostEqual(additional_code_operation(50,-49),to_additional_code(1))     
        self.assertAlmostEqual(additional_code_operation(5,-10),to_additional_code(-5))
        self.assertAlmostEqual(additional_code_operation(50,-100),to_additional_code(-50))
    def test_sec_pos(self):
        self.assertAlmostEqual(additional_code_operation(-2,1),to_additional_code(-1))
        self.assertAlmostEqual(additional_code_operation(-10,9),to_additional_code(-1))
        self.assertAlmostEqual(additional_code_operation(-50,49),to_additional_code(-1))     
        self.assertAlmostEqual(additional_code_operation(-5,10),to_additional_code(5))
        self.assertAlmostEqual(additional_code_operation(-50,100),to_additional_code(50))
    def test_all_neg(self):
        self.assertAlmostEqual(additional_code_operation(-1,-1),to_additional_code(-2))
        self.assertAlmostEqual(additional_code_operation(-10,-10),to_additional_code(-20))
        self.assertAlmostEqual(additional_code_operation(-50,-50),to_additional_code(-100))
        self.assertAlmostEqual(additional_code_operation(-1000,-1000),to_additional_code(-2000))

class Test_multiplication(unittest.TestCase):
    def test_positive_value(self):
        self.assertAlmostEqual(multiplication(0,0),to_additional_code(0))
        self.assertAlmostEqual(multiplication(1,0),to_additional_code(0))
        self.assertAlmostEqual(multiplication(1,2),to_additional_code(2))
        self.assertAlmostEqual(multiplication(2,2),to_additional_code(4))
        self.assertAlmostEqual(multiplication(10,10),to_additional_code(100))
        self.assertAlmostEqual(multiplication(100,100),to_additional_code(10000))

    def test_negative_value(self):
        self.assertAlmostEqual(multiplication(0,0),to_additional_code(0))
        self.assertAlmostEqual(multiplication(-1,-2),to_additional_code(2))
        self.assertAlmostEqual(multiplication(-2,-2),to_additional_code(4))
        self.assertAlmostEqual(multiplication(-10,-10),to_additional_code(100))
        self.assertAlmostEqual(multiplication(-100,-100),to_additional_code(10000))

    def test_mix_value(self):
        self.assertAlmostEqual(multiplication(0,0),to_straight_code(0))
        self.assertAlmostEqual(multiplication(-1,2),to_straight_code(-2))
        self.assertAlmostEqual(multiplication(2,-2),to_straight_code(-4))
        self.assertAlmostEqual(multiplication(-10,10),to_straight_code(-100))
        self.assertAlmostEqual(multiplication(100,-100),to_straight_code(-10000))

class Test_division(unittest.TestCase):
    def test_int_value(self):
        self.assertAlmostEqual(division(1,1),'00000000001,00000')
        self.assertAlmostEqual(division(2,1),'00000000010,00000')
        self.assertAlmostEqual(division(3,1),'00000000011,00000')
        self.assertAlmostEqual(division(4,2),'00000000010,00000')
        self.assertAlmostEqual(division(10,2),'00000000101,00000')
    
    def test_float_falue(self):
        self.assertAlmostEqual(division(1,2),'00000000000,10000')
        self.assertAlmostEqual(division(1,3),'00000000000,01010')
        self.assertAlmostEqual(division(1,5),'00000000000,00110')
        self.assertAlmostEqual(division(5,3),'00000000001,10101')
        self.assertAlmostEqual(division(100,71),'00000000001,01101')

    def test_sign(self):
        self.assertAlmostEqual(division(-1,1),'-00000000001,00000')
        self.assertAlmostEqual(division(2,-1),'-00000000010,00000')
        self.assertAlmostEqual(division(-3,1),'-00000000011,00000')
        self.assertAlmostEqual(division(4,-2),'-00000000010,00000')
        self.assertAlmostEqual(division(-10,2),'-00000000101,00000')

class Test_input_data(unittest.TestCase):
    def test_int_input(self):
        self.failureException(input_data(0,0))
        self.failureException(input_data(1000,12321))
        self.failureException(input_data(-10123,123123))
        self.failureException(input_data(12323,-213120))
    def test_float_input(self):
        self.failureException(input_data(0.121,0.121))
        self.failureException(input_data(1000.121,12321.121))
        self.failureException(input_data(-10123.121,123123.121))
        self.failureException(input_data(12323.121,-213120.121))
    def test_for_exeptions(self):
        self.assertRaises(Exception,input_data(10,'some_string'))
        self.assertRaises(Exception,input_data('some_string',10))
        self.assertRaises(Exception,input_data(10.123,'some_string'))
        self.assertRaises(Exception,input_data('some_string',10.123))

class Test_to_float(unittest.TestCase):
    def value_test(self):
        test_val="0000000000000000."
        self.assertAlmostEqual(to_float(0.9),test_val+'0011001100110011')
        self.assertAlmostEqual(to_float(0.6),test_val+'1001100110011010')
        self.assertAlmostEqual(to_float(0.4),test_val+'0110011001100110')
        self.assertAlmostEqual(to_float(0.2),test_val+'0011001100110011')
        self.assertAlmostEqual(to_float(0.1),test_val+'0001100110011010')
    def small_test_values(self):
        test_val="0000000000000000."
        self.assertAlmostEqual(to_float(0.09),test_val+'0001011100001010')
        self.assertAlmostEqual(to_float(0.06),test_val+'0000111101011100')
        self.assertAlmostEqual(to_float(0.04),test_val+'0000101000111101')
        self.assertAlmostEqual(to_float(0.02),test_val+'0000010100011111')
        self.assertAlmostEqual(to_float(0.01),test_val+'0000001010001111')
    def very_small_test_values(self):
        test_val="0000000000000000."
        self.assertAlmostEqual(to_float(0.0009),test_val+'0000000000111011')
        self.assertAlmostEqual(to_float(0.0006),test_val+'0000000000100111')
        self.assertAlmostEqual(to_float(0.0004),test_val+'0000000000011010')
        self.assertAlmostEqual(to_float(0.0002),test_val+'0000000000001101')
        self.assertAlmostEqual(to_float(0.0001),test_val+'0000000000000111')

class Test_float_sum(unittest.TestCase):
    def vlaue_test(self):
        self.assertAlmostEqual(float_sum(0.45,0.45),to_float(0.9))
        self.assertAlmostEqual(float_sum(0.3,0.3),to_float(0.6))
        self.assertAlmostEqual(float_sum(0.2,0.2),to_float(0.4))
        self.assertAlmostEqual(float_sum(0.05,0.05),to_float(0.1))


