
import csv
from matplotlib import pyplot

tjenesteroboter = []
serviceroboter = []

naeringProsent2022 = []
naeringer = []


with open("roboter.csv") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifteer = next(filinnhold)

    for rad in filinnhold:
        if rad[1] not in naeringer:
            naeringer.append(rad[1])

        if rad[0] == "Alle sysselsette":
            tjenesteroboter.append([rad[1],int(rad[2]),int(rad[4]),int(rad[4])-int(rad[2])])
            serviceroboter.append([rad[1],int(rad[5]),int(rad[7]),int(rad[7])-int(rad[5])]) 
        else:
            """
            antallSysselsatte = 0
            if rad[0] == "10-19 sysselsette":
                antallSysselsatte = 15
            elif rad[0] == "20-49 sysselsette":
                antallSysselsatte = 35
            """

            naeringProsent2022.append([rad[1],int(rad[4])])

    tjenesteroboter.sort(key=lambda x: -x[3]) # , reverse = True hadde også invertert
 
    #print("De tre næringene som har størt prossentvis økning: ",tjenesteroboter[:3])
    """
    for i in range (3):
        print(tjenesteroboter[i][0])
        print(tjenesteroboter[i][1])
        print(tjenesteroboter[i][2])
    """
    #print(naeringer)

print(len(naeringProsent2022))

pyplot.figure(figsize=(6,20))
x = [15,35,75,100]

def plotNaering(naering):
    y = []
    for rad in naeringProsent2022:
        if rad[0] == naering:
            y.append(rad[1])
    pyplot.plot(x,y,label=str(naering))
    
pyplot.xlabel("Antall sysselsatte")
pyplot.ylabel("Tjenesteroboter i prosent 2022")


for naering in naeringer:
    plotNaering(naering)

pyplot.legend(prop = { "size": 7 })
pyplot.show()



#basert på år
#basert på næringen
#basert på sysselsette 
#basert på tjenesteroboter vs serviceroboter






