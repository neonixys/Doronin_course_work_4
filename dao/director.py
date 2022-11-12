from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session
        
    def get_director_by_id(self, did):
        """
            Получение режиссера по id
        """
        return self.session.query(Director).filter(Director.id == did).one()

    def get_all_directors(self):
        """
            Получение всех режиссеров
        """
        return self.session.query(Director).all()

