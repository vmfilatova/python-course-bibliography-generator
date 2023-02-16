"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


class BookModel(BaseModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: Optional[str]
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(BaseModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date="01.01.2021",
        )
    """

    article: str
    website: str
    link: str
    access_date: str


class ArticlesCollectionModel(BaseModel):
    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str


class ArticleMagazineModel(BaseModel):
    """
    Модель статьи из журнала:

    .. code-block::

        ArticleMagazine(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            magazine_title="Образование и наука",
            year=2020,
            number = 10,
            pages="25-30",
        )
    """
    authors: str
    article_title: str
    magazine_title: str
    year: int = Field(..., gt=0)
    number: int = Field(..., gt=0)
    pages: str


class DissertationModel(BaseModel):
    """
    Модель диссертации:

    .. code-block::

        Dissertation(
            authors="Иванов И.М.",
            title_dissertation="Наука как искусство",
            doc_or_cand ="д-р. / канд.",
            branch_sciences="экон.",
            code = "01.01.01",
            city= "СПб.",
            year = 2020,
            pages = 199,
        )
    """
    authors: str
    title_dissertation: str
    doc_or_cand: str
    branch_sciences: str
    code: str
    city: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)
