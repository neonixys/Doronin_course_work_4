# Импорт необходимых библиотек# import jwt
import jwt
from flask import request, abort

from constants import JWT_ALGORITHM, JWT_SECRET


def auth_required(func):
    """
        Декоратор проверки аторизации
    """

    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception:
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """
       Декоратор проверки прав администратора
   """

    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            token_decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            if token_decoded['role'] != 'admin':
                abort(403)
        except Exception:
            abort(401)
        return func(*args, **kwargs)

    return wrapper
