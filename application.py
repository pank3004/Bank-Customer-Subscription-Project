import pickle
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
application=Flask(__name__)
app=application
log_model=pickle.load(open('models/model.pkl', 'rb'))


# route for home page
@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint(): 
    if request.method=='POST':
        age=float(request.form.get('age'))
        job = float(request.form.get('job'))
        marital = float(request.form.get('marital'))
        education = float(request.form.get('education'))
        default = float(request.form.get('default'))
        housing = float(request.form.get('housing'))
        loan = float(request.form.get('loan'))
        contact = float(request.form.get('contact'))
        month = float(request.form.get('month'))
        day_of_week = float(request.form.get('day_of_week'))
        duration = float(request.form.get('duration'))
        campaign = float(request.form.get('campaign'))
        poutcome = float(request.form.get('poutcome'))
        emp_var_rate = float(request.form.get('emp_var_rate'))
        cons_price_idx = float(request.form.get('cons_price_idx'))
        cons_conf_idx = float(request.form.get('cons_conf_idx'))


        result=log_model.predict([[age,job,marital,education,default,housing,loan,contact,month,day_of_week,duration,campaign,poutcome,emp_var_rate,cons_price_idx,cons_conf_idx]])

        return render_template('home.html',result=result[0])
    else: 
        return render_template('home.html')
    


if __name__=='__main__': 
    app.run(host="0.0.0.0")