
#第一步：数据预处理

def clean_news_data(news_data):
    cleaned_data = []
    for article in news_data:
        cleaned_article = {
            'headline': article.get('headline', '').strip(),
            'url': article.get('url', ''),
            'publishedAt': article.get('publishedAt', ''),
            'company': article.get('company', '').strip(),
        }
        cleaned_data.append(cleaned_article)
    return cleaned_data

#第二步：情感分析
#2.1 使用现有的情感分析工具（如 TextBlob 或 VADER）
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    # 获取情感的极性（polarity）：-1 表示消极，1 表示积极
    sentiment_score = analysis.sentiment.polarity
    return sentiment_score

#2.2 对新闻标题进行情感分析

def analyze_news_sentiment(news_data):
    for article in news_data:
        headline = article['headline']
        sentiment_score = analyze_sentiment(headline)
        article['sentiment'] = sentiment_score
    return news_data

#第三步：关键词提取
#3.1 使用 spaCy 进行关键词提取
import spacy

# 加载 spaCy 模型
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    keywords = []
    for ent in doc.ents:
        keywords.append(ent.text)
    return keywords

#3.2 提取公司相关的关键词
def extract_news_keywords(news_data):
    for article in news_data:
        headline = article['headline']
        article['keywords'] = extract_keywords(headline)
    return news_data


#第四步：整合分析模块

def analyze_news(news_data):
    # 清理新闻数据
    cleaned_news = clean_news_data(news_data)
    
    # 情感分析
    sentiment_news = analyze_news_sentiment(cleaned_news)
    
    # 提取关键词
    final_news = extract_news_keywords(sentiment_news)
    
    return final_news
