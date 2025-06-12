import json

def get_opensky_data():
    with open("../aircraft.json", "r") as f:
        r = json.load(f)


    print("A")
    airplanes_data = [
        [a["lon"], a["lat"], a["alt_baro"], a.get("gs", 0) * 0.514444]
        for a in r["aircraft"]
        if all(k in a and a[k] is not None for k in ("lat", "lon", "alt_baro"))
    ]

    print(r)

    for entry in airplanes_data:
        print(entry)
    # return airplanes_data

get_opensky_data()

