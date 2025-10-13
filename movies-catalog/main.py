from typing import Annotated

from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    status,
)
from fastapi.params import Depends

from schemas.movies_catalog import MoviesCatalog

app = FastAPI(
    title="Movies Catalog",
)


@app.get("/")
def read_root(
    request: Request,
    name="World",
):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )

    return {
        "message": f"Hello {name}!",
        "docs:": str(docs_url),
    }


def prepare_catalog(
    movie_id: int,
) -> MoviesCatalog:
    movie: MoviesCatalog | None = next(
        (movie for movie in MOVIES_CATALOG if movie.id == movie_id),
        None,
    )
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Movie not found",
    )


MOVIES_CATALOG = [
    MoviesCatalog(
        id=1,
        title="Никто",
        description="Непримечательный и незаметный семьянин Хатч живёт скучной жизнью обычного аудитора, пока однажды в его дом не вламываются грабители. И это бы сошло им с рук, если бы они не забрали браслетик его маленькой дочки. Не в силах это терпеть, Хатч отправляется на поиски наглецов, а на обратном пути ввязывается в драку с пьяными хулиганами, пристававшими к девушке в общественном транспорте. От души помахав кулаками, наш аудитор отправляет дебоширов в больницу, но оказывается, что один из пострадавших — брат влиятельного русского бандита. И он теперь жаждет мести.",
        year=2021,
    ),
    MoviesCatalog(
        id=2,
        title="Атель-Матель",
        description="Саша Родионов, пронырливый обнальщик из Москвы, задолжал денег опасному авторитету по кличке Пчеловод. Он не прощает задержек и жестоко расправляется с должниками, поэтому Саша вместе с семьей бежит в Дагестан по программе защиты свидетелей. Вот только жена и дети уверены, что это обычный отпуск, и теперь Саша вынужден выдать ветхий сарай в горном ауле за модный эко-отель. Однако популярность отеля выдает местоположение Родионова его недоброжелателям.",
        year=2025,
    ),
    MoviesCatalog(
        id=3,
        title="Миссия невыполнима: Финальная расплата",
        description="Искусственный интеллект Entity готовится уничтожить человечество, постепенно перехватывая контроль над ядерными арсеналами мировых держав. У Итана Ханта и его команды есть лишь 72 часа, чтобы найти устройство с исходным кодом Entity, которое находится на затонувшей российской подводной лодке «Севастополь», и предотвратить глобальную катастрофу.",
        year=2025,
    ),
    MoviesCatalog(
        id=4,
        title="Василий",
        description="Вася — скромный учитель ОБЖ из поселка Ковылкино. Звезд с неба не хватает, живет простой и размеренной жизнью. Зато его брат-близнец Коля, с которым они не виделись с детства, умудрился кинуть мексиканский наркокартель на деньги, и за это его ждет расплата! Василий впервые отправляется навестить брата в Мексику, не предполагая, что теперь ему предстоит применить все знания в ОБЖ на практике, спасаясь то от местных бандитов, то от ревнивой мексиканской красавицы Бониты. Таким похожим и таким разным близнецам предстоит снова узнать друг друга, найти свою любовь и свою семью.",
        year=2025,
    ),
]


@app.get(
    "/catalog",
    response_model=list[MoviesCatalog],
)
def get_catalog():
    return MOVIES_CATALOG


@app.get(
    "/catalog/{movie_id}",
    response_model=MoviesCatalog,
)
def get_movie_details(
    movie: Annotated[
        MoviesCatalog,
        Depends(prepare_catalog),
    ],
) -> MoviesCatalog:
    return movie
