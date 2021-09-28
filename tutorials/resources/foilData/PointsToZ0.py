import re
f1 = open('Ka4-70_0725','r')
f = open ('Ka4-70_0.4_new', 'w')
RezNumb1 = []
temp1 = f1.read()
result1 = temp1.split('\n')
print(result1)
Xrez1 =[]
Yrez1 =[]
Zrez1 =[]
for elem in result1:
    PrRezNumb1 = str(elem.split(' '))
    RezNumb1 = re.findall(r'-*\d+[\.]*[\w+]*\S+',PrRezNumb1)
    print(RezNumb1)
    if (len(RezNumb1)==3):
        FirstNumb1 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*',RezNumb1[0])
        for elem in FirstNumb1:
            Xrez1.append(elem)
        SecNumb1 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb1[1])
        for elem in SecNumb1:
            Yrez1.append(elem)
        ThrNumb1 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb1[2])
        for elem in ThrNumb1:
            Zrez1.append(elem)
f.write(str('(')+'\n')
#print(len(Xrez1))
#print(len(Yrez1))
#print(len(Zrez1))
for p in range(0, len(Xrez1)):
    f.write('(' +Xrez1[p] + ' ' + Yrez1[p] + ' ' + Zrez1[p] + ')' + '\n')
f.write(str(')')+'\n')
f1.close()