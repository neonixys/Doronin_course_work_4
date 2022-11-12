from flask import request, abort
from flask_restx import Resource, Namespace
import jwt

from constants import JWT_SECRET, JWT_ALGORITHM
from dao.model.user import UserSchema
from decorators import auth_required
from implemented import user_service

user_ns = Namespace('user')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        user_data = request.headers["Authorization"]
        token = user_data.split("Bearer ")[-1]
        decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        email = decoded_data.get('email')

        if email:
            return user_schema.dump(user_service.get_user_by_email(email))
        abort(404)

    @auth_required
    def patch(self):
        data = request.json
        password = data.get("password")

        if password:
            return "Нет", 403


        user_data = request.headers["Authorization"]
        token = user_data.split("Bearer ")[-1]
        decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        email = decoded_data.get('email')
        data["email"] = email


        user = user_service.update_user(data)
        if not user:
            return abort(404)
        return user_schema.dump(user)


@user_ns.route('/password/')
class UsersView(Resource):
    @auth_required
    def put(self):
        data = request.json


        user_data = request.headers["Authorization"]
        token = user_data.split("Bearer ")[-1]
        decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        email = decoded_data.get('email')
        data["email"] = email

        user = user_service.update_user(data)
        if not user:
            return abort(404)
        return user_schema.dump(user)

#
# @user_ns.route("/")
# class UserViews(Resource):
#
#     @admin_required
#     def get(self, username):
#         user = user_service.get_user_by_username(username)
#         return user_schema.dump(user), 200
#
#     @admin_required
#     def delete(self, username):
#         """
#             Формирование представления для удалени пользователя по имени
#         """
#         try:
#             user_service.delete_user(username)
#             return 'Пользователь удален', 200
#         except Exception:
#             return 404
#
#
#     @auth_required
#     def put(self, username):
#         req_json = request.json
#         user_service.update_user(req_json, username)
#         return 'Пользователь обновлен', 201
#
#
# @user_ns.route("/")
# class UserViews(Resource):
#     @auth_required
#     def get(self):
#         users = user_service.get_all_users()
#         return users_schema.dump(users)

#     def post(self):
#         data = request.json
#         user_service.create_user(data)
#         return 'Пользователь добавлен', 201
