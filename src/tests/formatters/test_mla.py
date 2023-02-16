"""
Тестирование функций оформления списка источников по MLA.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import BookModel, ArticleMagazineModel
from formatters.styles.mla import MLABook, MLAArticleMagazine


class TestMLA:
    """
    Тестирование оформления списка источников согласно MLA.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = MLABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство. Просвещение, 2020."
        )

    def test_articles_magazine(
            self, articles_magazine_model_fixture: ArticleMagazineModel
    ) -> None:
        """
        Тестирование форматирования статьи из журнала.

        :param ArticleMagazineModel articles_magazine_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        model = MLAArticleMagazine(articles_magazine_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. \"Наука как искусство.\" Сборник научных трудов, no. 10, 2020, pp. 25-30."
        )

    def test_citation_formatter(
            self,
            book_model_fixture: BookModel,
            articles_magazine_model_fixture: ArticleMagazineModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param ArticleMagazineModel articles_magazine_model_fixture: Фикстура модели статьи из журнала
       :return:
        """

        models = [
            MLABook(book_model_fixture),
            MLAArticleMagazine(articles_magazine_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[1]
        assert result[1] == models[0]
