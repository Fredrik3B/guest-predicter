from score import *
# import weather
weather = {
    # Hele timer
    "2022-08-21": {
        11: {
            [
            {"precipitation_amount": 0.1},
            {"cloud_area_fraction": 30}
            ]
        },
        12: {
            [
            {"precipitation_amount": 0.3},
            {"cloud_area_fraction": 50}
            ]
        },
        # ...
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