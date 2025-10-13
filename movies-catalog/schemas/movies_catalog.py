from pydantic import BaseModel


class MoviesCatalogBase(BaseModel):
    id: int
    title: str
    description: str
    year: int


class MoviesCatalog(MoviesCatalogBase):
    """
    Модель каталога фильмов
    """
