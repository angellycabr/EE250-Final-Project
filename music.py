import requests
import json
import random


def music_init():

    genre_json = requests.get("http://172.17.0.4:5000/classify?w=50").json()
    
    gen = genre_json['genre']
    print(gen)
    
    artist = {
    'blues' : ["Clarence Carter", "Luther Allison", "Son Seals"],
    'pop' : ["Beyonce", "Frank Ocean", "Drake"],
    'rock' : ["Led Zeppelin", "Guns N' Roses", "Radiohead"],
    'jazz' : ["Frank Sinatra", "Dean Martin", "Duke Ellington"]
    }

    num = random.randrange(0,3)
    
    url = "https://genius.p.rapidapi.com/search"
    querystring = {"q": artist[gen][num]}

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': "ced02c282fmsh9cf47f9d3973c56p175a75jsn2604638f4c3e"
        }

    r = requests.get(url, headers=headers,params=querystring)
    data = r.json()
    
    song1 = data['response']['hits'][0]['result']['title']
    song2 = data['response']['hits'][1]['result']['title']
    song3 = data['response']['hits'][2]['result']['full_title']
    output = song1 + ", " + song2 + ", " + song3 
    print(output)
    return str(output)

MUSIC_APP = {
    'name': 'Genre Recs',
    'init': music_init
}
    
if __name__ == '__main__':
    music_init()
