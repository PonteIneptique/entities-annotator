import click
import io
from annotator.app import db, app
from annotator.reader import LemmatizedCsvReader
from annotator.models import Word, Mention


@app.cli.group("annotator")
def cli() -> click:
    """ Loads and dumps data into/from the database using readers """


@cli.command()
def init():
    db.create_all()


@cli.command()
@click.argument("text_path", type=click.Path())
@click.argument("entities_list", type=click.File())
def load(text_path: str, entities_list: io.FileIO):
    """

    :param text_path:
    :param entities_list:
    :return:
    """
    reader = LemmatizedCsvReader(text_path)
    for entities in entities_list.readlines():
        word_text = entities.strip()
        word = Word(word_text=word_text)
        db.session.add(word)
        db.session.flush()
        for match in reader.get_kwic(word_text):
            db.session.add(Mention(mention_word=word.word_id, mention_text=repr(match)))
            print(repr(match))
    db.session.commit()
