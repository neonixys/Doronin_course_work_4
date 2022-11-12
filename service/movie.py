from flask import current_app

from dao.model.movie import MovieSchema
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_movie_by_id(self, mid):
        """
            Получение фильма по id
        """
        return self.dao.get_movie_by_id(mid)

    def get_all_movies(self, filters):
        sort, page = False, False
        # Check if it needed to sort list
        if filters.get("status") is not None:
            sort = True
        # Check if it needed to paginate
        if filters.get("page") is not None:
            page = filters.get("page")
        movies = self.dao.get_all_movies(sort, page)

        return movies

    # def get_all_movies(self, data):
    #     """
    #         Получение всех фильмов
    #     """
    #     movies_query = self.dao.get_movies()
    #
    #     status = data.get('status')
    #     page = data.get('page')
    #
    #     if status and status == 'new':
    #         movies_query = self.dao.get_new(movies_query)
    #
    #     if page:
    #         limit = current_app.config['ITEMS_PER_PAGE']
    #         offset = (page - 1) * limit
    #         movies_query = self.dao.get_pages(movies_query, limit, offset)
    #
    #     movies = self.dao.get_all_movies(movies_query)
    #
    #     return movies



