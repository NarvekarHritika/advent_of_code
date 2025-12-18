def shift_dail_to_left(dail_position, distance):
    return dail_position - distance

def shift_dail_to_right(dail_position, distance):
    return dail_position + distance

dail_position=50
count_for_dail_at_0=0
with open("day1/input.txt") as file:
    for input in file:
        input = input.rstrip()
        distance = int(input[1:]) %100
        if input[0] == "L":
            dail_position = shift_dail_to_left(dail_position, distance)
        else:
            dail_position = shift_dail_to_right(dail_position, distance)
        dail_position=dail_position %100

        if dail_position == 0:
            count_for_dail_at_0 = count_for_dail_at_0 +1
       
print(dail_position)
print(count_for_dail_at_0)

