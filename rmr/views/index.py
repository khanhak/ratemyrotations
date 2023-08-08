import flask
import rmr as app


@app.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    #connection = rmr.model.get_db()
    return flask.render_template("index.html", **context)

@app.app.route('/input/')
def show_input_form():
    return flask.redirect("https://docs.google.com/forms/d/e/1FAIpQLSfoHfv6Y3raKQe6h_Leab6Db76E-PVN5cJDvKVfExbRpf0waQ/viewform",code=302)