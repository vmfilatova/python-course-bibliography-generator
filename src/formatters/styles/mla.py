"""
Стиль цитирования по MLA.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import BookModel, ArticleMagazineModel
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)


class MLABook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $title. $publishing_house, $year."
        )

    def substitute(self) -> str:
        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
            edition=self.get_edition(),
        )

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """

        return f"{self.data.edition} изд. – " if self.data.edition else ""


class MLAArticleMagazine(BaseCitationStyle):
    """
    Форматирование для статьи из журнала.
    """

    data: ArticleMagazineModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors \"$article_title.\" $magazine_title, no. $number, $year, pp. $pages."
        )

    def substitute(self) -> str:
        logger.info('Форматирование статьи из журнала "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            magazine_title=self.data.magazine_title,
            year=self.data.year,
            number=self.data.number,
            pages=self.data.pages,
        )


class MLACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: MLABook,
        ArticleMagazineModel.__name__: MLAArticleMagazine,
    }

    def __init__(self, models: list[BaseModel]) -> None:
        """
        Конструктор.

        :param models: Список объектов для форматирования
        """

        formatted_items = []
        for model in models:
            formatted_items.append(self.formatters_map.get(type(model).__name__)(model))  # type: ignore

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.

        :return:
        """

        return sorted(self.formatted_items, key=lambda item: item.formatted)
