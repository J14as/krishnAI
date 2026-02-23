from models.user import db
from sqlalchemy import ForeignKey


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    conversation_id = db.Column(db.Integer, ForeignKey('conversation.id'), nullable=True)
    user_message = db.Column(db.Text, nullable=False)
    ai_response = db.Column(db.Text, nullable=False)
