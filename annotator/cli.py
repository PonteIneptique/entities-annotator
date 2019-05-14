import click
import io
from typing import Optional
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
@click.option("--sample", type=click.INT)
def load(text_path: str, entities_list: io.FileIO, sample: Optional[int]=None):
    """

    :param text_path:
    :param entities_list:
    :return:
    """
    reader = LemmatizedCsvReader(text_path)
    for entity_id, entities in enumerate(entities_list.readlines()):
        word_text = entities.strip()
        word = Word(word_text=word_text)
        db.session.add(word)
        db.session.flush()
        for match in reader.get_kwic(word_text):
            db.session.add(Mention(mention_word=word.word_id, mention_text=repr(match)))
            print(repr(match))
        if sample and entity_id == sample:
            print("Stopping on sample")
            break
    db.session.commit()
