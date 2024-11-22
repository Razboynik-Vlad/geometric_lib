import sys
sys.path.insert(0, '/home/vlad_kh/geometric_lib')
import unittest
from calculate import *

expected_result = [6.283185307179586,
                    188.49555921538757,
                    3.141592653589793,
                    2827.4333882308138, 
                    4, 
                    120,
                    1, 
                    900]

class TestCalc(unittest.TestCase):
    def test_valid_input_1(self):
        # Arrange/given
        global expected_result
        
        # Act/when
            
        result = calc("circle", "perimeter", [1])
                
        # Assert/then
        self.assertEqual(result, expected_result[0])

    def test_valid_input_2(self):
        # Arrange/given
        global expected_result
        
        # Act/when
            
        result = calc("circle", "area", [1])
                
        # Assert/then
        self.assertEqual(result, expected_result[2])
    
    def test_valid_input_3(self):
        # Arrange/given
        global expected_result
        
        # Act/when
            
        result = calc("square", "perimeter", [1])
                
        # Assert/then
        self.assertEqual(result, expected_result[4])
        
    def test_valid_input_4(self):
        # Arrange/given
        global expected_result
        
        # Act/when
            
        result = calc("square", "area", [1])
                
        # Assert/then
        self.assertEqual(result, expected_result[6])
        
    def test_valid_input_5(self):
        # Arrange/given
        global expected_result
        
        # Act/when
            
        result = calc("circle", "perimeter", [30])
                
        # Assert/then
        self.assertEqual(result, expected_result[1])
        
    def test_valid_input_6(self):
        # Arrange/given
        global expected_result
        
        # Act/when
            
        result = calc("circle", "area", [30])
                
        # Assert/then
        self.assertEqual(result, expected_result[3])
        
    def test_valid_input_7(self):
        # Arrange/given
        global expected_result
        
        # Act/when
            
        result = calc("square", "perimeter", [30])
                
        # Assert/then
        self.assertEqual(result, expected_result[5])
        
    def test_valid_input_8(self):
        # Arrange/given
        global expected_result
        
        # Act/when
            
        result = calc("square", "area", [30])
                
        # Assert/then
        self.assertEqual(result, expected_result[7])
        
    def test_invalid_input(self):
        # Arrange
        global expected_result
        
        # Act & Assert
        with self.assertRaises(ValueError):
            calc("square", "area", [-1])

if __name__ == '__main__':
    unittest.main()
     
