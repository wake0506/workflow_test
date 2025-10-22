import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.app import dedupe

def test_dedupe():
    # 测试基础去重功能
    input_data = [1, 2, 2, 3, 4, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert list(dedupe(input_data)) == expected
    
    # 测试空列表
    assert list(dedupe([])) == []
    
    # 测试字符串去重
    assert list(dedupe(['a', 'b', 'b', 'c'])) == ['a', 'b', 'c']