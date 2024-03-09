Process = {'P1': [4, 0], 'P2': [2, 1], 'P3': [6, 2], 'P4': [4, 3]}

OutTime = 0
FisnishTime = 0

InTimes = [0,1,2,3]
Times = [4,2,6,4]

Ts = []
Tf = []

TEspera = 0
TSistema = 0

for x in Times:
    #print(x)
    FisnishTime += x
    Tf.append(FisnishTime)
    Ts.append(OutTime)
    OutTime += x
    
#print(Ts)
#print(Tf)

for Ts, InTime in zip(Ts,InTimes):
    TEspera += (Ts - InTime)

TEspera = TEspera / len(Times)

print(TEspera)

for Tf, InTime in zip(Tf,InTimes):
    #print(Tf, InTime)
    TSistema += (Tf - InTime)
    #print(TSistema)


TSistema = TSistema / len(InTimes)

print(TSistema)