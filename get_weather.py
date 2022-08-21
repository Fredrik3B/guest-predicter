import requests
from datetime import datetime
from time import gmtime
import json

from read_data import get_weather_data
from db import read_db, write_db

DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"

sitename = "github.com/Fredrik3B/guest-predicter"
headers = {'user-agent': sitename}

lat, lon = 60.0770, 10.6588
url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"

def open_cache_json():
    print("Bruker cached datafil")
    with open("cache.json") as file:
        jsonfile = json.load(file)
    return jsonfile



def validate_resp(resp):
    print("Validerer response")
    if not resp.status_code == 304:
        if not resp.status_code == 200:
            if resp.status_code == 403:
                error_message = "Feil med User-Agent"
            elif resp.status_code == 429:
                error_message = "Throttling problemer. Fiks kreves for å ungå ban fra api"
            else:
                error_message = "Feil oppsto, bør sjekkes ut"
        
            return {"staus": "fail", "error_code": resp.status_code, "message": error_message}
        
        write_db(resp.headers.get("Expires"), resp.headers.get("Last-Modified"))

        jsondata = resp.json()
        with open("cache.json", "w") as file:
            json.dump(jsondata, file)
        return jsondata

    return open_cache_json()
    


def main():
    use_cached_data = read_db()
    print(use_cached_data)

    if use_cached_data:
        exp = datetime.strptime(use_cached_data[0], DATE_FORMAT)
        if not exp.timetuple() < gmtime():
            get_weather_data(open_cache_json())
            return
        headers["If-Modified-Since"] = use_cached_data[1]
        
    response = requests.get(url, headers=headers)
    validation = validate_resp(response)
    if isinstance(validation, dict):
        return validation

    get_weather_data(validation)
    
    

if __name__ == "__main__":
    main()