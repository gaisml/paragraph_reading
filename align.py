import os
from flask import request
from flask_restx import Resource
from application.resources.Aligner.extract import User
from application.resources.utils.input import input_fields
from application import api
from application.resources.Aligner import text_grid
from application.resources.Aligner import data
import pandas as pd
align= api.namespace('aligner', description='Used to align')

@align.route('/',endpoint='/align')
class Aligner(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        out_value = Aligner.get_data(words=json_data['paragraph '])
        return out_value





    # def post(self):
    #     json_data = request.get_json(force=True)
    #     out_value = Aligner.get_alignment(words=json_data['word'])
    #     return out_value



