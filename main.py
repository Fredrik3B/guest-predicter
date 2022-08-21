from score import *
# import weather
weather = {
    # Hele timer
    11: {
        [
        {"rainAmount": 0.1},
        {"caf": 30}
        ]
    },
    12: {
        [
        {"rainAmount": 0.3},
        {"caf": 50}
        ]
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