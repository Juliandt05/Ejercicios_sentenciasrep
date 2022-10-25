letra=str
while letra!=" ":
    letra=str(input("Dime un caracter en minuscula"))
    if letra=="a"or letra=="e"or letra=="i"or letra=="o"or letra=="u":
        print("Vocal")
    else:
        print("No Vocal")