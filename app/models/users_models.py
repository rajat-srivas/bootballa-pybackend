from pydantic import BaseModel


class Users_Favorites(BaseModel):
    id: int
    favorite_team: str
    favorite_league: str
    favorite_player: str

    class Config:
        orm_mode = True


class BootBalla_Users(BaseModel):
    id: int
    email: str
    name: str
    hashed_password: str
    profile_photp: str
    favorites_id: int

    class Config:
        orm_mode = True
