import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fetch_news import fetch_news  # 导入 fetch_news





class TestFetchNews(unittest.TestCase):

    def test_fetch_news(self):
        # 设置测试数据，假设查询的是苹果公司
        company_name = "Apple"
        
        # 调用 fetch_news 函数
        news_data = fetch_news(company_name)
        
        # 打印抓取到的新闻
        print(f"抓取到的新闻: {news_data}")
        
        # 检查返回的新闻数据是否是一个列表
        self.assertIsInstance(news_data, list)
        
        # 检查是否至少返回了一条新闻
        self.assertGreater(len(news_data), 0)
        
        # 检查新闻数据的字段是否包含必要的信息（如标题和 URL）
        for item in news_data:
            self.assertIn("headline", item)
            self.assertIn("url", item)
            self.assertIn("publishedAt", item)
            self.assertIn("company", item)

if __name__ == "__main__":
    unittest.main()
