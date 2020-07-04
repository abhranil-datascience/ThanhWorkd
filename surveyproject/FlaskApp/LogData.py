from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pandas as pd
import random
app = Flask(__name__)
api = Api(app)

################################### Greet User secured by Json Web Token ####################################################
class LogData(Resource):
    def get(self):
        logdata = request.args['logdata']
        XCoordinate=[]
        YCoordinate=[]
        Time=[]
        datatokenized=logdata.split("|")
        for item in datatokenized:
            if "," in item:
                XYSplitted=item.split(",")
                XCoordinate.append(XYSplitted[0])
                YCoordinate.append(XYSplitted[1])
                Time.append(XYSplitted[2])
            else:
                XCoordinate.append("NA")
                YCoordinate.append("NA")
                Time.append(item)
        ResultDict=dict(XCoordinate=XCoordinate,YCoordinate=YCoordinate,TimeInSeconds=Time)
        ResultDF=pd.DataFrame.from_dict(ResultDict)
        Filename="MouseCapture"+str(random.randint(10000,99999))+".csv"
        FilePath="../LogData/"+Filename
        ResultDF.to_csv(FilePath,index=False)
        return "success"

api.add_resource(LogData, '/LogData')

# driver function
if __name__ == '__main__':
    app.run(debug = True)
