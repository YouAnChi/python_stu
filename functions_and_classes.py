# 函数的定义和使用
def calculate_average(numbers):
    """计算一组数字的平均值
    Args:
        numbers: 数字列表
    Returns:
        平均值
    """
    if not numbers:  # 检查列表是否为空
        return 0
    return sum(numbers) / len(numbers)

# 函数使用示例
scores = [85, 92, 78, 90, 88]
print(f"\n函数使用演示：")
print(f"成绩列表: {scores}")
print(f"平均分: {calculate_average(scores):.2f}")

# 带默认参数的函数
def greet(name, greeting="你好"):
    return f"{greeting}，{name}！"

print(f"\n带默认参数的函数：")
print(greet("小明"))  # 使用默认问候语
print(greet("小红", "早上好"))  # 自定义问候语

# 类的定义和使用
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.scores = {}
    
    def add_score(self, subject, score):
        """添加一个科目的成绩"""
        self.scores[subject] = score
    
    def get_average_score(self):
        """计算平均成绩"""
        if not self.scores:  # 如果没有成绩记录
            return 0
        return calculate_average(list(self.scores.values()))
    
    def introduce(self):
        """学生自我介绍"""
        return f"我叫{self.name}，今年{self.age}岁"

# 类的使用示例
print(f"\n类的使用演示：")
# 创建学生对象
student = Student("小华", 16)

# 添加成绩
student.add_score("语文", 88)
student.add_score("数学", 95)
student.add_score("英语", 90)

# 使用学生类的方法
print(student.introduce())
print(f"各科成绩: {student.scores}")
print(f"平均成绩: {student.get_average_score():.2f}")