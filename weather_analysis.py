import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import numpy as np

class WeatherAnalysis:
    def __init__(self):
        self.data = None
    
    def load_data(self, file_path):
        """加载天气数据CSV文件"""
        try:
            self.data = pd.read_csv(file_path)
            # 将日期列转换为datetime类型
            self.data['日期'] = pd.to_datetime(self.data['日期'])
            return True
        except Exception as e:
            print(f'加载数据失败: {str(e)}')
            return False
    
    def analyze_temperature_trend(self, save_path=None):
        """分析温度趋势"""
        if self.data is None:
            return '请先加载数据'
        
        # 提取温度数值
        self.data['温度数值'] = self.data['温度'].str.rstrip('°C').astype(float)
        
        # 计算每日平均温度
        daily_temp = self.data.groupby('日期')['温度数值'].mean()
        
        # 绘制温度趋势图
        plt.figure(figsize=(12, 6))
        plt.plot(daily_temp.index, daily_temp.values, marker='o')
        plt.title('每日平均温度趋势')
        plt.xlabel('日期')
        plt.ylabel('温度 (°C)')
        plt.grid(True)
        plt.xticks(rotation=45)
        
        if save_path:
            plt.savefig(f'{save_path}_temperature_trend.png', bbox_inches='tight')
            plt.close()
        else:
            plt.show()
        
        # 计算基本统计信息
        stats = {
            '平均温度': f"{daily_temp.mean():.1f}°C",
            '最高温度': f"{daily_temp.max():.1f}°C",
            '最低温度': f"{daily_temp.min():.1f}°C",
            '温度标准差': f"{daily_temp.std():.1f}°C"
        }
        return stats
    
    def analyze_weather_types(self, save_path=None):
        """分析天气类型分布"""
        if self.data is None:
            return '请先加载数据'
        
        # 统计天气类型频率
        weather_counts = self.data['天气'].value_counts()
        
        # 绘制饼图
        plt.figure(figsize=(10, 8))
        plt.pie(weather_counts.values, labels=weather_counts.index, autopct='%1.1f%%')
        plt.title('天气类型分布')
        
        if save_path:
            plt.savefig(f'{save_path}_weather_types.png', bbox_inches='tight')
            plt.close()
        else:
            plt.show()
        
        return dict(weather_counts)
    
    def analyze_seasonal_patterns(self, save_path=None):
        """分析季节性模式"""
        if self.data is None:
            return '请先加载数据'
        
        # 添加季节信息
        self.data['季节'] = self.data['日期'].dt.month.map({
            12: '冬季', 1: '冬季', 2: '冬季',
            3: '春季', 4: '春季', 5: '春季',
            6: '夏季', 7: '夏季', 8: '夏季',
            9: '秋季', 10: '秋季', 11: '秋季'
        })
        
        # 计算每个季节的平均温度
        seasonal_temp = self.data.groupby('季节')['温度数值'].agg(['mean', 'std']).round(1)
        seasonal_temp.columns = ['平均温度', '标准差']
        
        # 绘制箱型图
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='季节', y='温度数值', data=self.data, order=['春季', '夏季', '秋季', '冬季'])
        plt.title('季节温度分布')
        plt.xlabel('季节')
        plt.ylabel('温度 (°C)')
        
        if save_path:
            plt.savefig(f'{save_path}_seasonal_patterns.png', bbox_inches='tight')
            plt.close()
        else:
            plt.show()
        
        return seasonal_temp.to_dict()

def main():
    # 创建分析实例
    analyzer = WeatherAnalysis()
    
    # 示例数据加载和分析
    print('天气数据分析工具')
    print('请确保数据文件格式正确（包含日期、温度、天气等列）')
    
    # 这里可以添加命令行参数解析，类似于weather_query.py
    # 现在仅作为示例展示基本功能
    
    # 假设我们有一个示例数据文件
    if analyzer.load_data('weather_data.csv'):
        print('\n1. 温度趋势分析')
        temp_stats = analyzer.analyze_temperature_trend(save_path='analysis_results')
        print('\n温度统计信息：')
        for key, value in temp_stats.items():
            print(f'{key}: {value}')
        
        print('\n2. 天气类型分析')
        weather_stats = analyzer.analyze_weather_types(save_path='analysis_results')
        print('\n天气类型统计：')
        for weather, count in weather_stats.items():
            print(f'{weather}: {count}次')
        
        print('\n3. 季节性分析')
        seasonal_stats = analyzer.analyze_seasonal_patterns(save_path='analysis_results')
        print('\n季节温度统计：')
        for season, stats in seasonal_stats.items():
            print(f'{season}:')
            for stat_name, value in stats.items():
                print(f'  {stat_name}: {value}°C')

if __name__ == '__main__':
    main()