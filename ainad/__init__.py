from flask import Flask, request, Response
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from controller.mental_health_controller import MentalHealthController

app = Flask(__name__)
mental_health_ctrl = MentalHealthController("ml/ada_bost_clf.joblib")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mental-health')
def mental_health(request):
    mental_health_ctrl.predict(
        age=request.args.get("age"),
        self_employeed=request.args.get("self_employeed"),
        family_history=request.args.get("family_history"),
        no_employees=request.args.get("no_employees"),
        remote_work=request.args.get("remote_work"),
        tech_company=request.args.get("tech_company"),
    )
