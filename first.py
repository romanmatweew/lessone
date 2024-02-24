def find_floor_entrance(apartment_num, floors=8, entrances=4, apartments_per_floor=8):
    apartments_per_entrance = floors * apartments_per_floor
    entrance_num = (apartment_num - 1) // apartments_per_entrance + 1
    apartment_num_within_entrance = (apartment_num - 1) % apartments_per_entrance + 1
    floor_num = (apartment_num_within_entrance - 1) // apartments_per_floor + 1
    return floor_num, entrance_num

room = int(input("Введите номер квартиры: "))
floor, entrance = find_floor_entrance(room)
print("Этаж:", floor)
print("Подъезд:", entrance)