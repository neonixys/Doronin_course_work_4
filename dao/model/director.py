# Импорт необходимых библиотек
from marshmallow import Schema, fields

# Импорт базы данных
from setup_db import db


# Формирование класса Director
class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# Формирование схемы Director
class DirectorSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
