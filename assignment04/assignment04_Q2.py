
km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
ft_to_in = lambda ft: ft * 12
in_to_cm = lambda inch: inch * 2.54
def distance_converter(distance, conversion_type, func):
    result = func(distance)
    print(f"{distance} {conversion_type.split(' to ')[0]} = {result} {conversion_type.split(' to ')[1]}")
distance = int(input("Enter distance value: "))
print("\nConversions:\n")
distance_converter(distance, "km to m", km_to_m)
distance_converter(distance, "m to cm", m_to_cm)
distance_converter(distance, "cm to mm", cm_to_mm)
distance_converter(distance, "ft to in", ft_to_in)
distance_converter(distance, "in to cm", in_to_cm)