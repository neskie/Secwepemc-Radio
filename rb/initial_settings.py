import os

#Remote host to control over ssh
REMOTE_HOST = 'hostname'
PORT = '22'
USER = 'username'

IDENTITY_FILE = 'identity file'

RB_ROOT = os.path.realpath(os.path.dirname(__file__))
DB_FILE = os.path.join(RB_ROOT, 'db.dump')
