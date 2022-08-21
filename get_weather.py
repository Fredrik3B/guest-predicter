import requests
from read_data import get_weather_data
from db import read_db, write_db

sitename = "github.com/Fredrik3B/guest-predicter"
headers = {'user-agent': sitename}

lat, lon = 60.0770, 10.6588
url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"

def validate_resp(resp):
    if not resp.status_code == 200:
        if resp.status_code == 403:
            error_message = "Feil med User-Agent"
        elif resp.status_code == 429:
            error_message = "Throttling problemer. Fiks kreves for å ungå ban fra api"
        else:
            error_message = "Feil oppsto, bør sjekkes ut"
     
        return {"staus": "fail", "error_code": resp.status_code, "message": error_message}
    
    write_db(resp.headers.get("Expires"), resp.headers.get("Last-Modified"))
    weather_data = get_weather_data(resp.json())


def main():

    use_cached_data = read_db()
    if not use_cached_data:
        response = requests.get(url, headers=headers)
        validate_resp(response)


if __name__ == "__main__":
    main()