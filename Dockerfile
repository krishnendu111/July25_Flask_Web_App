FROM python:3.9-slim
WORKDIR /Users/apple/Desktop/July25_Flask_Web_App/docker

RUN python3 -m pip install --upgrade pip

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "--app", "loan_approval_predictor", "run", "--host=0.0.0.0"]

