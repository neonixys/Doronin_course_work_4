import jwt
from flask import request, abort
from flask_restx import Resource, Namespace

from constants import JWT_SECRET, JWT_ALGORITHM
from dao.model.user import UserSchema
from decorators import auth_required
from implemented import user_service

user_ns = Namespace('user')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    # Get user by email
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
        # Check if where any password
        if password:
            return "Не угадал", 403

        # Get email from token
        user_data = request.headers["Authorization"]
        token = user_data.split("Bearer ")[-1]
        decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        email = decoded_data.get('email')
        data["email"] = email

        # Update users data
        user = user_service.update_user(data)
        if not user:
            return abort(404)
        return user_schema.dump(user)


@user_ns.route('/password/')
class UsersView(Resource):
    @auth_required
    def put(self):
        data = request.json

        # Get email from token
        user_data = request.headers["Authorization"]
        token = user_data.split("Bearer ")[-1]
        decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        email = decoded_data.get('email')
        data["email"] = email

        user = user_service.update_user(data)
        if not user:
            return abort(404)
        return user_schema.dump(user)


# # import jwt
# # from flask import request, abort
# # from flask_restx import Resource, Namespace
# #
# # from constants import JWT_SECRET, JWT_ALGORITHM
# # from dao.model.user import UserSchema
# # from decorators import auth_required
# # from implemented import user_service
# # from service.auth import get_email_from_header, change_the_password
# #
# # user_ns = Namespace('user')
# #
# # user_schema = UserSchema()
# # users_schema = UserSchema(many=True)
# # @user_ns.route("/<username>")
# # class UserViews(Resource):
# #     @auth_required
# #     def get(self):
# #         req_header = request.headers['Authorization']
# #
# #         email = get_email_from_header(req_header)
# #
# #         if not email:
# #             abort(401)
# #
# #         certain_user = user_service.get_user_by_email(email)
# #
# #         return user_schema.dump(certain_user), 200
# #
# # # @user_ns.route('/')
# # # class UsersView(Resource):
# # #     @auth_required
# # #     def get(self):
# # #         user_data = request.headers["Authorization"]
# # #         token = user_data.split("Bearer ")[-1]
# # #         decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
# # #         email = decoded_data.get('email')
# # #
# # #         if email:
# # #             return user_schema.dump(user_service.get_user_by_email(email))
# # #         abort(404)
# #
# #     @auth_required
# #     def patch(self):
# #         data = request.json
# #         password = data.get("password")
# #
# #         if password:
# #             return "Нет", 403
# #
# #         user_data = request.headers["Authorization"]
# #         token = user_data.split("Bearer ")[-1]
# #         decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
# #         email = decoded_data.get('email')
# #         data["email"] = email
# #
# #         user = user_service.update_user(data)
# #         if not user:
# #             return abort(404)
# #         return user_schema.dump(user)
# #
# #
# # @user_ns.route('/password/')
# # class UsersView(Resource):
# #     @auth_required
# #     class UserPassViews(Resource):
# #         @auth_required
# #         def put(self):
# #             password_1 = request.json.get('password_1')
# #             password_2 = request.json.get('password_2')
# #             header = request.headers['Authorization']
# #             email = get_email_from_header(header)
# #
# #             return change_the_password(email, password_1, password_2)
