## python基本用法和两个小demo

### 1. Python基础语法 (hello.py)
- 注释的使用
- print() 函数
- 变量定义和使用
- 基本数据类型（整数、浮点数、布尔值、字符串）
- 格式化字符串（f-string）

### 2. 基础数据结构 (basic_data_structures.py)
- 列表（List）的创建和操作
  - 列表的增删改查
  - 列表切片和遍历
  - 列表推导式
- 字典（Dictionary）的使用
  - 字典的创建和访问
  - 字典方法（keys, values, items）
  - 字典推导式
- 控制流程
  - if 条件语句
  - for 循环
  - while 循环
  - break 和 continue 语句

### 3. 函数和类 (functions_and_classes.py)
- 函数的定义和使用
  - 参数传递（位置参数、关键字参数）
  - 带默认参数的函数
  - 返回值处理
- 类的定义和使用
  - 构造函数（__init__）
  - 类方法和实例方法
  - 属性访问和封装
  - 继承和多态

### 4. Python高级特性 (advanced_features.py)
- 模块和包
  - 模块导入（math、random、datetime）
  - 包的使用示例
  - 自定义模块创建
- 异常处理
  - try-except 语句
  - 自定义异常
  - 异常的传播和捕获
- 文件操作
  - 文件的读写操作
  - 上下文管理器（with语句）
  - 文件和目录处理

### 5. 第三方库使用 (third_party_libs.py)
- requests库
  - HTTP请求（GET、POST）
  - 请求参数和头部设置
  - 响应处理和异常处理
- pandas库
  - DataFrame的创建和基本操作
  - 数据筛选和排序
  - 基本统计分析
- matplotlib库
  - 基本图表绘制
  - 图表样式设置
  - 图表保存和展示

# Python 天气查询与分析工具

这是一个基于Python的天气查询和分析工具，利用OpenWeatherMap API获取实时天气数据，并提供数据分析和可视化功能。

## 主要功能

- 实时天气查询
- 天气预报（5天）
- 多城市天气对比
- 天气数据分析
- 数据可视化

## 使用的数据科学库

本项目使用了多个Python数据科学库来处理和可视化天气数据。详细的库介绍、特性说明和代码示例请参考：[Python数据科学库介绍](data_science_libraries.md)

## 安装依赖

```bash
pip install pandas matplotlib seaborn requests tabulate
```
## 计划学习内容

### 6. 实战项目
- 天气查询项目
  - API 调用
  - JSON 数据处理
  - 命令行界面
- 数据分析项目
  - 数据清洗和预处理
  - 数据可视化
  - 统计分析报告

### 7. Web自动化测试 (Selenium)
- Selenium基础
  - WebDriver的安装和配置
  - 浏览器驱动设置
  - 页面导航和等待策略
- 元素定位
  - ID、Name、Class定位
  - XPath和CSS选择器
  - 相对定位和链式定位
- 页面交互
  - 点击和输入操作
  - 下拉框和弹窗处理
  - 文件上传和下载
- 高级特性
  - 显式等待和隐式等待
  - Frame和Window切换
  - JavaScript执行
  - 截图和日志记录
- 最佳实践
  - Page Object设计模式
  - 测试用例组织
  - 并发测试执行
  - 持续集成配置

## 环境配置

### Selenium环境配置
```bash
# 安装Selenium包
pip install selenium

# 安装浏览器驱动（以Chrome为例）
# MacOS
brew install chromedriver

# Windows（需要手动下载对应版本的chromedriver）
# 1. 访问 https://sites.google.com/chromium.org/driver/
# 2. 下载与Chrome浏览器版本匹配的驱动
# 3. 将驱动放入系统PATH环境变量中
```

### 示例代码
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建Chrome浏览器实例
driver = webdriver.Chrome()

# 访问网页
driver.get("https://www.example.com")

# 等待元素可见并点击
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "search")))
element.click()

# 输入文本
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium自动化测试")

# 提交表单
search_box.submit()

# 关闭浏览器
driver.quit()
```

## 学习资源
- Python官方文档：https://docs.python.org/zh-cn/3/
- Selenium官方文档：https://www.selenium.dev/documentation/
- 在线教程和实践平台
  - Python教程：https://www.runoob.com/python3
  - LeetCode Python练习：https://leetcode.cn/
- 示例代码和练习
  - 本地示例代码
  - 课后练习题

## 注意事项
- 每个主题都配有相应的示例代码，建议动手实践
- 遇到问题时优先查阅官方文档
- 保持代码规范，注重编程风格
- 多做练习，加深对知识点的理解
- 及时总结和复习已学内容
