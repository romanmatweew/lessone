room = input().split()


# Функция для определения этажа и подъезда
def find_floor_entrance(room):
    room_num = int(room[0])
    if len(room) > 1:
        entrance_num = int(room[1])
    else:
        entrance_num = None

    # Параметры дома
    num_floors = 8
    num_apartments_per_floor = 4
    num_entrances = 4

    # Определение подъезда
    if entrance_num:
        entrance = entrance_num
    else:
        entrance = (room_num - 1) // (num_floors * num_apartments_per_floor) + 1

    # Определение этажа
    room_num_in_entrance = room_num - (entrance - 1) * num_floors * num_apartments_per_floor
    floor = (room_num_in_entrance - 1) // num_apartments_per_floor + 1

    return floor, entrance


floor, entrance = find_floor_entrance(room)
print(floor, entrance)