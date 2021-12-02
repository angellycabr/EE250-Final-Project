import pickle
from flask import Flask,request
from flask import jsonify
import json

clf = pickle.load(open('model.pickle','rb'))

app = Flask(__name__)
#Want volume to come from the raspberry pi

@app.route("/classify")
def hello_world():

   volume = pickle.load(open("sound.pickle", "rb"))
   genre = clf.predict([[float(volume)]])[0]
   
   return json.dumps({"genre" : genre})
