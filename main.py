from score import *
import requests
import json

# import weather
weather = {
    "2022-08-21T20:38:56Z": {
        "cloud_area_fraction": 0.0,
        "precipitation_amount": 0.0
    }
}
    
HOUR_RANKING_KIKUT = {11: 5, 12: 25, 13: 35, 14: 25, 15: 10}

def main(hourRanking):
    hourValue = []
    for i in hourRanking:
        hourValue.append(hourRanking[i]/100)
    values = []
    for value in hourValue:
        for condition in weather:
            values.append(scoreFunction(weather, 40) * value)
    print(values)
    x = sum(values)
    print(x)

main(HOUR_RANKING_KIKUT)