import flask
import rmr as app
import json
import pandas as pd
from collections import defaultdict

from flask import render_template, redirect, url_for

#filter
def process_timestamp(timestamp):
    split = timestamp.split("/")
    return str(split[1] + "/" + split[2][:4])
app.app.jinja_env.filters['process_timestamp'] = process_timestamp
@app.app.route('/state_input/')
def input_rotation_info():
    return redirect("https://forms.gle/W6U5s9Zb9pi2MC3YA",code=302)


@app.app.route('/sites_by_state/<string:state_abbreviation>/')
def show_states(state_abbreviation):


    #get state names and abberviations
    json_file = "rmr//static//us_states.json"
    ls = []
    f = open(json_file)
    state_json = json.load(f)
    this_state_name = state_json[state_abbreviation]



    # scrape data from GSheets with pandas, only add to list if state_name = string state_name
    # 
    '''
    - Scrape data from GSheets with pandas
    - NOTE: this might be slow (or google might rate limit me) so maybe I should do this asynchronously, store it in my DB, then render from my DB when user needs it
    - Maybe 
    
    '''
    SHEET_ID = '1TX-A8lL0XJnNayQYsgDOcRbweo2l724BN9eerbNH6XI'
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv'
    df = pd.read_csv(url)
    #print("csv head",df.head())
    filtered_df = df.loc[df['State'] == this_state_name]
    #TODO: improve speed by vectorizing operations instead of going row by row and splitting
    info = []
    
    for idx,row in filtered_df.iterrows():
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


        

    context = {"rotation_info":info,"state_name":this_state_name}
    return render_template("state_input.html",**context)


