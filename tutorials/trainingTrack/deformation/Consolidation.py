#!/usr/bin/env python
import re
f1 = open('faces', 'r') # file about triangles
f2 = open('points','r') # file about nodes
#f3 = open('wallShearStressMean','r') # file about Sigmas
#f4 = open('pMean','r') # file about Pressure
f3 = open('wallShearStress','r') # file about Sigmas
f4 = open('p','r') # file about Pressure
f = open('ImportData.txt', 'w')
#f11 = open('res.txt', 'w')
#f12 = open('resss.txt', 'w')
#ft= open('testfile.txt', 'w')
RezNumb1 = []
temp1 = f1.read()
result1 = temp1.split('\n')
Xrez1 =[]
Yrez1 =[]
Zrez1 =[]
for elem in result1:
    PrRezNumb1 = str(elem.split(' '))
    RezNumb1 = re.findall(r'\w+',PrRezNumb1)
    if (len(RezNumb1)==4):
        FirstNumb1 = re.findall(r'\d+',RezNumb1[1])
        for elem in FirstNumb1:
            Xrez1.append(elem)
        SecNumb1 = re.findall(r'\d+', RezNumb1[2])
        for elem in SecNumb1:
            Yrez1.append(elem)
        ThrNumb1 = re.findall(r'\d+', RezNumb1[3])
        for elem in ThrNumb1:
            Zrez1.append(elem)

f.write(result1[1]+'\n')
for p in range(0,len(Xrez1)):
    f.write(Xrez1[p] + ' ' + Yrez1[p] + ' ' + Zrez1[p] + '\n')

f1.close()

RezNumb2 = []
temp2 = f2.read()
result2 = temp2.split('\n')
Xrez2 =[]
Yrez2 =[]
Zrez2 =[]
for elem in result2:
    PrRezNumb2 = str(elem.split(' '))
    RezNumb2 = re.findall(r'-*\d+[\.]*[\w+]*\S+',PrRezNumb2)
    if (len(RezNumb2)==3):
        FirstNumb2 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*',RezNumb2[0])
        for elem in FirstNumb2:
            Xrez2.append(elem)
        SecNumb2 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb2[1])
        for elem in SecNumb2:
            Yrez2.append(elem)
        ThrNumb2 = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb2[2])
        for elem in ThrNumb2:
            Zrez2.append(elem)
f.write(result2[1]+'\n')
#print(len(Xrez2))
#print(len(Yrez2))
#print(len(Zrez2))
for p in range(0, len(Xrez2)):
    f.write(Xrez2[p] + ' ' + Yrez2[p] + ' ' + Zrez2[p] + '\n')
f2.close()

RezNumb = []
temp = f3.read()
result = temp.split('\n')
Xrez =[]
Yrez =[]
Zrez =[]
for elem in result:
    PrRezNumb = str(elem.split(' '))
    RezNumb = re.findall(r'-*\d+[\.]*[\w+]*\S+',PrRezNumb)
    #print(RezNumb)
    if (len(RezNumb)==3):
        FirstNumb = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*',RezNumb[0])
        #FirstNumby = FirstNumb[0].replace('e','*10E')
        #print(float(FirstNumb[0]))
        FirstNumb[0] = (float(FirstNumb[0]) * -10000)
        FirstNumb[0] = str("{:0.9f}".format(FirstNumb[0]))
        for elem in FirstNumb:
            Xrez.append(elem)
        SecNumb = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb[1])
        SecNumb[0] = (float(SecNumb[0]) * -10000)
        SecNumb[0] = str("{:0.9f}".format(SecNumb[0]))
        for elem in SecNumb:
            Yrez.append(elem)
        ThrNumb = re.findall(r'-*\d+[\.]*[\d+]*[\w+\-\d+]*', RezNumb[2])
        ThrNumb[0] = str(float(ThrNumb[0]) * -10000)
        for elem in ThrNumb:
            Zrez.append(elem)

#f.write(result[1]+'\n')
for p in range(0,len(Xrez)):
    f.write(Xrez[p] + '\n')
#f.write(result[1]+'\n')
for p in range(0,len(Yrez)):
    f.write(Yrez[p] + '\n')
#f.write(result[1]+'\n')
#for p in range(0,len(Zrez)):
 #   f.write(Zrez[p] + '\n')

print(len(Xrez))
print(len(Yrez))

f3.close()

RezNumb3 = []
temp3 = f4.read()
result3 = temp3.split('\n')
Xrez3 =[]
Yrez3 =[]
Zrez3 =[]
for elem in result3:
    PrRezNumb3 = str(elem.split(' '))
    RezNumb3 = re.findall(r'-*\d+\.\w+\S+',PrRezNumb3)
    #print(RezNumb2)
    if (len(RezNumb3)==1):
        FirstNumb3 = re.findall(r'-*\d+\.[\d+]*[\w+\-\d+]*',RezNumb3[0])
        FirstNumb3[0] = (float(FirstNumb3[0]) * 10000)
        FirstNumb3[0] = str("{:0.9f}".format(FirstNumb3[0]))
        #print(FirstNumb2)
        # pattern = compile('^[^\\.\\s][-a-z0-9_.]+@([-a-z0-9]+\\.)+[a-z]{2,6}(\\s|$)')\n"
        for elem in FirstNumb3:
            Xrez3.append(elem)
#f.write(result[1]+'\n')
for p in range(0,len(Xrez3)):
     f.write(Xrez3[p] + '\n')
f4.close()

f.close()
