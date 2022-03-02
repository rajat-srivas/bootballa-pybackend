from pydantic import BaseModel


class NewsArticle(BaseModel):
    id: int
    main_title: str
    sub_title: str
    link: str
    postingTime: str
    imgSrc: str
