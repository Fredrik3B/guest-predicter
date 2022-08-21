import requests

sitename = "github.com/Fredrik3B/guest-predicter"
headers = {'user-agent': sitename}

lat, lon = 60.0770, 10.6588
url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"

response = requests.get(url, headers=headers)
def validate_resp(resp):
    if not resp.status_code == "200":
        if resp.status_code == "403":
            error_message = "Feil med User-Agent"
        elif resp.status_code == "429":
            error_message = "Throttling problemer. Fiks kreves for å ungå ban fra api"
        else:
            error_message = "Feil oppsto, bør sjekkes ut"
        return {"staus": "fail", "error_code": resp.status_code, "message": error_message}


    
