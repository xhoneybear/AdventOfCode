import re

def run(data):
    parts = 0
    gears = 0
    for i, line in enumerate(data):
        j = 0
        while j < len(line):
            if line[j].isdigit():
                number = ""
                start = (max(i - 1, 0), max(j - 1, 0))
                while j < len(line) and line[j].isdigit():
                    number += line[j]
                    j += 1
                end = (min(i + 2, len(data)), min(j + 1, len(line)))
                generator = (data[n][start[1]:end[1]] for n in range(start[0], end[0]))
                part = "".join(generator)
                part = re.sub(r"[0-9|\\.]", "", part)
                if part:
                    parts += int(number)
                continue
            elif line[j] == "*":
                nums = []
                if data[i][j - 1].isdigit():
                    nums.append(int(re.findall(r"[0-9]+", data[i][:j])[-1]))
                if data[i][j + 1].isdigit():
                    nums.append(int(re.findall(r"[0-9]+", data[i][j + 1:])[0]))
                for y in (i - 1, i + 1):
                    x = 0
                    while x < len(data[y]):
                        if data[y][x].isdigit():
                            start = x
                            while x < len(data[y]) and data[y][x].isdigit():
                                x += 1
                            end = x
                            if j in range(start - 1, end + 1):
                                nums.append(int(data[y][start:end]))
                        x += 1
                if len(nums) == 2:
                    gears += nums[0] * nums[1]
            j += 1
    print(parts)
    print(gears)
