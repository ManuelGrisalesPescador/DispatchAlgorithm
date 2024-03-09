
OutTime = 0
FinishTime = 0

InTimes = [0,1,2,3]
Times = [4,2,6,4]

Ts = [InTimes[0]]
OutTime = 0
Tf = [Times[0]]

FinishTime = Times[0]
OutTime = Times[0]


Times.remove(Times[0])
InTimes.remove(InTimes[0])

InTimes = [x for _,x in sorted(zip(Times,InTimes))]
Times.sort()



TEspera = 0
TSistema = 0


for x in Times:
    #print(x)
    FinishTime += x
    Tf.append(FinishTime)  
    Ts.append(OutTime)
    OutTime += x
    
    
InTimes.insert(0,0)
Times.insert(0,0)
    
#print(Tf)
print(Times)
print(InTimes)
print(Ts)
#print(InTimes)

for Ts, InTime in zip(Ts,InTimes):
    #print(Ts, InTime)
    TEspera += (Ts - InTime)
    #print(TEspera)

TEspera = TEspera / len(InTimes)

print(TEspera)



for Tf, InTime in zip(Tf,InTimes):
    #print(Ts, InTime)
    TSistema += (Tf - InTime)
    #print(TEspera)

TSistema = TSistema / len(InTimes)

print(TSistema)
