from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("map.html")
