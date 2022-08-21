from score import *
from config import config
import json

# import weather
weather = {
    11: {
        "cloud_area_fraction": 0.5,
        "precipitation_amount": 70
    },
    12: {
        "cloud_area_fraction": 0.1,
        "precipitation_amount": 20
    },
    13: {
        "cloud_area_fraction": 0,
        "precipitation_amount": 0
    },
    14: {
        "cloud_area_fraction": 0,
        "precipitation_amount": 0
    },
    15: {
        "cloud_area_fraction": 0,
        "precipitation_amount": 0
    }
}

def main(hourRanking):
    values = []
    for i in weather:
        values.append(scoreFunction(weather[i]["cloud_area_fraction"], weather[i]["precipitation_amount"]) * hourRanking[i])
    x = sum(values)
    print(x)

main(config["lokasjon"]["kikut"]["time_ranking"])