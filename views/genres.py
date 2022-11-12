from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
# Формирование сереилизаторов для модели Genres для одного элемента и для спи
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenreViews(Resource):
    def get(self):
        """
            Формирование представления для получения жанров
        """
        query = genre_service.get_all_genres()
        return genres_schema.dump(query)


@genre_ns.route("/<int:gid>")
class GenreViews(Resource):
    # @auth_required
    def get(self, gid: int):
        """
            Формирование представления для получения жанра по id
        """
        try:
            genre = genre_service.get_genre_by_id(gid)
            return genre_schema.dump(genre), 200
        except Exception:
            return 'Таких жанров нет'

