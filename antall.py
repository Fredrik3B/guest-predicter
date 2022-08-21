def antall(score):
    antall = 0.0000016025641*score**4 - 0.0007468919969*score**3 + 0.1116987179487*score**2 - 2.6855089355089*score + 37.4999999999999
    antall = round(antall)
    return antall

def dag(dag):
    antallMennesker = antall(70)*dag
    return antallMennesker

print(dag(0.3))