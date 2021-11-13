import os.path as op

DEBUG_MODE = True

README_FILE = 'README.md'

BASE_PATH = op.dirname(__file__) + '/'

with open(BASE_PATH + README_FILE) as readme_file:
    BASE_TITLE = readme_file.readline().strip()
    for line in readme_file:
        pass
    COPYRIGHT = line
