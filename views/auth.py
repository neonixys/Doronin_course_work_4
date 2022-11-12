from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthViews(Resource):
    # Register new user
    def post(self):
        data = request.json
        email = data.get("email", None)
        password = data.get("password", None)
        if email is None or password is None:
            return '', 400
        user_service.create_user(data)
        return '', 201


# User authentication
@auth_ns.route('/login/')
class AuthViews(Resource):
    # Get tokens
    def post(self):
        data = request.json

        email = data.get("email", None)
        password = data.get("password", None)

        if email is None or password is None:
            return '', 400
        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    # Refresh tokens
    def put(self):
        data = request.json
        token = data.get('refresh_token')

        tokens = auth_service.refresh_token(token)

        return tokens, 201



# # from flask import request, abort
# # from flask_restx import Resource, Namespace
# #
# # from implemented import user_service
# # from service.auth import generate_tokens, refresh_token
# #
# # auth_ns = Namespace('auth')
# #
# # #
# # # @auth_ns.route("/register/")
# # # class AuthRegisterViews(Resource):
# # #     def post(self):
# # #         data = request.json
# # #
# # #         if not data.get('email') or not data.get('password'):
# # #             abort(400)
# # #
# # #         user_service.create_user(data)
# # #
# # #         return 'Пользователь создан', 201
# # #
# # #
# # # @auth_ns.route("/login/")
# # # class AuthLoginViews(Resource):
# # #     # def post(self):
# # #     #     data = request.json
# # #     #
# # #     #     email = data.get("email", None)
# # #     #     password = data.get("password", None)
# # #     #
# # #     #     if email is None or password is None:
# # #     #         return 'Отсутствует логин или пароль', 400
# # #     #     tokens = generate_tokens(email, password)
# # #     #     return tokens, 201
# # #
# # #     def post(self):
# # #         data = request.json
# # #
# # #         email = data.get("email", None)
# # #         password = data.get("password", None)
# # #
# # #         if email is None or password is None:
# # #             return '', 400
# # #         tokens = generate_tokens(email, password)
# # #         return tokens, 201
# # #
# # #     def put(self):
# # #         data = request.json
# # #         token = data.get('refresh_token')
# # #
# # #         tokens = refresh_token(token)
# # #
# # #         return tokens, 201
# # @auth_ns.route("/register/")
# # class RegisterView(Resource):
# #     def post(self):
# #         data = request.json
# #
# #         email = data.get('email', None)
# #         password = data.get('password', None)
# #
# #         if None in [email, password]:
# #             return ' ', 400
# #
# #         user_service.create_user(data)
# #
# #         return '', 201
# #
# #
# # @auth_ns.route("/login/")
# # class LoginView(Resource):
# #     def post(self):
# #         data = request.json
# #
# #         email = data.get('email')
# #         password = data.get('password')
# #
# #         if None in [email, password]:
# #             return ' ', 400
# #
# #         tokens = generate_tokens(email, password)
# #
# #         if not tokens:
# #             return ' ', 401
# #
# #         return tokens, 201
# #
# #     def put(self):
# #         data = request.json
# #         refresh_token = data.get('refresh_token')
# #
# #         tokens = refresh_token(refresh_token)
# #
# #         return tokens, 201
