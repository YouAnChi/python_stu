# Python数据科学库介绍

本文档详细介绍了项目中使用的主要数据科学库，包括它们的特性、使用场景和代码示例。

## Pandas

Pandas是Python中最常用的数据处理库，提供了强大的数据结构和数据分析工具。

### 主要特性
- DataFrame和Series数据结构
- 高效的数据读写（CSV、JSON等）
- 灵活的数据筛选和过滤
- 强大的数据聚合和统计功能
- 时间序列处理

### 常用功能示例

```python
# 创建DataFrame
data = {
    '城市': ['北京', '上海', '广州', '深圳'],
    '温度': [25, 28, 30, 29],
    '湿度': [40, 55, 70, 65]
}
df = pd.DataFrame(data)

# 数据筛选和统计
high_temp_cities = df[df['温度'] > 28]
daily_temp = df.groupby('城市')['温度'].mean()

# 数据导出
df.to_csv('weather_data.csv')

# 基本统计信息
print(df.describe())
```

## Matplotlib

Matplotlib是Python最基础的绘图库，提供了丰富的图表类型和自定义选项。

### 主要特性
- 支持多种图表类型（折线图、柱状图、散点图等）
- 灵活的布局系统
- 详细的图表定制选项
- 支持保存为多种图片格式

### 常用功能示例

```python
# 创建温度趋势图
plt.figure(figsize=(12, 6))
plt.plot(df['城市'], df['温度'], marker='o')
plt.title('城市温度对比')
plt.xlabel('城市')
plt.ylabel('温度 (°C)')
plt.grid(True)

# 创建温湿度对比图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 温度柱状图
ax1.bar(df['城市'], df['温度'])
ax1.set_title('城市温度分布')
ax1.set_ylabel('温度 (°C)')

# 湿度折线图
ax2.plot(df['城市'], df['湿度'], marker='s', color='green')
ax2.set_title('城市湿度分布')
ax2.set_ylabel('湿度 (%)')

plt.tight_layout()
plt.savefig('weather_comparison.png')
```

## Seaborn

Seaborn是基于Matplotlib的统计数据可视化库，提供了更美观的视觉风格和更高级的绘图功能。

### 主要特性
- 内置美观的视觉主题
- 统计图表（箱线图、小提琴图等）
- 多变量数据可视化
- 自动处理分类数据

### 常用功能示例

```python
# 设置视觉主题
sns.set_theme(style="whitegrid")

# 创建温度分布的箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(x='城市', y='温度', data=df)
plt.title('城市温度分布')

# 创建温湿度关系的散点图
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='温度', y='湿度', hue='城市')
plt.title('温度与湿度关系')

# 创建温度分布的小提琴图
plt.figure(figsize=(10, 6))
sns.violinplot(x='城市', y='温度', data=df)
plt.title('城市温度分布（小提琴图）')
```

## 数据可视化最佳实践

1. 选择合适的图表类型
   - 折线图：展示趋势变化
   - 柱状图：比较不同类别的数值
   - 散点图：展示两个变量之间的关系
   - 箱线图：展示数据分布特征

2. 图表美化技巧
   - 设置合适的图表大小和比例
   - 添加清晰的标题和轴标签
   - 使用网格线提高可读性
   - 选择合适的颜色方案

3. 代码组织建议
   - 使用面向对象的方式创建图表
   - 将常用的绘图函数封装为可重用的工具函数
   - 统一设置图表样式
   - 保持代码的可读性和可维护性