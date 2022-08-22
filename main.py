from score import *
from config import config
import get_weather

# import weather
weather = get_weather.main()

def main(hourRanking):
    values = []
    for i in weather:
        values.append(scoreFunction(weather[i]["precipitation_amount"], weather[i]["cloud_area_fraction"]) * hourRanking[i])
    print("\nRating per time: ")
    print(values)
    x = sum(values)
    print("\nDagens rating er: ")
    print(x)
    return x