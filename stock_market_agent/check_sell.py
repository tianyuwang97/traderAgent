from fetch_news import fetch_news
from analyze_news import analyze_news

def make_stock_decision(news_data, company_stock_price, company_earnings_report):
    """
    综合新闻数据、情感分析和公司基本面数据来做出股票操作决策
    """

    # 计算新闻情感得分的加权平均值
    sentiment_score = sum([article['sentiment'] for article in news_data]) / len(news_data)
    
    # 根据情感得分判断基本操作方向
    if sentiment_score > 0.5:
        sentiment_decision = "buy"
    elif sentiment_score < -0.5:
        sentiment_decision = "sell"
    else:
        sentiment_decision = "hold"
    
    # 基于公司财报的基本操作判断
    if company_earnings_report['net_income'] > company_earnings_report['expected_income']:
        earnings_decision = "buy"
    else:
        earnings_decision = "sell"
    
    # 基于股价相对于历史均值的判断（股价低于均值买入，高于均值卖出）
    if company_stock_price['current_price'] < company_stock_price['moving_average']:
        price_decision = "buy"
    else:
        price_decision = "sell"
    
    # 综合情感、财报和股价决策
    if sentiment_decision == "buy" and earnings_decision == "buy" and price_decision == "buy":
        final_decision = "buy"
    elif sentiment_decision == "sell" or earnings_decision == "sell" or price_decision == "sell":
        final_decision = "sell"
    else:
        final_decision = "hold"
    
    return final_decision

def main():
    # 1. 假设我们要分析苹果公司的股票
    company_name = "Apple"

    # 2. 抓取苹果公司的新闻数据
    news_data = fetch_news(company_name)

    # 3. 对抓取的新闻数据进行情感分析
    analyzed_data = analyze_news(news_data)

    # 4. 获取公司股票的当前价格（示例数据）
    company_stock_price = {
        'current_price': 145.32,  # 当前股价
        'moving_average': 140.00  # 50日移动平均股价
    }

    # 5. 获取公司财报数据（示例数据）
    company_earnings_report = {
        'net_income': 5000000000,  # 净收入
        'expected_income': 4500000000  # 预期收入
    }

    # 6. 根据新闻情感、财报和股价做出股票操作决策
    decision = make_stock_decision(analyzed_data, company_stock_price, company_earnings_report)

    # 7. 输出决策结果
    print(f"Based on the news, earnings, and stock price data, the decision is to: {decision}")

if __name__ == "__main__":
    main()
