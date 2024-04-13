from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

GMT_VEHICLES_URL = "https://maps.trilliumtransit.com/gtfsmap-realtime/feed/ccta-vt-us/vehicles"
CAT_VEHICLES_URL = "https://feeds.transloc.com/3/vehicle_statuses?agencies=603&include_arrivals=true"
GMT_ROUTES_URL = "https://gtfs-api.trilliumtransit.com/gtfs-api/routes/by-feed/ccta-vt-us"
GMT_STOPS_URL = "https://gtfs-api.trilliumtransit.com/gtfs-api/stops/by-feed/ccta-vt-us/route-id/19137,19139,13496,13497,13498,3190,3191,7458,11182,7455,74419,74409,74410,74411,19141,74418,74413,3175,74412,3153,3176,3167,3177,3181,3168,3183,3197,3194,19140,3195,3196,3186,7335,74414,74415,3171,3172,3174,3188,74416,74417,3163,3164,3165,19138,32941,32942,11183,19143,19142,19144,19145,"
STOP_DATA = "/static/routes.json"

@app.route("/", methods=["GET"])
def home():
    return render_template("map.html")

@app.route("/data/vehicles", methods=["POST"])
def vehicleData():
    # TODO: handle failure to fetch data
    return jsonify(get_vehicles());

def gmt_buses():
    res = requests.get(GMT_VEHICLES_URL)
    data = res.json()

    if data['status'] != "success":
        print("ERROR fetching gmt buses")
        return None

    items = data['data']

    ROUTES = ["19137", "19139"]
    vehicles = [bus for bus in items if bus["route_id"] in ROUTES]
    return vehicles


def cat_buses():
    res = requests.get(CAT_VEHICLES_URL)
    data = res.json()
    if data['success'] != True:
        print("ERROR fetching cat buses")
        return None

    return [{'id': bus['id'],
             'lat': bus['position'][0],
             'lon': bus['position'][1]} for bus in data['vehicles']]


def get_vehicles():
    return {
        'gmt': gmt_buses(),
        'cat': cat_buses()
    }

@app.route("/data/routes", methods=["POST"])
def stopData():
    return jsonify(get_stops())
def get_stops():
    bus_routes = []
    with open(STOP_DATA) as file:
        data = json.load(file)

    route1 = "19137"
    route1_data = []
    route2 = "19139"
    route2_data = []
    for stop in data[route1]['stops']:
        stop_data = [stop["stop_name"], stop["stop_code"], stop["coordinates"][0], stop["coordinates"][1]]
        route1_data.append(stop_data)
    for stop in data[route2]['stops']:
        stop_data = [stop["stop_name"], stop["stop_code"], stop["coordinates"][0], stop["coordinates"][1]]
        route2_data.append(stop_data)
    bus_routes.append(route1_data)
    bus_routes.append(route2_data)

    return bus_routes

if __name__=="__main__":
    app.run(debug=True)
