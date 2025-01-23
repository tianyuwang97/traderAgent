import os
import datetime
import csv


# from fetch_news import fetch_news
# from analyze_news import analyze_news
# from record_trade import record_trade
# from check_sell import check_sell


# 抓取新闻数据
def fetch_news():
    print("Fetching news data...")
    return [{"company": "Apple", "headline": "Apple launches new iPhone", "sentiment": "positive"}]

# 分析新闻数据
def analyze_news(news):
    print("Analyzing news data...")
    analysis_results = []
    for item in news:
        result = {
            "company": item["company"],
            "action": "buy" if item["sentiment"] == "positive" else "sell",
            "reason": item["headline"]
        }
        analysis_results.append(result)
    return analysis_results

# 记录买入操作
def record_trade(trade):
    print(f"Recording trade: {trade}")
    if not os.path.exists("trades.csv"):
        with open("trades.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "company", "action", "price", "reason"])
    
    with open("trades.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            trade["date"], trade["company"], trade["action"], trade["price"], trade["reason"]
        ])

# 检查是否需要卖出
def check_sell():
    print("Checking for sell opportunities...")
    today = datetime.date.today()

    if not os.path.exists("trades.csv"):
        print("No trades to check.")
        return

    trades_to_keep = []
    with open("trades.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            trade_date = datetime.datetime.strptime(row["date"], "%Y-%m-%d").date()
            days_held = (today - trade_date).days

            if row["action"] == "buy" and days_held >= 30:
                print(f"Sell {row['company']} - held for {days_held} days")
            else:
                trades_to_keep.append(row)

    with open("trades.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "company", "action", "price", "reason"])
        writer.writeheader()
        writer.writerows(trades_to_keep)

# 主程序入口
if __name__ == "__main__":
    print("Starting Stock Market Agent...")
    news_data = fetch_news()
    analysis_results = analyze_news(news_data)

    for result in analysis_results:
        if result["action"] == "buy":
            trade = {
                "date": datetime.date.today().strftime("%Y-%m-%d"),
                "company": result["company"],
                "action": "buy",
                "price": 100.0,
                "reason": result["reason"]
            }
            record_trade(trade)

    check_sell()
