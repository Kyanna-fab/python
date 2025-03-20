weight = float(input("Weight:"))
unit =input("(K)g or (L)bs:")

if unit.upper()=="K":
    coverted =weight / 0.45
    print("Weight in (L)bs: " + str(coverted))
else :
    unit.upper() == "L"
    coverted = weight * 0.45
    print("Weight in (K)g: " + str(coverted))


