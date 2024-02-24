melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni': 1455, 'Si': 1415, 'Be': 1287}
element1, element2 = input().split()
temperature_difference = abs(melt[element1] - melt[element2])
print(temperature_difference)