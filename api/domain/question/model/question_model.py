from marshmallow import fields
from api import db,ma


# model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 고유 번호
    subject = db.Column(db.String(200), nullable=False) # 제목
    content = db.Column(db.Text(), nullable=False) # 내용
    create_date = db.Column(db.DateTime(), nullable=False) # 작성일시


# marshmallow
class QuestionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Question


class QuestionRequestSchema(ma.SQLAlchemyAutoSchema):
    subject = fields.Str()
    content = fields.Str()



