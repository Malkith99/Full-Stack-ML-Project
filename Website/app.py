from flask import Flask, render_template,request
import pickle

app=Flask(__name__)


def prediction(lst):
    filename = 'model/predictor1.pickle'
    with open(filename, 'rb') as file:      #rb- read binart
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/',methods=['POST','GET'])
def index():
    pred="NULL"
    if request.method=='POST':
        gender=request.form['gender']
        married=request.form['married']
        dependents=request.form['dependents']
        education=request.form['education']
        selfEmployed=request.form['selfEmployed']
        applicantIncome=request.form['applicantIncome']
        coapplicantIncome=request.form['coapplicantIncome']
        loanAmount=request.form['loanAmount']
        loanAmountTerm=request.form['loanAmountTerm']
        propertyArea=request.form['propertyArea']
        if request.form.getlist('creditHistory'):
            creditHistory=1
        else:
            creditHistory=0


        feature_list=[int(gender),int(married),int(dependents),int(education),int(selfEmployed),int(applicantIncome),int(coapplicantIncome),int(loanAmount),int(loanAmountTerm)]

        property_list=['Semiurban','Urban','Rural']    
        def encodingList(list,value):    
            for item in list:
                if item==value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        encodingList(property_list,propertyArea)
        feature_list.append(creditHistory)

        print(feature_list)
        pred_value=prediction(feature_list)
        print(pred_value)
        if pred_value[0]==1:
            pred="Loan Approved"
        else:
            pred="Loan Rejected"
        print(pred)
    return render_template('index.html',pred=pred)   

if __name__=="__main__":
    app.run(debug=True)