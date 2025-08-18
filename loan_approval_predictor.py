from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route("/ping", methods=['GET'])
def pinger():
    return {'message': 'Suraaj is the instructor for MLOPS'}

@app.route("/predict", methods=['POST'])
def prediction():
    loan_req= request.get_json()
    print(loan_req)

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
    if loan_req['Married'] == "Yes":
        Married = 1
    else:
        Married = 0

    Applicant_Income = loan_req['ApplicantIncome']
    Loan_Amount = loan_req['LoanAmount']
    Credit_History= loan_req['Credit_History']

    model = open("./classifier.pkl", "rb")
    clf = pickle.load(model)
    result= clf.predict([[Gender, Married, Applicant_Income, Loan_Amount, Credit_History]])

    print(result)

    return {'loan_approval_status':str(result)}