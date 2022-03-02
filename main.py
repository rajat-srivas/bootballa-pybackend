from typing import List
import fastapi
import requests
import uvicorn
import httpx
from goal_news_scrapper import ScrapNewsArticlesFromGoal
from models.news_article import NewsArticle


api = fastapi.FastAPI()


@api.get('/api/news')
async def ScrapGoalForBreakNews(pageNumber: int = 1, pageSize: int = 5) -> List[NewsArticle]:
    baseUrl = "https://www.goal.com/en-in/news/1"
    #pageData = requests.get(baseUrl   )
    pageData = ''
    async with httpx.AsyncClient() as client:
        pageData = await client.get(baseUrl)
    try:
        breakingNews = ScrapNewsArticlesFromGoal(pageData)
    except:
        return fastapi.Response(content='{"error" : "Snap!! something went wrong" }',
                                        status_code=400,
                                        media_type="application/json")
    return fastapi.responses.JSONResponse(content={"result": breakingNews[(pageNumber-1)*pageSize:pageNumber*pageSize]}, status_code=200)


uvicorn.run(api)
