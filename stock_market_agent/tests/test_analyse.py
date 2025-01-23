import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fetch_news import fetch_news  # 导入 fetch_news
from analyze_news import analyze_news




def main():
    # 假设我们要抓取苹果公司的新闻
    company_name = "Apple"
    
    # 抓取新闻
    news_data = fetch_news(company_name)
    
    # 分析新闻数据
    analyzed_data = analyze_news(news_data)
    
    # 打印分析结果
    for article in analyzed_data:
        print(f"Headline: {article['headline']}")
        print(f"Sentiment: {article['sentiment']}")
        print(f"Keywords: {article['keywords']}")
        print("------")

   
    
    
if __name__ == "__main__":
    main()
