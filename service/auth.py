import calendar
import datetime

import jwt
from flask_restx import abort

from constants import JWT_SECRET, JWT_ALGORITHM
from service.user import UserService


class AuthService:
    def __init__(self, service: UserService):
        self.user_service = service

    def generate_tokens(self, email: str, password: str | None, is_refresh: bool = False) -> dict:
        """
        This function is generate access and refresh tokens
        """
        user = self.user_service.get_user_by_email(email)
        # Check if where is a user
        if user is None:
            raise abort(404)
        # Check if users password is in the db
        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                raise abort(400)

        # Transform password to string, because jwt can`t encode bytes
        data = {
            "email": user.email,
            "password": user.password.decode('utf-8')
        }
        # 30 min token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(payload=data, key=JWT_SECRET, algorithm=JWT_ALGORITHM)

        # 130 day token
        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(payload=data, key=JWT_SECRET, algorithm=JWT_ALGORITHM)

        tokens = {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

        return tokens

    # Generate new access token
    def refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, JWT_SECRET, JWT_ALGORITHM)
        email = data.get("email")
        return self.generate_tokens(email, None, is_refresh=True)
#
#
#
#
# # # Импорт необходимых библиотек
# # import base64
# # import calendar
# # import datetime
# # import hashlib
# # import hmac
# #
# # import jwt
# # from flask import abort
# #
# # from constants import JWT_SECRET, JWT_ALGORITHM, PWD_HASH_SALT, PWD_HASH_ITERATIONS
# # from implemented import user_service
# # from setup_db import db
# #
# #
# # def generate_tokens(email, password, is_refresh=False):
# #     user = user_service.get_user_by_email(email)
# #
# #     if user is None:
# #         raise abort(404)
# #
# #     if not is_refresh:
# #         db_pass = user.password
# #         if not check_password(db_pass, password):
# #             raise abort(400)
# #
# #     data = {
# #         "email": user.email,
# #         "password": user.password.decode('utf-8')
# #     }
# #     min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
# #     data['exp'] = calendar.timegm(min30.timetuple())
# #     access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
# #
# #     days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
# #     data['exp'] = calendar.timegm(days130.timetuple())
# #     refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
# #
# #     return {'access_token': access_token,
# #             'refresh_token': refresh_token}
# #
# #
# # # def generate_tokens(self, email: str, password: str | None, is_refresh: bool = False):
# # #     """
# # #         Генерация токенов
# # #     """
# # #
# # #     user = self.user_service.get_user_by_email(email)
# # #
# # #     if user is None:
# # #         raise abort(401)
# # #
# # #     # Проверка на обновление токенов (is_refresh=True) или формирование изначальных (is_refresh=False)
# # #     # Сравнение введенного и хэшированного паролей
# # #     if not is_refresh:
# # #         if not self.user_service.compare_passwords(user.password, password):
# # #             raise abort(401)
# # #
# # #     data = {
# # #         "email": user.email,
# # #         "password": user.password.decode('utf-8')
# # #     }
# # #
# # #     # Формирование срока действия токенов
# # #     # 30 минутный токен
# # #     min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
# # #     data["exp"] = calendar.timegm(min30.timetuple())
# # #     access_token = jwt.encode(payload=data, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
# # #
# # #     # 130 дневный токен
# # #     day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
# # #     data["exp"] = calendar.timegm(day130.timetuple())
# # #     refresh_token = jwt.encode(payload=data, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
# # #
# # #     tokens = {
# # #         "access_token": access_token,
# # #         "refresh_token": refresh_token
# # #     }
# # #
# # #     return tokens
# # #
# #
# # def check_password(db_hash, client_password):
# #     decoded_digest = base64.b64decode(db_hash)
# #
# #     hash_digest = hashlib.pbkdf2_hmac(
# #         'sha256',
# #         client_password.encode('utf-8'),
# #         PWD_HASH_SALT,
# #         PWD_HASH_ITERATIONS
# #     )
# #
# #     return hmac.compare_digest(decoded_digest, hash_digest)
# #
# #
# # def refresh_token(self, refresh_token):
# #     """
# #         Обновление токенов по refresh_token
# #     """
# #     data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
# #     email = data.get("email")
# #     return self.generate_tokens(email, None, is_refresh=True)
# #
# #
# # def get_email_from_header(header: str):
# #     token = header.split('Bearer ')[-1]
# #     data_dict = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
# #
# #     email = data_dict.get('user_email')
# #
# #     return email
# #
# #
# # def change_the_password(user_email, pass1, pass2):
# #     user = user_service.get_user_by_email(user_email)
# #
# #     db_pass = user.password
# #
# #     is_confirmed = check_password(db_pass, pass1)
# #
# #     if is_confirmed:
# #         user.password = user_service.get_hash(pass2)
# #
# #         db.session.add(user)
# #         db.session.commit()
# #
# #         return '', 204
# #
# #     abort(401)
