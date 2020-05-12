from flask import (
    Blueprint,
    current_app, redirect, render_template,
    request, url_for)


bp = Blueprint('dreamcatcher', __name__)


@bp.route('/')
def render_chart():
    hello_text = current_app.config['HELLO_TEXT']
    return render_template('base.html', hello_text=hello_text)
