import pytest
from app.app import dedupe, add_numbers

def test_dedupe_function():
    """测试去重功能"""
    assert list(dedupe([1, 2, 2, 3])) == [1, 2, 3]
    assert list(dedupe(['a', 'b', 'b', 'c'])) == ['a', 'b', 'c']
    assert list(dedupe([])) == []
    assert list(dedupe([1, 2, 3])) == [1, 2, 3]

class TestAdditionFunctionality:
    """测试加法功能"""
    
    def test_add_positive_numbers(self):
        """测试正数加法"""
        assert add_numbers(2, 3) == 5
        assert add_numbers(10, 15) == 25
    
    def test_add_negative_numbers(self):
        """测试负数加法"""
        assert add_numbers(-2, -3) == -5
        assert add_numbers(-10, 5) == -5
    
    def test_add_float_numbers(self):
        """测试浮点数加法"""
        assert add_numbers(2.5, 3.5) == 6.0
    
    def test_add_invalid_input(self):
        """测试无效输入"""
        with pytest.raises(ValueError):
            add_numbers("2", 3)