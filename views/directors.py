# Импорт необходимых библиотек
from flask import request
from flask_restx import Resource, Namespace

# Импорт схемы Director
from dao.model.director import DirectorSchema
# Импорт экземпляра класса DirectorService
from implemented import director_service

# Импорт декораторов

# Формирование нэймспейса
director_ns = Namespace('directors')

# Формирование сереилизаторов для модели Director для одного элемента и для списка
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """
            Формирование представления для получения режиссеров
        """
        try:
            directors = director_service.get_all_directors()
            return directors_schema.dump(directors), 200
        except Exception:
            return 404


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did: int):
        """
            Формирование представления для получения режиссера по id
        """
        try:
            director = director_service.get_director_by_id(did)
            return director_schema.dump(director), 200
        except Exception:
            return 'Такого режиссера нет'
