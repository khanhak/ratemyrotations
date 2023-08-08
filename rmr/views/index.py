import flask
import rmr


@rmr.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    #connection = rmr.model.get_db()
    return flask.render_template("index.html", **context)