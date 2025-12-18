dial_position = 50
zero_count = 0

with open("day1/input.txt") as file:
    for line in file:
        direction = line[0]
        distance = int(line[1:])

        start = dial_position
        zero_count += distance // 100
        remaining = distance % 100

        if remaining > 0:
            if direction == "R":
                if start != 0 and start + remaining >= 100:
                    zero_count += 1
                dial_position = (start + remaining) % 100
            else:  # L
                if start != 0 and start - remaining <= 0:
                    zero_count += 1
                dial_position = (start - remaining) % 100
print(dial_position)
print(zero_count)