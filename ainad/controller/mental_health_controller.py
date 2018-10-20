from sklearn.externals import joblib
from flask import Response
import json

class MentalHealthController(object):
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.gender_encoder = joblib.load("ml/encoders/label_Gender.sav")
        self.self_employee_encoder = joblib.load("ml/encoders/label_self_employed.sav")
        self.family_encoder = joblib.load("ml/encoders/label_family_history.sav")
        self.no_employees_encoder = joblib.load("ml/encoders/label_no_employees.sav")
        self.remote_work_encoder = joblib.load("ml/encoders/label_remote_work.sav")
        self.tech_company_encoder = joblib.load("ml/encoders/label_tech_company.sav")
        self.work_interfere_encoder = joblib.load("ml/encoders/label_work_interfere.sav")

    def predict(self, request):
        ne = self.transform_n_employee(int(request.args.get("no_employees")))

        to_predict = [
            request.args.get("age"),
            self.gender_encoder.transform([request.args.get("gender")]),
            self.self_employee_encoder.transform([request.args.get("self_employeed")]),
            self.family_encoder.transform([request.args.get("family_history")]),
            self.no_employees_encoder.transform([ne]),
            self.remote_work_encoder.transform([request.args.get("remote_work")]),
            self.tech_company_encoder.transform([request.args.get("tech_company")]),
            self.work_interfere_encoder.transform([request.args.get("work_interfere")])
        ]

        pred = int(self.model.predict([to_predict])[0])
        res = {
            "prediction": pred,
        }        
        return Response(json.dumps(res), status=200)
    
    def transform_n_employee(self, ne):
        if ne <= 5:
            return '1-5'
        
        if ne <= 25:
            return '6-25'
        
        if ne <= 100:
            return '26-100'

        if ne <= 500:
            return '100-500'

        if ne <= 1000:
            return '500-1000'

        return 'More than 1000'

    def transform_gender(self, gender):
        gender = gender.lower()

        #Made gender groups
        male_str = ["male", "m", "male-ish", "maile", "mal", "male (cis)", "make", "male ", "man","msle", "mail", "malr","cis man", "Cis Male", "cis male"]
        trans_str = ["trans-female", "something kinda male?", "queer/she/they", "non-binary","nah", "all", "enby", "fluid", "genderqueer", "androgyne", "agender", "male leaning androgynous", "guy (-ish) ^_^", "trans woman", "neuter", "female (trans)", "queer", "ostensibly male, unsure what that really means"]           

        if gender in male_str:
            return "male"
        
        if gender in trans_str:
            return "trans"
        return "female"
