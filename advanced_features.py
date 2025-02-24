# 模块导入示例
import math
import random
from datetime import datetime

print("\n模块导入和使用示例：")
print(f"圆周率π的值：{math.pi:.2f}")
print(f"生成1-10的随机数：{random.randint(1, 10)}")
print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 异常处理示例
print("\n异常处理示例：")

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "错误：除数不能为零"
    except TypeError:
        return "错误：请输入数字"

# 测试异常处理
print(f"10 / 2 = {divide_numbers(10, 2)}")
print(f"10 / 0 = {divide_numbers(10, 0)}")
print(f"'10' / 2 = {divide_numbers('10', 2)}")

# 自定义异常
class AgeError(Exception):
    """年龄验证异常"""
    pass

def verify_age(age):
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0 or age > 150:
        raise AgeError("年龄必须在0到150岁之间")
    return f"年龄{age}验证通过"

print("\n自定义异常示例：")
try:
    print(verify_age(20))  # 正常情况
    print(verify_age(-5))  # 触发AgeError
except (TypeError, AgeError) as e:
    print(f"错误：{str(e)}")

# 文件操作示例
print("\n文件操作示例：")

# 写入文件
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write("这是第一行\n")
    f.write("这是第二行\n")

# 读取文件
print("读取文件内容：")
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# 追加内容
with open('example.txt', 'a', encoding='utf-8') as f:
    f.write("这是追加的第三行\n")

# 再次读取
print("追加后的文件内容：")
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)