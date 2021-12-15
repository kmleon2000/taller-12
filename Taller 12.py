def simular_semiparabolico(Vo,Yo):
    Xo = 0
    t = 0
    g = 9.8

    coords = []

    while (Yo - (1/2 * g* (t**2))) >= 0:
        
        xcoord = round(Xo + Vo * t,2)                 # x(t) = Xo + Vo * t
        ycoord = round(Yo - (1/2 * g* (t**2)),2)      # y(t) = Yo - 1/2(g * (t**2))
        coords.append((xcoord,ycoord))
        t += 0.2

    return coords

data = simular_semiparabolico(100,400)

print(data)