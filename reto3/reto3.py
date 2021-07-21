c1 = 0
e1 = 0
e2 = 0
p1 = 0
p2 = 0
n = 0
pa = 0
i=1
j=1
k=0
sur=0
medi=0
medicamentos=[]
medica=[]
pacientes=0
poscicion_mayor=0
poscicion_menor=0
porcentaje=0
total=0

while pacientes<=0 or sur<=0:
    tmp=input()
    datos=tmp.split()
    sur=int(datos[0])
    pacientes=int(datos[1])

for i in range(sur):
    medi=int(input())
    while medi<=0:
        medi=int(input())
    medicamentos.append(medi)
    medica.append(medi)
for j in range(pacientes):
    tnt=input()
    dat=tnt.split()
    surcur=int(dat[0])
    if surcur>0:
        var_1 = float(dat[1])
        var_2 = float(dat[2])
        if (var_1 < 80 and var_1 >= 0):
            if (var_2 < 60 and var_2 >= 0):
                c1 = c1 + 1
                e2 = e2 + 1
                medicamentos[surcur-1] = medicamentos[surcur-1] - 5
            else:
                c1 = c1 + 1
        elif (var_1 >= 80 and var_1 < 120):
            if (var_2 >= 60 and var_2 < 80):
                c1 = c1 + 1
            else:
                c1 = c1 + 1
        elif (var_1 >= 120 and var_1 < 130):
            if (var_2 >= 80 and var_2 < 85):
                c1 = c1 + 1
            else:
                c1 = c1 + 1
        elif (var_1 >= 130 and var_1 < 140):
            if (var_2 >= 85 and var_2 < 90):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1] = medicamentos[surcur-1] - 2
            else:
                c1 = c1 + 1
        elif (var_1 >= 140 and var_1 < 160):
            if (var_2 >= 90 and var_2 < 100):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1] = medicamentos[surcur-1] - 5
            elif (var_2 < 90):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1] = medicamentos[surcur-1] - 20
            else:
                c1 = c1 + 1
        elif (var_1 >= 160 and var_1 < 180):
            if (var_2 >= 100 and var_2 < 110):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1] = medicamentos[surcur-1] - 10
            elif (var_2 < 90):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1] = medicamentos[surcur-1] - 20
            else:
                c1 = c1 + 1
        elif (var_1 >= 180):
            if (var_2 >= 110):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1] = medicamentos[surcur-1] - 30
            elif (var_2 < 90):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1] = medicamentos[surcur-1] - 20
            else:
                c1 = c1 + 1
    else:
        pass
menor=medicamentos[0]
mayor=medicamentos[0]
for x in range(sur):
    if (medicamentos[x]>mayor):
        mayor=medicamentos[x]
        poscicion_mayor=x+1
    elif (medicamentos[x]<menor):
        menor=medicamentos[x]
        poscicion_menor=x+1

print(f"{poscicion_menor} {min(medicamentos)}")
print(f"{poscicion_mayor} {max(medicamentos)}")
for k in range(sur):
    porcentaje=(medicamentos[k]*100)/medica[k]
    total=100-porcentaje
    print(f"{k+1} {total:.2f}%")
