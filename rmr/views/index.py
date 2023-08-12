import flask
import rmr as app
import pandas as pd

@app.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    #connection = rmr.model.get_db()

    SHEET_ID = '1TX-A8lL0XJnNayQYsgDOcRbweo2l724BN9eerbNH6XI'
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv'
    df = pd.read_csv(url)
    #print("csv head",df.head())
    #TODO: improve speed by vectorizing operations instead of going row by row and splitting
    info = []
    
    for idx,row in df.iterrows():
        timestamp = row['Timestamp']
        rotation_site = row['Name of rotation site']
        specialty = row['Specialty']
        teaching_quality = row['Teaching Quality (1 is worst, 5 is best)']
        patient_exposure = row['Patient Exposure']
        preceptor_support = row['Preceptor Support']
        hours_per_week = row['Average hours per week']
        comments = row['Comments']

        info.append({
            "timestamp":timestamp,#this should be hidden from user, but available for sorting
            "rotation_site_name":rotation_site,
            "specialty":specialty,
            "teaching_quality":teaching_quality,
            "patient_exposure":patient_exposure,
            "preceptor_support":preceptor_support,
            "hours_per_week":hours_per_week,
            "comments":comments
        })


        

    context = {"rotation_info":info}


    return flask.render_template("index.html", **context)

@app.app.route('/input/')
def show_input_form():
    return flask.redirect("https://docs.google.com/forms/d/e/1FAIpQLSfoHfv6Y3raKQe6h_Leab6Db76E-PVN5cJDvKVfExbRpf0waQ/viewform",code=302)