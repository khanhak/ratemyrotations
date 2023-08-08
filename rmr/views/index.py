import flask
import rmr as app


@app.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    #connection = rmr.model.get_db()
    return flask.render_template("index.html", **context)