
converters = [
    lambda t: t * 1000,                 
    lambda kg: kg * 1000,              
    lambda g: g * 1000,                 
    lambda mg: mg * 0.00000220462       
]
tonnes = float(input("Enter weight in tonnes: "))
kg = converters[0](tonnes)
gm = converters[1](kg)
mg = converters[2](gm)
lbs = converters[3](mg)
print("Weight conversions:")
print(f"{kg} kg")
print(f"{gm} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")