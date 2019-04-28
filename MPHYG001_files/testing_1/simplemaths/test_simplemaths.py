import pytest
from simplemaths.simplemaths import SimpleMaths as sm
import unittest 

square = [(1,1), (2,4), (3,9), (4,16), (5,25), (6, 36)]
factorial = [(1,1), (2,2), (3,6), (4,24), (5,120), (6, 720)]
power = [(1,1), (2,8), (3,27), (4,64), (5,125)]
oddeven = [(0, 'Even'), (2, 'Even'), (4, 'Even'), (6, 'Even'), (8, 'Even'), (1, 'Odd'), (3, 'Odd'), (5, 'Odd'), (7, 'Odd'), (9, 'Odd')]
square_root = [(36, 6), (25, 5), (16,4), (9,3), (4,2)]
neg_square_root = [(-3, 1.0605752387249068e-16+1.7320508075688772j)]

class TestSimpleMaths():
    def test_constructor_float(self):
        with pytest.raises(TypeError) as exception:
            number=sm(3.9)
            exception = number.square()

    @pytest.mark.parametrize('number, output', square)
    def test_square(self, number, output):
        number = sm(number)
        answer = number.square()
        assert answer == output
        
    @pytest.mark.parametrize('number, output', factorial)
    def test_factorial(self, number, output):
        number = sm(number)
        answer = number.factorial()
        assert answer == output
        
    @pytest.mark.parametrize('number, output', oddeven)
    def test_odd_or_even(self, number, output):
        number = sm(number)
        answer = number.odd_or_even()
        assert answer == output
        
    @pytest.mark.parametrize('number, output', square_root)
    def test_square_root(self, number, output):
        number = sm(number)
        answer = number.square_root()
        assert answer == output
    
    @pytest.mark.parametrize('number, output', neg_square_root)
    def test_neg_square_root(self, number, output):
        number = sm(number)
        answer = number.square_root()
        assert answer == pytest.approx(output, 0.1)
        
      
#            def test_correct_shelves_are_inputted(self):
#        testInput = input['merlins']
#        self.assertTrue(Laboratory(testInput['lower'], testInput['upper']))
#        
#        number = SimpleMaths(3)
#
#print(number.square())