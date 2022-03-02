from bs4 import BeautifulSoup
import pprint

pp = pprint.PrettyPrinter()


def ScrapNewsArticlesFromGoal(pageData):
    parsedData = BeautifulSoup(pageData.content, "html.parser")
    articles = parsedData.find_all('table', class_='widget-news-card')
    newsArticles = []
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
        newsArticle = {
            'id': id,
            'main_title': main_title,
            'sub_tile': sub_title,
            'link': link,
            'imgSrc': imgSrc,
            'postingTime': postingTime
        }
        newsArticles.append(newsArticle)
    return newsArticles
