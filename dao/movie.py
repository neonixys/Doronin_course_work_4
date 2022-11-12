from dao.model.movie import Movie


class MovieDAO:
    """
        Класс работает с bd и получает CRUD
    """

    def __init__(self, session):
        self.session = session

    def get_movie_by_id(self, mid):
        """
            Получение фильма по id
        """
        return self.session.query(Movie).filter(Movie.id == mid).one_or_none()

    def get_all_movies(self, sort: bool = False, page=False):
        """
        This method give us a list of movies depend on a requested parameters
        :param sort: if need sort movie by year set True
        :param page: if need paginate, set page True
        :return: movies sorted by parameters
        """
        if page and sort:
            movies = self.session.query(Movie).order_by(Movie.year.desc()).paginate(page=int(page), per_page=12).items
        elif sort:
            movies = self.session.query(Movie).order_by(Movie.year.desc()).all()
        elif page:
            movies = self.session.query(Movie).paginate(page=int(page), per_page=12).items
        else:
            movies = self.session.query(Movie).all()
        return movies

        # def get_movies(self):
    #     return self.session.query(Movie)
    #
    # def get_all_movies(self, query):
    #     return query.all()
    #
    # def get_new(self, query):
    #     return query.order_by(Movie.year.desc())
    #
    # def get_pages(self, query, limit, offset):
    #     return query.limit(limit).offset(offset)
