import enum
import os


class Categories(enum.Enum):
    Org = "#F47373"
    Pers = "#697689"
    Event = "#37D67A"
    Place = "#2CCCE4"
    Wrong = "#FFFFFF"


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG = True
    template_folder = os.path.join(basedir, "templates")
    static_folder = os.path.join(basedir, "statics")
    # SQLALCHEMY_ECHO = True

    # Defaults
    PAGINATION_DEFAULT_TOKENS = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    print('THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION.')
