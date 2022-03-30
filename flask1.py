from flask import Flask, jsonify, request
import csv 
import pandas as pd 

x = []

with open("flask1/movies.csv") as y:
    reader = csv.reader(y)
    data = list(reader)
    x = data[1:]

liked_movies = []
disliked_movies = []
unwatched = []

app = Flask(__name__)

@app.route('/get-movie') 

def get_movie():
    return jsonify({
        "data":x[0],
        "status":"success!",
        })

@app.route("/liked-movies", methods = ["POST"])

def liked_movies():
    movie = x[0]
    x = x[1:]
    liked_movies.append(movie)

    
    return jsonify({
        "status":"success"
    }), 201

@app.route("/disliked-movies", methods = ["POST"])

def disliked_movies():
    movie = x[0]
    x = x[1:]
    disliked_movies.append(movie)

    
    return jsonify({
        "status":"success"
    }), 201

@app.route("/unwatched", methods = ["POST"])

def unwatched():
    movie = x[0]
    x = x[1:]
    unwatched.append(movie)
    return jsonify({
        "status":"success"
    }), 201

if __name__ == "__main__":
    app.run()

'''



    


