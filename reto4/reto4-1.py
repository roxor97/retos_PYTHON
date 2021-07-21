c1 = 0
e1 = 0
e2 = 0
p1 = 0
p2 = 0
n = 0
pa = 0
sur=0
k_medica=0
medi=0
medicamentos=[]
comp=[]
pacientes=0
poscicion_mayor=0
sur_mayor=0
poscicion_menor=0
sur_menor=0
porcentaje=0
total=0
pacient=[]
medica=[]
medica2=[]
while pacientes<=0 or sur<=0 or k_medica<=0:
    tmp=input()
    datos=tmp.split()
    sur=int(datos[0])
    pacientes=int(datos[2])
    k_medica=int(datos[1])

for i in range(sur):
    datos = list(map(int, input().split()))
    medicamentos.append(datos)

for i in range(sur):
    comp.append([0]*k_medica)
for i in range(sur):
    for j in range(k_medica):
        comp[i][j]=medicamentos[i][j]


for i in range(sur):
    pacient.append([0]*1)
for i in range(sur):
    medica.append([0]*k_medica)
for i in range(sur):
    medica2.append([0]*k_medica)
for j in range(pacientes):
    tnt=input()
    dat=tnt.split()
    surcur=int(dat[0])
    t_medi=int(dat[1])
    existencias=int(dat[2])
    
    if surcur>0:
        var_1 = float(dat[3])
        var_2 = float(dat[4])
        if (var_1 < 80 and var_1 >= 0):
            if (var_2 < 60 and var_2 >= 0):
                c1 = c1 + 1
                e2 = e2 + 1
                medicamentos[surcur-1][t_medi-1] = medicamentos[surcur-1][t_medi-1] - existencias
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
                medica2[surcur-1][t_medi-1]=existencias
                if(t_medi==1 and medica[surcur-1][0]<=existencias):
                    medica[surcur-1][0]=existencias
                if(t_medi==1 and medica2[surcur-1][0]>=existencias):
                    medica2[surcur-1][0]=existencias
            else:
                c1 = c1 + 1
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
        elif (var_1 >= 80 and var_1 < 120):
            if (var_2 >= 60 and var_2 < 80):
                c1 = c1 + 1
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
            else:
                c1 = c1 + 1
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
        elif (var_1 >= 120 and var_1 < 130):
            if (var_2 >= 80 and var_2 < 85):
                c1 = c1 + 1
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
            else:
                c1 = c1 + 1
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
        elif (var_1 >= 130 and var_1 < 140):
            if (var_2 >= 85 and var_2 < 90):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1][t_medi-1] = medicamentos[surcur-1][t_medi-1] - existencias
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
                medica2[surcur-1][t_medi-1]=existencias
                if(t_medi==1 and medica[surcur-1][0]<=existencias):
                    medica[surcur-1][0]=existencias
                if(t_medi==1 and medica2[surcur-1][0]>=existencias):
                    medica2[surcur-1][0]=existencias
            else:
                c1 = c1 + 1
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
        elif (var_1 >= 140 and var_1 < 160):
            if (var_2 >= 90 and var_2 < 100):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1][t_medi-1] = medicamentos[surcur-1][t_medi-1] - existencias
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
                medica2[surcur-1][t_medi-1]=existencias
                if(t_medi==1 and medica[surcur-1][0]<=existencias):
                    medica[surcur-1][0]=existencias
                if(t_medi==1 and medica2[surcur-1][0]>=existencias):
                    medica2[surcur-1][0]=existencias
            elif (var_2 < 90):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1][t_medi-1] = medicamentos[surcur-1][t_medi-1] - existencias
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
                medica2[surcur-1][t_medi-1]=existencias
                if(t_medi==1 and medica[surcur-1][0]<=existencias):
                    medica[surcur-1][0]=existencias
                if(t_medi==1 and medica2[surcur-1][0]>=existencias):
                    medica2[surcur-1][0]=existencias
            else:
                c1 = c1 + 1
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
        elif (var_1 >= 160 and var_1 < 180):
            if (var_2 >= 100 and var_2 < 110):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1][t_medi-1] = medicamentos[surcur-1][t_medi-1] - existencias
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
                medica2[surcur-1][t_medi-1]=existencias
                if(t_medi==1 and medica[surcur-1][0]<=existencias):
                    medica[surcur-1][0]=existencias
                if(t_medi==1 and medica2[surcur-1][0]>=existencias):
                    medica2[surcur-1][0]=existencias
            elif (var_2 < 90):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1][t_medi-1] = medicamentos[surcur-1][t_medi-1] - existencias
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
                medica2[surcur-1][t_medi-1]=existencias
                if(t_medi==1 and medica[surcur-1][0]<=existencias):
                    medica[surcur-1][0]=existencias
                if(t_medi==1 and medica2[surcur-1][0]>=existencias):
                    medica2[surcur-1][0]=existencias
            else:
                c1 = c1 + 1
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
        elif (var_1 >= 180):
            if (var_2 >= 110):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1][t_medi-1] = medicamentos[surcur-1][t_medi-1] - existencias
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
                medica2[surcur-1][t_medi-1]=existencias
                if(t_medi==1 and medica[surcur-1][0]<=existencias):
                    medica[surcur-1][0]=existencias
                if(t_medi==1 and medica2[surcur-1][0]>=existencias):
                    medica2[surcur-1][0]=existencias
            elif (var_2 < 90):
                c1 = c1 + 1
                e1 = e1 + 1
                medicamentos[surcur-1][t_medi-1] = medicamentos[surcur-1][t_medi-1] - existencias
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
                medica2[surcur-1][t_medi-1]=existencias
                if(t_medi==1 and medica[surcur-1][0]<=existencias):
                    medica[surcur-1][0]=existencias
                if(t_medi==1 and medica2[surcur-1][0]>=existencias):
                    medica2[surcur-1][0]=existencias
            else:
                c1 = c1 + 1
                pacient[surcur-1][0]=pacient[surcur-1][0]+1
    else:
        pass


