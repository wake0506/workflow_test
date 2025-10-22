def dedupe(items):
    """
    去重函数 - 保留顺序
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def add_numbers(a, b):
    """
    实现两个数字的加法运算
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("输入参数必须是数字")
    return a + b

if __name__ == "__main__":
    # 测试去重功能
    sample_data = [1, 2, 2, 3, 4, 4, 5]
    result = list(dedupe(sample_data))
    print(f"原始数据: {sample_data}")
    print(f"去重结果: {result}")
    
    # 测试加法功能
    print(f"加法测试: 5 + 3 = {add_numbers(5, 3)}")