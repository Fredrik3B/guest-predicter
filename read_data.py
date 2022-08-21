from dateutil.parser import isoparse

start_time = 11
stop_time = 16

def get_weather_data(jsondata):
    cleaned_data = {}
    data = jsondata["properties"]["timeseries"]
    for hour in data:
        time = isoparse(hour["time"])
        if time.hour >= start_time and time.hour < stop_time:
            if hour["data"].get("next_1_hours"):
                cleaned_data[time.hour] = {
                    "cloud_area_fraction": hour["data"]["instant"]["details"]["cloud_area_fraction"],
                    "precipitation_amount": hour["data"]["next_1_hours"]["details"]["precipitation_amount"]
                }
            
    return cleaned_data
        
