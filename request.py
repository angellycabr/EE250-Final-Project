import requests
import pickle

genre_json = requests.get("http://172.17.0.2:5000/classify?w=50").json()
gen = genre_json['genre']

pickle.dump(gen, open("req.pickle", "wb"))
