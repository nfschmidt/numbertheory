import pytest
import divisibility as d

numbers_sample = [1, 10, 48, 2534, 46756456]

class TestGcd():

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
        assert d.gcd(a, b) == d.gcd(b, a)
        
    def test_gcd_of_0_and_0_raises_ValueError(self):
        with pytest.raises(ValueError) as exception_info:
            d.gcd(0, 0)
            
        assert 'All numbers cannot be 0' in str(exception_info.value)

    def test_gdc_is_non_negative(self):
        assert d.gcd(-10, 100) >= 0
        assert d.gcd(10, -100) >= 0


class TestGcdLinearCombination():

    ab_xy = [
        (7469, 2464, 1, -3),
        (423, 198, -7, 15),
        (93, 81, 7, -8),
        (3587, 1819, -36, 71)
    ]
    
    @pytest.mark.parametrize('number', numbers_sample)
    def test_with_positive_numbers_a_multiple_of_b_the_result_is_0_1(self, number):
        assert d.gcd_linear_combination(number * 5, number) == (0, 1)

    @pytest.mark.parametrize('number', numbers_sample)
    def test_positive_a_multiple_of_negative_b_result_is_0_negative1(self, number):
        assert d.gcd_linear_combination(number * 5, -number) == (0, -1)

    @pytest.mark.parametrize('number', numbers_sample)
    def test_with_positive_numbers_b_multiple_of_a_the_result_is_1_0(self, number):
        assert d.gcd_linear_combination(number, number * 5) == (1, 0)

    @pytest.mark.parametrize('number', numbers_sample)
    def test_positive_b_multiple_of_negative_a_result_is_negative1_0(self, number):
        assert d.gcd_linear_combination(-number, number * 5) == (-1, 0)

    def test_second_reminder_equals_0(self):
        assert d.gcd_linear_combination(88, 12) == (1, -7)

    @pytest.mark.parametrize('a, b, x, y', ab_xy)
    def test_positive_numbers_a_greater_than_b_more_than_2_reminders(self, a, b, x, y):
        assert d.gcd_linear_combination(a, b) == (x, y)

    @pytest.mark.parametrize('a, b, x, y', ab_xy)
    def test_positive_numbers_b_greater_than_a_more_than_2_reminders(self, a, b, x, y):
        assert d.gcd_linear_combination(b, a) == (y, x)

    @pytest.mark.parametrize('a, b, x, y', ab_xy)
    def test_positive_a_negative_b(self, a, b, x, y):
        assert d.gcd_linear_combination(a, -b) == (x, -y)

    @pytest.mark.parametrize('a, b, x, y', ab_xy)
    def test_positive_b_negative_a(self, a, b, x, y):
        assert d.gcd_linear_combination(-a, b) == (-x, y)

    @pytest.mark.parametrize('a, b, x, y', ab_xy)
    def test_negative_numbers(self, a, b, x, y):
        assert d.gcd_linear_combination(-a, -b) == (-x, -y)

    def test_raises_exception_if_both_arguments_are_0(self):
        with pytest.raises(ValueError) as error_info:
            d.gcd_linear_combination(0, 0)

        assert 'All numbers cannot be 0' in str(error_info.value) 
