import enum
import os


class Categories(enum.Enum):
    Org = "Organization"
    Pers = "Person"
    Event = "Event"
    Place = "Place"


class Colors(enum.Enum):
    Categories.Org = "#F47373"
    Categories.Pers = "#697689"
    Categories.Event = "#37D67A"
    Categories.Place = "#2CCCE4"


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    template_folder = os.path.join(basedir, "templates")
    static_folder = os.path.join(basedir, "statics")
    # SQLALCHEMY_ECHO = True

    # Defaults
    PAGINATION_DEFAULT_TOKENS = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    print('THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION.')