menor=medicamentos[0][0]
mayor=[0][0]
posicion_mayor=0
posicion_menor=0
sur_mayor=0
sur_menor=0
minimo=0
dif=0
total_dif=0
exis_min=0
prom=0
prom2=0
difer=0
s=0
for i in range(sur):
    print(i+1)
    for x in range(k_medica):
        if (medicamentos[i][x]>=mayor):
            mayor=medicamentos[i][x]
            posicion_mayor=x+1
            sur_mayor=i+1
        if (medicamentos[i][x]<=menor):
            menor=medicamentos[i][x]
            posicion_menor=x+1
            sur_menor=i+1
        if(medicamentos[i][x]==comp[i][x]):
            exis_min=0
        if(medicamentos[i][x]<comp[i][x]):
            dif=comp[i][x]-medicamentos[i][x]
            total_dif=total_dif+dif
            if(difer<=dif):
                difer=dif
    if (pacient[i][0]>0):
        prom2=total_dif/pacient[i][0]
    if (pacient[i][0]==0):
        prom2=0
    prom=total_dif/k_medica
    print(f"{posicion_menor} {menor}")
    print(f"{posicion_mayor} {mayor}")
    print(f"{exis_min:.2f} {prom:.2f} {difer:.2f} ")
    print(f"{prom2:.2f}")
    difer=0
    mayor=0
    dif=0
    prom=0
    exis_min=0
    total_dif=0
    prom2=0
    menor=10000000

for i in range (sur):
    if(medica[i][0]>=mayor):
        mayor=medica[i][0]
        sur_mayor=i+1
    if(medica2[i][0]<=menor):
        menor=medica2[i][0]
        if(s>=i):
            menor=medica2[i][0]
            sur_menor=i+1
print(f"{sur_menor} {menor}")
print(f"{sur_mayor} {mayor}")
