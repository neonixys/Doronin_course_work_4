from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_genre_by_id(self, gid):
        """
            Получение жанра по id
        """
        return self.session.query(Genre).filter(Genre.id == gid).one()

    def get_all_genres(self):
        """
            Получение всех жанров
        """
        return self.session.query(Genre).all()

