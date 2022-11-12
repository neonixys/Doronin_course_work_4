from flask import request, abort, render_template
from flask_restx import Resource, Namespace


from implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route("/register/")
class AuthRegisterViews(Resource):
    def post(self):
        data = request.json

        if not data.get('email') or not data.get('password'):
            abort(400)

        user_service.create_user(data)

        return 'Пользователь создан', 201


@auth_ns.route("/login/")
class AuthLoginViews(Resource):
    def post(self):
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            return "Отсутствует логин или пароль", 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token')
        print(refresh_token)

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201
