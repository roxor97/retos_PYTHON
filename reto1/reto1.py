var_1= float(input())
var_2= float(input())
if (var_1 < 80):
    if (var_2 < 60):
        print("Hipotension")
elif (var_1 >= 80 and var_1 <120):
    if (var_2 >= 60 and var_2 <80):
        print("Optimo")
elif (var_1>=120 and var_1<130):
    if (var_2>=80 and var_2<85):
        print("Normal Alerta Verde")
elif (var_1>=130 and var_1<140):
    if (var_2>=85 and var_2<90):
        print("normal alta")
elif (var_1>=140 and var_1<160):
    if (var_2>=90 and var_2<100):
        print("Hipertension grado 1")
    elif (var_1>=140):
        if (var_2<90):
            print("Hipertension Sistolica Aislada Alerta Naranja")
elif (var_1 >= 160 and var_1<180):
    if (var_2>=100 and var_2<110):
        print("Hipertension grado 2")
elif (var_1>=180):
    if (var_2>=110):
        print("Hipertension Grado 3 Alerta Roja")
    elif (var_1>=180):
        if(var_2<110):
            print("No se puede determinar la categoria Alerta Gris")
else:
    print("ingrese los datos otra vez")