import requests
import json



def get_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=217d3fcc142d44a892d1141b07c0d2b0'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'
