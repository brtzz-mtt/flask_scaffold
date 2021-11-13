from cnf import *

from flask import Flask, render_template
from markdown import markdown

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
    file = open('README.md', 'r')
    html = markdown(file.read()).replace("\n", '')
    file.close()
    return flask_template_render(
        args = {'html': html}
    )

print(BASE_TITLE + " | " + COPYRIGHT)

if __name__ == '__main__':
    app.run(debug = DEBUG_MODE)
