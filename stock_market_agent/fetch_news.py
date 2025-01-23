import requests
import datetime

# NewsAPI 的免费 API 密钥（你需要先注册并获取）
API_KEY = "f66c4d70f9274083bf7d3fe7f9dea234"
BASE_URL = "https://newsapi.org/v2/everything"

# 获取指定公司名称的新闻数据
def fetch_news(company_name):
    # 构建查询参数
    params = {
        'q': company_name,  # 公司名或关键词
        'apiKey': API_KEY,  # API 密钥
        'language': 'en',    # 英文新闻
        'sortBy': 'publishedAt',  # 按发布日期排序
        'pageSize': 50,      # 每次请求返回最多5条新闻
    }

    # 发起 GET 请求
    response = requests.get(BASE_URL, params=params)
    
    # 处理请求错误
    if response.status_code != 200:
        print(f"Error fetching news: {response.status_code}")
        return []

    # 获取新闻数据
    data = response.json()
    
    # 解析新闻内容
    articles = data.get("articles", [])
    news = []

    for article in articles:
        news_item = {
            "company": company_name,
            "headline": article["title"],
            "description": article["description"],
            "url": article["url"],
            "publishedAt": article["publishedAt"],
            "sentiment": analyze_sentiment(article["title"])  # 你可以在这里加入情感分析功能
        }
        news.append(news_item)

    return news

# 模拟情感分析（这里只是一个简单的示例，可以用更复杂的情感分析模型替代）
def analyze_sentiment(title):
    positive_keywords = ["positive", "good", "strong", "rise", "growth"]
    negative_keywords = ["negative", "bad", "fall", "decline", "loss"]

    if any(keyword in title.lower() for keyword in positive_keywords):
        return "positive"
    elif any(keyword in title.lower() for keyword in negative_keywords):
        return "negative"
    else:
        return "neutral"

# 测试函数
if __name__ == "__main__":
    company_name = "NVDA"
    news_data = fetch_news(company_name)
    for item in news_data:
        print(f"Headline: {item['headline']}")
        print(f"Sentiment: {item['sentiment']}")
        print(f"URL: {item['url']}")
        print(f"Published At: {item['publishedAt']}")
        print("="*50)
