from annotator.app import db
from annotator.config import Categories
from typing import Iterator


class Mention(db.Model):
    mention_id: int = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    mention_text: str = db.Column(db.Text, nullable=False)
    mention_word: int = db.Column(db.Integer, db.ForeignKey('word.word_text'))


class Word(db.Model):
    word_id: int = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    word_text: str = db.Column(db.Text, nullable=False)
    categories: str = db.Column(db.Enum(Categories), default=None)
    user: Iterator[Mention] = db.relationship(Mention, lazy='select')
