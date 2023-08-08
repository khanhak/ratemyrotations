"""rmr development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'0'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
rmr_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = rmr_ROOT/'var'/'uploads'
STATIC_FOLDER = rmr_ROOT/'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/rmr.sqlite3
DATABASE_FILENAME = rmr_ROOT/'var'/'rmr.sqlite3'

