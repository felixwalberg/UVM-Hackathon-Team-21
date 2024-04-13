from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

GMT_VEHICLES_URL = "https://maps.trilliumtransit.com/gtfsmap-realtime/feed/ccta-vt-us/vehicles"
GMT_ROUTES_URL = "https://gtfs-api.trilliumtransit.com/gtfs-api/routes/by-feed/ccta-vt-us"
GMT_STOPS_URL = "https://gtfs-api.trilliumtransit.com/gtfs-api/stops/by-feed/ccta-vt-us/route-id/19137,19139,13496,13497,13498,3190,3191,7458,11182,7455,74419,74409,74410,74411,19141,74418,74413,3175,74412,3153,3176,3167,3177,3181,3168,3183,3197,3194,19140,3195,3196,3186,7335,74414,74415,3171,3172,3174,3188,74416,74417,3163,3164,3165,19138,32941,32942,11183,19143,19142,19144,19145,"

@app.route("/", methods=["GET"])
def home():
    return render_template("map.html")

@app.route("/data/vehicles", methods=["POST"])
def vehicleData():
    # TODO: handle failure to fetch data
    return jsonify(get_vehicles());

def get_vehicles():
    res = requests.get(GMT_VEHICLES_URL)
    data = res.json()

    if data['status'] != "success":
        return None

    return data['data']

if __name__=="__main__":
    app.run(debug=True)
