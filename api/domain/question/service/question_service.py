from datetime import datetime

from api import db
from api.domain.question.model.question_model import Question, QuestionSchema, QuestionRequestSchema
from api.domain.question.dao.question_dao import QuestionDao

question_dao = QuestionDao()


class QuestionService:

    def question_list(self):
        question_list = Question.query.order_by(Question.create_date.desc())
        question_schema = QuestionSchema(many=True)
        question = question_schema.dump(question_list)
        return question

    # SQLAlchemy 사용
    def create(self, payload):
        question_schema = QuestionRequestSchema()
        payload = question_schema.load(payload)
        question = Question(subject=payload["subject"], content=payload['content'], create_date=datetime.now())
        db.session.add(question)
        db.session.commit()

    # MySQL-Connector 사용
    #def create(self, payload):
    #    question_dao.create(payload)

    def update(self, question_id, payload):
        question_schema = QuestionRequestSchema()
        payload = question_schema.load(payload)
        question = Question.query.get(question_id)
        question.subject = payload["subject"]
        question.content = payload['content']
        db.session.commit()

    def delete(self, question_id):
        question = Question.query.get(question_id)
        db.session.delete(question)
        db.session.commit()