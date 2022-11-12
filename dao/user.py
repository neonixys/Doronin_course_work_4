from dao.model.user import User


class UserDAO:
    """
        Класс получает данные из bd
    """
    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        """
            Получение всех пользователей
        """
        return self.session.query(User).all()

    def get_user_by_id(self, uid):
        """
            Получение пользователя по username
        """
        return self.session.query(User).filter(User.id == uid).one()


    def get_user_by_email(self, email):
        """
            Получение пользователя по email
        """
        return self.session.query(User).filter(User.email == email).first()


    def create_user(self, user_data):
        """
            Создание пользователя
        """
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        return user

    def update_user(self, user_data: dict):
        """
            Обновление пользователя
        """
        email = user_data.get("email")
        self.session.query(User).filter(User.email == email).update(user_data)
        self.session.commit()
        return self.get_user_by_email(email)

