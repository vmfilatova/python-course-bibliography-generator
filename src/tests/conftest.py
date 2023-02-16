"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, ArticleMagazineModel, \
    DissertationModel


@pytest.fixture
def book_model_fixture() -> BookModel:
    """
    Фикстура модели книги.

    :return: BookModel
    """

    return BookModel(
        authors="Иванов И.М., Петров С.Н.",
        title="Наука как искусство",
        edition="3-е",
        city="СПб.",
        publishing_house="Просвещение",
        year=2020,
        pages=999,
    )


@pytest.fixture
def internet_resource_model_fixture() -> InternetResourceModel:
    """
    Фикстура модели интернет-ресурса.

    :return: InternetResourceModel
    """

    return InternetResourceModel(
        article="Наука как искусство",
        website="Ведомости",
        link="https://www.vedomosti.ru",
        access_date="01.01.2021",
    )


@pytest.fixture
def articles_collection_model_fixture() -> ArticlesCollectionModel:
    """
    Фикстура модели сборника статей.

    :return: ArticlesCollectionModel
    """

    return ArticlesCollectionModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        collection_title="Сборник научных трудов",
        city="СПб.",
        publishing_house="АСТ",
        year=2020,
        pages="25-30",
    )


@pytest.fixture
def articles_magazine_model_fixture() -> ArticleMagazineModel:
    """
    Фикстура модели статьи для журнала.

    :return: ArticleMagazineModel
    """

    return ArticleMagazineModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        magazine_title="Сборник научных трудов",
        number=10,
        year=2020,
        pages="25-30",
    )


@pytest.fixture
def dissertation_model_fixture() -> DissertationModel:
    """
    Фикстура модели диссертации.

    :return: DissertationModel
    """

    return DissertationModel(
        authors="Иванов И.М.",
        title_dissertation="Наука как искусство",
        doc_or_cand="д-р. / канд.",
        branch_sciences="экон.",
        code="01.01.01",
        city="СПб.",
        year=2020,
        pages= 199,
    )
