# 导入所需的第三方库
import requests
import pandas as pd
import matplotlib.pyplot as plt

# requests库示例：发送HTTP请求
print("\nrequests库使用示例：")

# 发送GET请求
def get_weather(city):
    """获取城市天气信息（示例API）"""
    try:
        # 这是一个示例API URL，实际使用时需要替换为真实的天气API
        url = f"https://api.example.com/weather?city={city}"
        response = requests.get(url)
        
        # 检查请求是否成功
        response.raise_for_status()
        
        # 解析JSON响应
        data = response.json()
        return data
    except requests.RequestException as e:
        return f"请求错误：{str(e)}"

# 由于这是示例代码，我们模拟API响应
print("模拟天气API请求示例")
print("注意：这是模拟数据，实际使用需要替换为真实API")

# pandas库示例：数据处理
print("\npandas库使用示例：")

# 创建示例数据
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 35, 28],
    '成绩': [85, 92, 78, 95]
}

# 创建DataFrame
df = pd.DataFrame(data)
print("\n原始数据：")
print(df)

# 基本统计分析
print("\n基本统计信息：")
print(df.describe())

# 数据筛选
print("\n成绩大于85的学生：")
print(df[df['成绩'] > 85])

# 数据排序
print("\n按成绩排序：")
print(df.sort_values(by='成绩', ascending=False))

# 数据可视化
plt.figure(figsize=(10, 6))
plt.bar(df['姓名'], df['成绩'])
plt.title('学生成绩柱状图')
plt.xlabel('姓名')
plt.ylabel('成绩')

# 保存图表
plt.savefig('student_scores.png')
plt.close()

print("\n数据可视化图表已保存为'student_scores.png'")