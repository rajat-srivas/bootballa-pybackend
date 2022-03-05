from statistics import mode
from typing import List
from bs4 import BeautifulSoup
import pprint
from app.models.news_article import NewsArticle

pp = pprint.PrettyPrinter()


def ScrapNewsArticlesFromGoal(pageData) -> List[NewsArticle]:
    parsedData = BeautifulSoup(pageData.content, "html.parser")
    articles = parsedData.find_all('table', class_='widget-news-card')
    newsList = []
    id = 0
    for news in articles:
        id = id+1
        main_title = ''
        sub_title = ''
        link = ''
        postingTime = ''
        imgSrc = ''
        contentTag = news.find_all('td', class_='widget-news-card__content')
        for contentBody in contentTag:
            titleTag = contentBody.find_all(
                'h3', class_='widget-news-card__title')
            sub_title = titleTag[0]['title']
            linkTag = contentBody.find_all('a')
            link = 'http://www.goal.com/' + linkTag[0]['href']
            main_title = linkTag[0].get_text()
            timeTag = contentBody.find_all('div')
            postingTime = timeTag[0].get_text()
        imageTag = news.find_all('td', class_='widget-news-card__image')
        for imageBody in imageTag:
            imgTag = imageBody.find_all('img')
            imgSrc = imgTag[0]['src']
        newsItem = {
            'id': id,
            'main_title': main_title.strip(),
            'sub_title': sub_title.strip(),
            'link': link.strip(),
            'imgSrc': imgSrc.strip(),
            'postingTime': postingTime.strip()
        }
        model = NewsArticle(**newsItem)
        newsList.append(model.dict())
    return newsList
