import requests
import json
import argparse
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

class WeatherQuery:
    def __init__(self):
        # 使用 OpenWeatherMap API，需要注册获取 API key
        self.api_key = "YOUR_API_KEY"  # 请替换为你的 API key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
    
    def get_weather(self, city):
        try:
            # 构建请求参数
            params = {
                'q': city,
                'appid': self.api_key,
                'lang': 'zh_cn',  # 返回中文结果
                'units': 'metric'  # 使用摄氏度
            }
            
            # 发送 GET 请求
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # 检查请求是否成功
            
            # 解析返回的 JSON 数据
            weather_data = response.json()
            
            # 提取需要的信息
            result = {
                '城市': weather_data['name'],
                '天气': weather_data['weather'][0]['description'],
                '温度': f"{weather_data['main']['temp']}°C",
                '体感温度': f"{weather_data['main']['feels_like']}°C",
                '湿度': f"{weather_data['main']['humidity']}%",
                '风速': f"{weather_data['wind']['speed']}m/s",
                '更新时间': datetime.fromtimestamp(weather_data['dt']).strftime('%Y-%m-%d %H:%M:%S')
            }
            
            return result
        
        except requests.exceptions.RequestException as e:
            return {'error': f'获取天气信息失败: {str(e)}'}
        except (KeyError, json.JSONDecodeError) as e:
            return {'error': f'解析天气数据失败: {str(e)}'}

    def get_forecast(self, city, days=5):
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'lang': 'zh_cn',
                'units': 'metric'
            }
            
            response = requests.get(self.forecast_url, params=params)
            response.raise_for_status()
            
            forecast_data = response.json()
            forecasts = []
            
            for item in forecast_data['list'][:days*8:8]:  # 每天8个数据点，取每天的第一个
                forecast = {
                    '日期': datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d'),
                    '天气': item['weather'][0]['description'],
                    '温度': f"{item['main']['temp']}°C",
                    '湿度': f"{item['main']['humidity']}%",
                    '风速': f"{item['wind']['speed']}m/s"
                }
                forecasts.append(forecast)
            
            return forecasts
        except requests.exceptions.RequestException as e:
            return {'error': f'获取天气预报失败: {str(e)}'}
        except (KeyError, json.JSONDecodeError) as e:
            return {'error': f'解析天气预报数据失败: {str(e)}'}
    
    def compare_cities(self, cities):
        results = []
        for city in cities:
            result = self.get_weather(city)
            if 'error' not in result:
                results.append(result)
        
        if results:
            df = pd.DataFrame(results)
            return df
        return None

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='天气查询工具')
    parser.add_argument('cities', nargs='+', help='要查询天气的城市名称（可多个）')
    parser.add_argument('--forecast', action='store_true', help='显示天气预报')
    parser.add_argument('--compare', action='store_true', help='比较多个城市的天气')
    parser.add_argument('--save', help='保存结果到文件')
    args = parser.parse_args()
    
    weather = WeatherQuery()
    
    if args.compare and len(args.cities) > 1:
        # 比较多个城市的天气
        df = weather.compare_cities(args.cities)
        if df is not None:
            print('\n城市天气对比:')
            print(tabulate(df, headers='keys', tablefmt='pretty'))
            
            # 绘制温度对比图
            plt.figure(figsize=(10, 6))
            plt.bar(df['城市'], df['温度'].str.rstrip('°C').astype(float))
            plt.title('城市温度对比')
            plt.xlabel('城市')
            plt.ylabel('温度 (°C)')
            plt.xticks(rotation=45)
            
            if args.save:
                plt.savefig(f'{args.save}_temperature_comparison.png')
                df.to_csv(f'{args.save}_weather_comparison.csv')
                print(f'\n结果已保存到 {args.save}_temperature_comparison.png 和 {args.save}_weather_comparison.csv')
            
            plt.close()
    
    elif args.forecast:
        # 显示天气预报
        for city in args.cities:
            forecasts = weather.get_forecast(city)
            if isinstance(forecasts, list):
                print(f'\n{city}未来5天天气预报:')
                df = pd.DataFrame(forecasts)
                print(tabulate(df, headers='keys', tablefmt='pretty'))
                
                if args.save:
                    df.to_csv(f'{args.save}_{city}_forecast.csv')
                    print(f'预报已保存到 {args.save}_{city}_forecast.csv')
            else:
                print(forecasts['error'])
    
    else:
        # 显示单个城市的当前天气
        for city in args.cities:
            result = weather.get_weather(city)
            if 'error' in result:
                print(result['error'])
            else:
                print(f'\n{city}天气查询结果:')
                for key, value in result.items():
                    print(f'{key}: {value}')
                
                if args.save:
                    with open(f'{args.save}_{city}_weather.json', 'w', encoding='utf-8') as f:
                        json.dump(result, f, ensure_ascii=False, indent=4)
                    print(f'结果已保存到 {args.save}_{city}_weather.json')

if __name__ == '__main__':
    main()