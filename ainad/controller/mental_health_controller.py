from sklearn.externals import joblib
from flask import Response

class MentalHealthController(object):
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.gender_encoder = joblib.load("ml/label_Gender.sav")
        self.self_employee_encoder = joblib.load("ml/label_self_employed.sav")
        self.family_encoder = joblib.load("ml/label_family_history.sav")
        self.no_employees_encoder = joblib.load("ml/label_no_employees.sav")
        self.remote_work_encoder = joblib.load("ml/label_no_employees.sav")
        self.tech_company_encoder = joblib.load("ml/label_tech_company.sav")

    def predict(self, **kwargs):
        to_predict = [
            kwargs.get("age"),
            self.gender_encoder.transform(kwargs.get("gender")),
            self.self_employee_encoder.transform(kwargs.get("self_employeed")),
            self.family_encoder.transform(kwargs.get("family_history")),
            self.no_employees_encoder.transform(kwargs.get("no_employees")),
            self.remote_work_encoder.transform(kwargs.get("remote_work")),
            self.tech_company_encoder.transform(kwargs.get("tech_company")),
        ]

        self.model.predict([to_predict])

        return Response(status=200)
    
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
