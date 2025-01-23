import unittest
from unittest.mock import patch
import requests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools import get_financial_data  # 使用绝对导入
 
class TestFinancialData(unittest.TestCase):

    # 模拟 API 返回数据
    @patch('requests.get')
    def test_get_financial_data_success(self, mock_get):
        # 模拟 API 返回的 JSON 数据
        mock_response = {
            "annualReports": [
                {
                    "fiscalDateEnding": "2023-09-30",
                    "netIncome": 93736000000,
                    "totalRevenue": 391035000000
                }
            ]
        }
        
        # 设置 mock 的返回值
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        # 调用函数并验证结果
        result = get_financial_data('AAPL', 'fake_api_key')
        
        # 验证返回值
        self.assertEqual(result['net_income'], 93736000000)
        self.assertEqual(result['expected_income'], 391035000000)
        self.assertEqual(result['fiscalDateEnding'], '2023-09-30')

    @patch('requests.get')
    def test_get_financial_data_no_reports(self, mock_get):
        # 模拟 API 返回没有财务数据的情况
        mock_response = {}
        
        # 设置 mock 的返回值
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        # 调用函数并验证返回值
        result = get_financial_data('AAPL', 'fake_api_key')
        
        # 验证结果
        self.assertEqual(result, {"error": "No financial data available"})

    @patch('requests.get')
    def test_get_financial_data_api_fail(self, mock_get):
        # 模拟 API 请求失败的情况
        mock_get.return_value.status_code = 500
        
        # 调用函数并验证返回值
        result = get_financial_data('AAPL', 'fake_api_key')
        
        # 验证结果
        self.assertEqual(result, {"error": "API request failed"})

if __name__ == '__main__':
    unittest.main()
