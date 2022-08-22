from main import *
from datetime import datetime

uke = { # [mandag: 0, tirsdag: 1...]
    0: 0.2,
    1: 0.2,
    2: 0.2,
    3: 0.2,
    4: 0.4,
    5: 0.95,
    6: 1,
}

def antall(score):
    antall = 0.0000016025641*score**4 - 0.0007468919969*score**3 + 0.1116987179487*score**2 - 2.6855089355089*score + 37.4999999999999
    antall = round(antall)
    return antall

def dag(dag):
    antallMennesker = antall(main(config["lokasjon"]["kikut"]["time_ranking"]))*dag
    antallMennesker = round(antallMennesker)
    print("\nForventet antall mennesker er:")
    return antallMennesker

print(dag(uke[datetime.today().weekday()]))
