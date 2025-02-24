# 列表（List）的使用演示
fruits = ["苹果", "香蕉", "橙子"]  # 创建一个列表
print("\n列表操作演示：")
print(f"原始水果列表: {fruits}")

# 列表操作
fruits.append("葡萄")  # 添加元素
print(f"添加葡萄后: {fruits}")
print(f"第一个水果是: {fruits[0]}")
print(f"列表长度: {len(fruits)}")

# 字典（Dictionary）的使用演示
student = {  # 创建一个字典
    "name": "小明",
    "age": 18,
    "scores": {"语文": 90, "数学": 95, "英语": 88}
}

print("\n字典操作演示：")
print(f"学生信息: {student}")
print(f"学生姓名: {student['name']}")
print(f"数学成绩: {student['scores']['数学']}")

# 控制流程 - if语句
print("\nif语句演示：")
score = student['scores']['数学']
if score >= 90:
    print("数学成绩优秀！")
elif score >= 80:
    print("数学成绩良好！")
else:
    print("数学成绩需要提高！")

# 控制流程 - for循环
print("\nfor循环演示：")
print("水果清单：")
for index, fruit in enumerate(fruits, 1):
    print(f"{index}. {fruit}")

# while循环
print("\nwhile循环演示：")
count = 3
while count > 0:
    print(f"倒计时: {count}")
    count -= 1
print("循环结束！")