#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
网页爬虫项目

这个项目实现了一个简单的网页爬虫，用于抓取新闻网站的数据，
并对数据进行分析和可视化展示。
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os

class NewsCrawler:
    def __init__(self, base_url, max_pages=5, retry_times=3):
        self.base_url = base_url
        self.max_pages = max_pages
        self.retry_times = retry_times
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive'
        }
        self.news_data = []

    def fetch_page(self, url, retry_count=0):
        """获取页面内容，带重试机制"""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            if retry_count < self.retry_times:
                print(f"获取页面失败，正在进行第{retry_count + 1}次重试...")
                return self.fetch_page(url, retry_count + 1)
            print(f"获取页面失败: {e}")
            return None

    def fetch_news_detail(self, url):
        """获取新闻详细内容"""
        html = self.fetch_page(url)
        if not html:
            return None

        try:
            soup = BeautifulSoup(html, 'html.parser')
            # 适配新浪新闻的文章内容结构
            content = soup.select_one('#article') or soup.select_one('.article')
            if content:
                return {
                    'content': content.get_text(strip=True),
                    'publish_time': self._extract_publish_time(soup),
                    'author': self._extract_author(soup)
                }
        except Exception as e:
            print(f"解析新闻详情失败: {e}")
        return None

    def _extract_publish_time(self, soup):
        """提取发布时间"""
        time_element = soup.select_one('.date') or soup.select_one('.time-source')
        return time_element.text.strip() if time_element else None

    def _extract_author(self, soup):
        """提取作者信息"""
        author_element = soup.select_one('.show_author') or soup.select_one('.source')
        return author_element.text.strip() if author_element else None

    def crawl_multiple_pages(self):
        """爬取多个页面的新闻"""
        print("\n正在爬取新浪新闻首页...")
        html = self.fetch_page(self.base_url)
        if html:
            self.parse_news(html)
        else:
            print("新闻页面爬取失败")

    def parse_news(self, html):
        """解析新闻内容"""
        if not html:
            return
        
        soup = BeautifulSoup(html, 'html.parser')
        # 适配新浪新闻的HTML结构
        news_items = soup.select('.news-item') or soup.select('.main-news h2') or soup.select('.ct_t_01 a') or soup.select('.news-2 a')
        
        if not news_items:
            print("未找到新闻列表，可能是页面结构已变更")
            return
        
        for item in news_items:
            try:
                title_link = item.select_one('a')
                if not title_link:
                    continue
                    
                news = {
                    'title': title_link.text.strip(),
                    'date': datetime.now().strftime('%Y-%m-%d'),
                    'category': '新浪新闻',
                    'url': title_link.get('href', '')
                }
                
                if news['title'] and news['url'] and news['url'].startswith('http'):
                    # 获取新闻详情
                    detail = self.fetch_news_detail(news['url'])
                    if detail:
                        news.update(detail)
                    self.news_data.append(news)
            except (AttributeError, KeyError) as e:
                print(f"解析新闻项失败: {e}")
    
    def save_data(self, filename='news_data.json'):
        """保存数据到文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.news_data, f, ensure_ascii=False, indent=2)
    
    def analyze_data(self):
        """分析数据"""
        if not self.news_data:
            print("没有获取到新闻数据，无法进行分析")
            return

        df = pd.DataFrame(self.news_data)
        if df.empty:
            print("数据框为空，无法进行分析")
            return

        print(f"\n共获取到 {len(df)} 条新闻")
        
        # 统计基本信息
        print("\n新闻数据统计：")
        if 'publish_time' in df.columns:
            print(f"发布时间范围：{df['publish_time'].min()} 至 {df['publish_time'].max()}")
        if 'author' in df.columns:
            print("\n作者统计：")
            print(df['author'].value_counts().head())

        # 新闻标题词频分析
        print("\n热门词汇统计：")
        all_titles = ' '.join(df['title'])
        words = all_titles.split()
        word_freq = pd.Series(words).value_counts().head(10)
        print(word_freq)

        # 绘制多个图表
        plt.figure(figsize=(15, 10))

        # 1. 新闻类别分布
        plt.subplot(2, 2, 1)
        if 'category' in df.columns:
            df['category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
            plt.title('新闻类别分布')

        # 2. 作者发文数量
        plt.subplot(2, 2, 2)
        if 'author' in df.columns:
            df['author'].value_counts().head(5).plot(kind='bar')
            plt.title('TOP5作者发文数量')
            plt.xticks(rotation=45)

        # 3. 热门词汇统计
        plt.subplot(2, 2, 3)
        word_freq.plot(kind='barh')
        plt.title('热门词汇TOP10')

        # 4. 发布时间分布
        plt.subplot(2, 2, 4)
        if 'publish_time' in df.columns:
            df['publish_time'].value_counts().sort_index().plot(kind='line')
            plt.title('新闻发布时间分布')
            plt.xticks(rotation=45)

        plt.tight_layout()
        plt.savefig('news_analysis_detailed.png')
        print("\n详细分析图表已保存为 'news_analysis_detailed.png'")

        print("\n新闻标题列表：")
        for title in df['title']:
            print(f"- {title}")

        # 按类别统计新闻数量
        if 'category' in df.columns:
            category_counts = df['category'].value_counts()
            print("\n新闻类别统计：")
            print(category_counts)

            # 绘制柱状图
            plt.figure(figsize=(10, 6))
            category_counts.plot(kind='bar')
            plt.title('新闻类别分布')
            plt.xlabel('类别')
            plt.ylabel('数量')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('news_analysis.png')
            print("\n分析图表已保存为 'news_analysis.png'")
        else:
            print("\n未找到类别数据，跳过类别分析")

def main():
    # 使用新浪新闻首页
    crawler = NewsCrawler('https://news.sina.com.cn/', max_pages=1)
    crawler.crawl_multiple_pages()
    crawler.save_data()
    crawler.analyze_data()

if __name__ == '__main__':
    main()