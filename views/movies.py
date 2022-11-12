from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from decorators import auth_required
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")

        filters = {
            "status": status,
            "page": page,
        }
        all_movies = movie_service.get_all_movies(filters)
        result = movies_schema.dump(all_movies)
        return result, 200




@movie_ns.route('/<int:pk>')
class MovieView(Resource):
    @auth_required
    def get(self, pk: int):
        try:
            movie = movie_service.get_movie_by_id(pk)
            result = movie_schema.dump(movie)
            return result, 200
        except Exception as e:
            return e



# @movie_ns.route("/")
# class MovieViews(Resource):
#     @auth_required
#     def get(self):
#         status = request.args.get("status")
#         page = request.args.get("page")
#
#         filters = {
#             "status": status,
#             "page": page,
#         }
#         all_movies = movie_service.get_all_movies(filters)
#         result = movies_schema.dump(all_movies)
#         return result, 200
#
#
# @movie_ns.route("/<int:mid>")
# class MovieView(Resource):
#     @auth_required
#     def get(self, mid: int):
#         """
#             Формирование представления для получения фильма по id
#         """
#         try:
#             movie = movie_service.get_movie_by_id(mid)
#             return movie_schema.dump(movie), 200
#         except Exception:
#             return 'Такого фильма нет'
