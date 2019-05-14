from annotator.app import db
from annotator.config import Categories
from typing import Iterator, Optional


class Mention(db.Model):
    mention_id: int = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    mention_text: str = db.Column(db.Text, nullable=False)
    mention_word: int = db.Column(db.Integer, db.ForeignKey('word.word_id'))


class Word(db.Model):
    word_id: int = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    word_text: str = db.Column(db.Text, nullable=False)
    categories: str = db.Column(db.Enum(Categories), default=None)
    mentions: Iterator[Mention] = db.relationship(Mention, lazy='select')

    @property
    def next(self) -> Optional["Word"]:
        return Word.query.filter(
            Word.word_id > self.word_id
        ).order_by(Word.word_id).limit(1).first()

    @property
    def prev(self) -> Optional["Word"]:
        return Word.query.filter(
            Word.word_id < self.word_id
        ).order_by(Word.word_id).limit(1).first()

