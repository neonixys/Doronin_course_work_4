# Импорт необходимых библиотек
from marshmallow import Schema, fields

# Импорт базы данных
from setup_db import db


# Формирование класса Genre
class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# Формирование схемы Genre
class GenreSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
