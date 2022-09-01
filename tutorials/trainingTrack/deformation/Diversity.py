import re
f1 = open('ImportDataDefault.txt','r')
f2 = open('ExportData.txt','r')
#fresx = open('pointDisplacementx_prev', 'w')
#fresy = open('pointDisplacementy_prev', 'w')
fresz = open('pointDisplacementz', 'w')
#f = open('resultzzzdontneed.txt','w')

RezNumb1 = []
temp1 = f1.read()
result1 = temp1.split('\n')
Xrez1 =[]
Yrez1 =[]
Zrez1 =[]

lines_index = []

with open("ImportDataDefault.txt", 'r', buffering=1, encoding="utf8") as f1:
    while f1.readline():
        lines_index.append(f1.tell())

    f1.seek(lines_index[int(result1[0])])
    temp2 = f1.read()
    result2 = temp2.split('\n')

    for elem in result2:
        PrRezNumb1 = str(elem.split(' '))
        RezNumb1 = re.findall(r'-*\d+[\.]*[\w+]*\S+', PrRezNumb1)
        if (len(RezNumb1) == 3):
            FirstNumb1 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb1[0])
            for elem in FirstNumb1:
                Xrez1.append(elem)
            SecNumb1 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb1[1])
            for elem in SecNumb1:
                Yrez1.append(elem)
            ThrNumb1 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb1[2])
            for elem in ThrNumb1:
                Zrez1.append(elem)
#f.write(result2[0]+'\n')
#for p in range(0,len(Zrez1)):
#    f.write(Zrez1[p] + '\n')


RezNumb2 = []
temp3 = f2.read()
result3 = temp3.split('\n')
Xrez2=[]
Yrez2=[]
Zrez2 =[]

for elem in result3:
    PrRezNumb2 = str(elem.split(' '))
    RezNumb2 = re.findall(r'-*\d+[\.]*[\w+]*\S+', PrRezNumb2)
    if (len(RezNumb2) == 3):
        FirstNumb2 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb2[0])
        for elem in FirstNumb2:
            Xrez2.append(elem)
        SecNumb2 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb2[1])
        for elem in SecNumb2:
            Yrez2.append(elem)
        ThrNumb2 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb2[2])
        for elem in ThrNumb2:
            Zrez2.append(elem)

print(len(Zrez1))
print(len(Zrez2))

Xrez3 = []
Yrez3 = []
Zrez3 = []

for p in range(0,len(Zrez1)):
    Rez1 = str(float(Xrez2[p]) - float(Xrez1[p]))
    Rez2 = str(float(Yrez2[p]) - float(Yrez1[p]))
    Rez3 = float(Zrez2[p]) - float(Zrez1[p])
    Rez3 = str("{:0.9f}".format(Rez3))

    Xrez3.append(Rez1)
    Yrez3.append(Rez2)
    Zrez3.append(Rez3)

#fresx.write(str(len(Xrez3))+'\n')
#fresx.write(str('(')+'\n')
#fresy.write(str(len(Yrez3))+'\n')
#fresy.write(str('(')+'\n')
fresz.write(str(len(Zrez3))+'\n')
fresz.write(str('(')+'\n')

for p in range(0,len(Zrez3)):
    #fresx.write(Xrez3[p] + '\n')
    #fresy.write(Yrez3[p] + '\n')
    fresz.write(Zrez3[p] + '\n')


#fresx.write(str(')')+'\n')
#fresy.write(str(')')+'\n')
fresz.write(str(')')+'\n')



