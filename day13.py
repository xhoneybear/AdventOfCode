from pathlib import Path

with open(Path(__file__).parent / "input/input_13.txt", "r") as f:
    signals = f.readlines()

signal = [[]]
signal_ordered = []

n = 0

for i in range(len(signals)):
    try:
        temp = eval(signals[i])
        signal[n].append(temp)
        signal_ordered.append(temp)
    except:
        signal.append([])
        n += 1

signal_ordered.append([[2]])
signal_ordered.append([[6]])

def compare(list1, list2, index):
    global check
    if check == 0:
        if not type(list1) == type(list2):
            print("type mismatch. converting", list1, "or", list2, "to a list")
            if type(list1) == int:
                list1 = [list1]
            else:
                list2 = [list2]
            print(list1, list2)
        if type(list1) == list:
            try:
                if len(list2) > 0:
                    for i in range(len(list2)):
                        if check == 0:
                            compare(list1[i], list2[i], index)
                else:
                    if len(list1) > 0:
                        print("\033[34mList with index", index, "ran out of items!\033[0m")
                        print("\033[31mLeft side is bigger, not the right order\033[0m")
                        check = -1
            except IndexError:
                print("\033[34mList with index", index, "ran out of items!\033[0m")
                print(list1)
                print(list2)
                print(len(list1), len(list2))
                if len(list1) > len(list2):
                    print("\033[31mLeft side is bigger, not the right order\033[0m")
                    check = -1
                else:
                    print("\033[32mLeft side is smaller, the right order\033[0m")
                    check = 1
        else:
            print("Comparing", list1, "and", list2, "from list", index)
            if list1 > list2:
                print("\033[31mLeft side is bigger, not the right order\033[0m")
                check = -1
            elif list2 > list1:
                print("\033[32mLeft side is smaller, the right order\033[0m")
                check = 1

indices = []

for n in range(len(signal)):
    check = 0
    compare(signal[n][0], signal[n][1], n+1)
    if check == 1:
        if n+1 not in indices:
            print("Appending", n+1)
            indices.append(n+1)

to_sort = 1

while to_sort > 0:
    to_sort = 0
    for n in range(len(signal_ordered)-1):
        check = 0
        compare(signal_ordered[n], signal_ordered[n+1], n+1)
        if check != 1:
            temp = signal_ordered[n]
            signal_ordered[n] = signal_ordered[n+1]
            signal_ordered[n+1] = temp
            to_sort += 1

divider = 1
for i in range(len(signal_ordered)):
    if signal_ordered[i] == [[2]] or signal_ordered[i] == [[6]]:
        divider *= i+1

print("Sum of correctly aligned lists' indices:", sum(indices))
print("Score of dividing signals:", divider)