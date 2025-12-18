def is_repeated_half(s: str) -> bool:
    half = len(s) // 2
    return s[:half] == s[half:]

acc = 0
with open("day2/input.txt") as file:
    for line in file:
        line = line.split(',')
        for r in line:
            # [start_no, end_no] = r.split('-')
            # start_no= int(start_no)
            # end_no= int(end_no) +1
            [start_no, end_no] = map(int, r.split('-'))
            for i in range(start_no, end_no):
                s=str(i)
                if len(s)%2==0:
                    if is_repeated_half(s):
                        acc += i

print(acc)