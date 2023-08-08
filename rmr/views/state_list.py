import flask
import rmr as app
import json
import pandas as pd
from flask import url_for, render_template

@app.app.route('/state_list/')
def show_state_list():
    json_file = "rmr//static//us_states.json"
    ls = []
    f = open(json_file)
    data = json.load(f)
    for k,v in data.items():
        ls.append({
            'abbreviation':k,
            'state_name':v
        })
    context = {"state_list":ls}
    return render_template("state_list.html",**context)


