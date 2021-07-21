c1 = 0
e1 = 0
e2 = 0
p1 = 0
p2 = 0
med1 = int(input())
med2 = int(input())
while 0 < med1 and med2 > 0:
    var_1 = float(input())
    var_2 = float(input())
    if (var_1 < 80 and var_1 >= 0):
        if (var_2 < 60 and var_2 >= 0):
            c1 = c1 + 1
            e2 = e2 + 1
            med2 = med2 - 5
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
            med1 = med1 - 2
        else:
            c1 = c1 + 1
    elif (var_1 >= 140 and var_1 < 160):
        if (var_2 >= 90 and var_2 < 100):
            c1 = c1 + 1
            e1 = e1 + 1
            med1 = med1 - 5
        elif (var_2 < 90):
            c1 = c1 + 1
            e1 = e1 + 1
            med1 = med1 - 20
        else:
            c1 = c1 + 1
    elif (var_1 >= 160 and var_1 < 180):
        if (var_2 >= 100 and var_2 < 110):
            c1 = c1 + 1
            e1 = e1 + 1
            med1 = med1 - 10
        elif (var_2 < 90):
            c1 = c1 + 1
            e1 = e1 + 1
            med1 = med1 - 20
        else:
            c1 = c1 + 1
    elif (var_1 >= 180):
        if (var_2 >= 110):
            c1 = c1 + 1
            e1 = e1 + 1
            med1 = med1 - 30
        elif (var_2 < 90):
            c1 = c1 + 1
            e1 = e1 + 1
            med1 = med1 - 20
        else:
            c1 = c1 + 1
if(c1>0):
    p1 = e1 / c1
    p2 = e2 / c1
    print(c1)
    print(f"{e1} {p1:.2%}")
    print(f"{e2} {p2:.2%}") 
else:
    print(0)
    print(f"{0} {0:.2%}")
    print(f"{0} {0:.2%}")