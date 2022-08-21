from score import *
from config import config
import get_weather



# import weather
weather = get_weather.main()

def main(hourRanking):
    values = []
    for i in weather:
        values.append(scoreFunction(weather[i]["cloud_area_fraction"], weather[i]["precipitation_amount"]) * hourRanking[i])
    x = sum(values)
    print(x)

main(config["lokasjon"]["kikut"]["time_ranking"])