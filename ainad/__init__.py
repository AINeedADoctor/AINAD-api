from flask import Flask, request, Response
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from ainad.controller.mental_health_controller import MentalHealthController
from ainad.controller.prevent_stress_controller import PreventStressController

app = Flask(__name__)
mental_health_ctrl = MentalHealthController("ml/ada_bost_clf.joblib")
prevent_stress_ctrl = PreventStressController("ml/logistic_regression.joblib")

@app.route('/')
def hello_world():
    return 'Hello, World!'

# /mental-health?age=22&gender=male&self_employeed=No&family_history=No&no_employees=6-25&remote_work=No&tech_company=Yes&work_interfere=Often
@app.route('/mental-health')
def mental_health():
    return mental_health_ctrl.predict(request)

# /prevent-stress?sex=male&na=3&ho=5&lr=2&hp=0&hpm=0&ca=1&ha=1&asm=0&dep=0&child=2&smoke=1&civil=1
@app.route('/prevent-stress')
def prevent_stress():
    return prevent_stress_ctrl.predict(request)


if __name__ == "__main__":
    app.run()