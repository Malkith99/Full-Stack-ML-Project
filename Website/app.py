from flask import Flask, render_template,request
import pickle
import numpy as np

app=Flask(__name__)


def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        gender=request.form['gender']
        married=request.form['married']
        dependents=request.form['dependents']
        education=request.form['education']
        selfEmployed=request.form['selfEmployed']
        coapplicantIncome=request.form['coapplicantIncome']
        loanAmount=request.form['loanAmount']
        loanAmountTerm=request.form['loanAmountTerm']
        if request.form.getlist('creditHistory'):
            creditHistory=1
        else:
            creditHistory=0
        #print(creditHistory)
        feature_list=[gender,married,dependents,education,selfEmployed,coapplicantIncome,loanAmount,loanAmountTerm,creditHistory]
        
        pred_value=prediction(feature_list)
        if pred_value[0]==1:
            return render_template('index.html',pred="Loan Approved")
        else:
            return render_template('index.html',pred="Loan Rejected")

    return render_template('index.html')   

if __name__=="__main__":
    app.run(debug=True)