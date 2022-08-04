
from flask_frozen import Freezer
from app import app

FREEZER_DESTINATION = '../build'

FREEZER_IGNORE_MIMETYPE_WARNINGS = True

# FREEZER_SKIP_EXISTING = True

FREEZER_REMOVE_EXTRA_FILES = False

app.config.from_object(__name__)



freezer = Freezer(app, with_static_files=True, log_url_for=False, with_no_argument_rules=False)

@freezer.register_generator
def url_generator():
    yield '/'

if __name__ == '__main__':
    freezer.freeze()
