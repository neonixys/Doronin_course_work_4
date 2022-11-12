from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_director_by_id(self, did):
        """
            Получение режиссера по id
        """
        return self.dao.get_director_by_id(did)

    def get_all_directors(self):
        """
            Получение всех режиссеров
        """
        return self.dao.get_all_directors()
