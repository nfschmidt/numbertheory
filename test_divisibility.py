import pytest
import divisibility as d


class TestGcd():
    numbers_sample = [1, 10, 48, 2534, 46756456]

    pairs_with_gcd = [
        (7469, 2464, 77),
        (2689, 4001, 1),
        (2947, 3997, 7),
        (1109, 4999, 1),
        (0, 190, 190),
        (1194, 0, 1194),
    ]
    
    @pytest.mark.parametrize("number", numbers_sample)
    def test_gcd_between_number_and_0_is_number(self, number):
        assert d.gcd(0, number) == number
        
    @pytest.mark.parametrize("number", numbers_sample)
    def test_gcd_of_two_equal_numbers_is_the_same_number(self, number):
        assert d.gcd(number, number) == number
            
    @pytest.mark.parametrize("a, b, g", pairs_with_gcd)
    def test_gcd_correctly_computes_gcd(self, a, b, g):
        assert d.gcd(a, b) == g
                
    @pytest.mark.parametrize("a, b, g", pairs_with_gcd)
    def test_gcd_of_a_b_equals_gcd_of_b_a(self, a, b, g):
        assert d.gcd(a, b) == d.gcd(b, a) and d.gcd(b, a) == g
        
    def test_gcd_of_0_and_0_raises_ValueError(self):
        with pytest.raises(ValueError) as exception_info:
            d.gcd(0, 0)
            
        assert 'Both numbers cannot be 0' in str(exception_info.value)

    def test_gdc_is_non_negative(self):
        assert d.gcd(-10, 100) >= 0
        assert d.gcd(10, -100) >= 0
