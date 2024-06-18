from flask import Flask, render_template,request

app=Flask(__name__)

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
        print(creditHistory)


    return render_template('index.html')   

if __name__=="__main__":
    app.run(debug=True)