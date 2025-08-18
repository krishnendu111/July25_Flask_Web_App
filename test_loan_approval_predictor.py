import pytest
import json
from loan_approval_predictor import app

@pytest.fixture
def client():      #pass this as an input parameter wherever server is req
    return app.test_client()

def test_pinger(client):
    resp= client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {'message': 'Suraaj is the instructor for MLOPS'}

def test_prediction(client):
    test_data = {
    "Gender": "Male",
    "Married": "Yes",
    "ApplicantIncome": 5000000,
    "LoanAmount": 5000,
    "Credit_History": 1.0
}
    resp= client.post('/predict', json =test_data)

    assert resp.status_code == 200
    assert resp.json == {'loan_approval_status': '[1]'}
