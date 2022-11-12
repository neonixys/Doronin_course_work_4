import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_user_by_id(self, uid):
        """
            Получение пользователя по id
        """
        return self.dao.get_user_by_id(uid)

    def get_user_by_email(self, email: str):
        return self.dao.get_user_by_email(email)

    def get_all_users(self):
        """
            Получение всех пользователей
        """
        return self.dao.get_all_users()

    def create_user(self, user_data):
        """
            Создание пользователя
        """
        password = user_data.get('password')
        hashed_password = self.generate_password(password)
        user_data['password'] = hashed_password
        self.dao.create_user(user_data)

    def patch_user(self, user_data):
        user = self.get_user_by_id(user_data['id'])

        if user_data.get('name'):
            user.name = user_data['name']
        if user_data.get('surname'):
            user.name = user_data['surname']

    def update_user(self, user_data: dict):
        return self.dao.update_user(user_data)

    def update_password(self):
        pass

    def delete_user(self, user_data):
        """
            Удаление пользователя
        """
        return self.dao.delete_user(user_data)

    def generate_password(self, password):
        """
            Хэширование пароля
        """
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password):
        """
            Сравнение хэшированного пароля и введенного пароля
        """

        hashed_pasword = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        decoded_password = base64.b64decode(password_hash)

        return hmac.compare_digest(decoded_password, hashed_pasword)
