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

def test_app():
    assert app is not None

    assert str(type(app)) == "<class 'flask.app.Flask'>"
    assert app.static_folder == BASE_PATH + 'static'
    assert app.template_folder == 'templates'

    view_functions = app.view_functions

    assert 'index' in view_functions

    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.charset == 'utf-8'
        assert response.mimetype == 'text/html'
        assert response.status == '200 OK'
