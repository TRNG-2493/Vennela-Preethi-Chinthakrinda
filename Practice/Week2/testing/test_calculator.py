import unittest

from calculator import add
from calculator import divide
from calculator import is_even

#wr Test
# name of testcase name shd be descriptive.
class TestAdd(unittest.TestCase):
    #def setUp(self):
        #print("============SETUP================")
        
    #def tearDown(self):
        #print("===========TEARDOWN===============")
        
    #fixtures - useful for setting up and cleaning up
    
    #@classmethod #decorator
    #def setUpClass(cls):
    #    print("SET UP CLASS")
    
    def test_add_two_positive_number(self):
        # Arrange
        x,y=10,20
        expected_result = 30
        # Act
        result=add(x,y)
        # Assert
        self.assertEqual(expected_result,result,"Test failed") #displayes msg only when test fails
    
    def test_add_two_negative_number(self):
        self.assertEqual(add(-2,-3),-5)
    
    def test_add_one_negative_one_positive_number(self):
        self.assertEqual(add(10,-5),5,msg="Test failed")
    
    def test_add_two_zeros(self):
        self.assertEqual(add(0,0),0,msg="Expected result is zero, test failed")
    
    def test_add_positive_and_zero(self):
        self.assertEqual(add(3,0),3)
    
    def test_add_negative_and_zero(self):
            self.assertEqual(add(-10,0),-10)
    
class TestDiv(unittest.TestCase):
    
    def test_divide_evenly(self):
        self.assertEqual(divide(10,2),5)
    
    def test_divide_floats_approximately(self):
        self.assertAlmostEqual(divide(5,2),2.5,msg="Test failed")
    
    def test_divide_floats(self):
        #self.assertEqual(round(divide(10,3),3),3.333,msg="test failed")
        
        #use round and assertEqual to round off to n decimal places, round(divide(10,3),3 - round off to 3 decimal places.)
        #or
        self.assertAlmostEqual(divide(10,3),3.333,places=3,msg="test failed")
        
    def test_divide_by_zero_exception(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
    
    def test_divide_by_zero_message(self):
        with self.assertRaises(ZeroDivisionError) as ctx:
            divide(1, 0)
        self.assertIn("zero", str(ctx.exception))   

class TestEven(unittest.TestCase):
    
    def test_is_even_number(self):
        #self.assertEqual(is_even(2),True)
        #self.assertEqual(is_even(0),True)
        #self.assertEqual(is_even(-3),False)
        #self.assertEqual(is_even(7),False)
        # if one fails, all fails and we cannot understand where or for
        # which number we got failed, instead of writing a unit test for each number in each line
        # we can write define the test cases.
        cases=[(2,True),(0,True),(-3,False),(7,False)] # (number,expected); list of tuples
        for value, expected in cases: #loop thru test cases
            with self.subTest(number=value): #separate subtest for each number
                self.assertEqual(is_even(value), expected)
                            
if __name__ == "__main__":
    unittest.main()
        