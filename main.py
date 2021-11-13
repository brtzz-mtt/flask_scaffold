from cnf import *

from flask import Flask, render_template

def flask_template_render(template: str = 'index.html',
    title: str = BASE_TITLE,
    args: dict = {},
    debug: bool = DEBUG_MODE
) -> str:
    return render_template(template,
        title = title,
        args = args,
        debug = debug
    )

app = Flask(__name__)

@app.route('/')
def index():
    return flask_template_render()

if __name__ == '__main__':
    print(BASE_TITLE + " | " + COPYRIGHT)
    app.run(debug = DEBUG_MODE)
