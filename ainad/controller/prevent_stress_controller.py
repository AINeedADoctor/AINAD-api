from sklearn.externals import joblib
from flask import Response
import json

class PreventStressController(object):
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, request):
        predict = [
            request.args.get("sex"),
            request.args.get("na"),     # Number adults  
            request.args.get("ho"),     # Health opinion
            request.args.get("lr"),     # last revision
            request.args.get("hp"),     # High presion       
            request.args.get("hpm"),    # Medicate?
            request.args.get("ca"),     # Colesterol alt
            request.args.get("ha"),     # heart attack
            request.args.get("asm"),    # Asma
            request.args.get("dep"),    # depresion y/n
            request.args.get("child"),  # How many children
            request.args.get("smoke"),  # smoke y/n
            request.args.get("civil"),  # Estat civil
        ]

        res = {
            "prediction": self.model.predict([predict])
        }

        return Response(json.dumps(res), status=200)