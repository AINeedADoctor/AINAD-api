from sklearn.externals import joblib
from flask import Response
import json
import numpy as np

class PreventStressController(object):
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, request):
        predict = [
            1 if request.args.get("sex") == "male" else 2,
            request.args.get("na"),     # Number adults  
            request.args.get("ho"),     # Health opinion
            request.args.get("lr"),     # last revision
            request.args.get("hp"),     # High presion       
            request.args.get("hpm"),    # Medicate?
            request.args.get("ca"),     # Colesterol alt
            request.args.get("ha"),     # heart attack
            request.args.get("asm"),    # Asma
            request.args.get("dep"),    # depresion y/n
            request.args.get("civil"),  # Estat civil
            request.args.get("child"),  # How many children
            request.args.get("smoke"),  # smoke y/n
        ]

        res = {
            "prediction": int(self.model.predict(
                np.array(predict, dtype=float).reshape(1, -1)
            )[0])
        }

        return Response(json.dumps(res), status=200)