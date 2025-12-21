def is_repeated_half(s: str) -> bool:
    half = len(s) // 2
    return s[:half] == s[half:]


def subset_chek(s: str, k: int) -> str:
    i = 0
    while i + k < len(s):
        j = i + k
        if s[i:j] == s[j : j + k]:
            i += k
        else:
            return "no_match"
    return "match"


def check_repeated_in_subset(s: str) -> bool:
    for k in range(1, len(s)):
        if len(s) % k == 0:
            if subset_chek(s, k) == "match":
                return True
    return False


total = 0
with open("day2/input.txt") as file:
    for line in file:
        line = line.split(",")
        for part in line:
            [start_no, end_no] = map(int, part.split("-"))
            for i in range(start_no, end_no + 1):
                s = str(i)
                if check_repeated_in_subset(s):
                    total += i

print(total)
