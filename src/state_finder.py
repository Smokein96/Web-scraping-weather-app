import requests

def location_finder(city:str) :
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "city": city,
        "country": "India",
        "format": "json",
        "addressdetails": 1
    }

    headers = {
        "User-Agent": "WeatherApp/1.0"
    }

    try:
        resp = requests.get(url, params=params, headers=headers)
        resp.raise_for_status()
    except Exception as e:
        print(e)
        exit()
        
    data = resp.json()

    if not data:
        return None

    if " " in data[0]["address"]["state"]:

        parsed = data[0]["address"]["state"].replace(" ","-").lower()
        return parsed
    else:
        return data[0]["address"]["state"]  