from flask import Flask, request, Response
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from controller.mental_health_controller import MentalHealthController

app = Flask(__name__)
mental_health_ctrl = MentalHealthController("ml/ada_bost_clf.joblib")

@app.route('/')
def hello_world():
    return 'Hello, World!'

# http://127.0.0.1:5000/mental-health?age=22&gender=male&self_employeed=No&family_history=No&no_employees=6-25&remote_work=No&tech_company=Yes&work_interfere=Often
@app.route('/mental-health')
def mental_health():
    return mental_health_ctrl.predict(request)

if __name__ == "__main__":
    app.run()