from typing import List
from app.business.goal_news_scrapper import ScrapNewsArticlesFromGoal
from app.models.news_article import NewsArticle
import fastapi
import httpx

router = fastapi.APIRouter()


@router.get('/news')
async def ScrapGoalForBreakNews(pageNumber: int = 1, pageSize: int = 5) -> List[NewsArticle]:
    baseUrl = "https://www.goal.com/en-in/news/1"
    pageData = ''
    async with httpx.AsyncClient() as client:
        pageData = await client.get(baseUrl)
    try:
        breakingNews = ScrapNewsArticlesFromGoal(pageData)
    except Exception as ex:
        return fastapi.Response(content='{"error" : "Snap!! something went wrong" }',
                                        status_code=400,
                                media_type="application/json")
    return fastapi.responses.JSONResponse(content={"result": breakingNews[(pageNumber-1)*pageSize:pageNumber*pageSize]}, status_code=200)
