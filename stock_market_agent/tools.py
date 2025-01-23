import yfinance as yf

def get_stock_data(ticker):
    """
    获取指定股票代码的实时股价及50日移动平均
    """
    stock = yf.Ticker(ticker)
    
    # 获取历史数据（例如：过去60天）
    history = stock.history(period="60d")
    
    # 获取当前股价
    current_price = history['Close'][-1]
    
    # 获取50日移动平均
    moving_average = history['Close'].rolling(window=50).mean().iloc[-1]
    
    return {
        'current_price': current_price,
        'moving_average': moving_average
    }



from alpha_vantage.fundamentaldata import FundamentalData

import requests

def get_financial_data(symbol, api_key):
    # 构建 API 请求 URL
    url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={api_key}"
    
    # 发送 GET 请求
    response = requests.get(url)
    
    # 确保请求成功
    if response.status_code == 200:
        data = response.json()
        
        # 从返回的 JSON 数据中提取净收入和预期收入
        # 注意，Avantage 返回的 "annualReports" 中包含每一年的财务数据
        if "annualReports" in data:
            annual_reports = data["annualReports"]
            latest_report = annual_reports[0]  # 最新的年度财报
            
            # 获取净收入和预期收入（这些字段的名称可能因公司不同而有所不同）
            net_income = latest_report.get('netIncome', 'N/A')  # 默认值为 'N/A'
            expected_income = latest_report.get('totalRevenue', 'N/A')  # 默认值为 'N/A'
            fiscalDateEnding = latest_report.get('fiscalDateEnding', 'N/A')
            return {
                'net_income': net_income,
                'expected_income': expected_income,
                'fiscalDateEnding':fiscalDateEnding
            }
        else:
            return {"error": "No financial data available"}
    else:
        return {"error": "API request failed"}

# 示例：获取 AAPL（苹果公司）的财报数据
api_key = "YFEVP8ROIGHX76UG"  # 替换为你的 API 密钥
symbol = "AAPL"  # 苹果公司的股票代码
financial_data = get_financial_data(symbol, api_key)

# 打印结果
print(f"Net Income: {financial_data['net_income']}")
print(f"Expected Income: {financial_data['expected_income']}")
print(f"year : {financial_data['fiscalDateEnding']}")


import requests

def get_exchange_rate(base_currency="USD", target_currency="EUR"):
    """
    获取 USD 到 EUR 的汇率
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    # 获取目标货币汇率
    return data['rates'].get(target_currency, 1)

def convert_to_euro(amount, base_currency="USD"):
    """
    将金额从 base_currency 转换为欧元
    """
    exchange_rate = get_exchange_rate(base_currency)
    return amount * exchange_rate

# 示例：将股价从 USD 转换为 EUR

ticker = "AAPL"
a=get_stock_data("AAPL")


# 获取 'current_price' 和 'moving_average' 的浮动值
current_price = a['current_price']




stock_price_in_eur = convert_to_euro(current_price)
print(f"Stock price in EUR: {stock_price_in_eur:.2f}")


# company_earnings_report = get_company_earnings("AAPL", "YFEVP8ROIGHX76UG")
# income = company_earnings_report['net_income']
# expectcome = company_earnings_report['expected_income']

# print("the income of the ", ticker, income)
