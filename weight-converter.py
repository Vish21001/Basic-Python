weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit == "L" or unit == "l":
    converted_weight = float(weight) * 0.45
    print(f"You are {converted_weight} kilos")
elif unit == "K" or unit == "k":
    converted_weight = float(weight) / 0.45
    print(f"You are {converted_weight} pounds")
