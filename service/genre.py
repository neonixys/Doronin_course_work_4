from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_genre_by_id(self, gid):
        """
            Получение жанра по id
        """
        return self.dao.get_genre_by_id(gid)

    def get_all_genres(self):
        """
            Получение всех жанров
        """
        return self.dao.get_all_genres()

