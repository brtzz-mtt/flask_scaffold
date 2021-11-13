from main import *

def test_cnf():
    assert isinstance(DEBUG_MODE, (bool, int))
    assert BASE_PATH
    assert isinstance(BASE_PATH, str)
    assert BASE_PATH == op.dirname(__file__) + '/'
    assert BASE_TITLE
    assert isinstance(BASE_TITLE, str)
    assert COPYRIGHT
    assert isinstance(COPYRIGHT, str)
