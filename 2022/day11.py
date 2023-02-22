from pathlib import Path

with open(Path(__file__).parent / "input/input_11.txt", "r") as f:
    monkeys = f.readlines()

count = 1

for line in monkeys:
    if line == "\n":
        count += 1

for i in range(len(monkeys)):
    monkeys[i] = monkeys[i].replace(",", "").lstrip(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz:=").removesuffix("\n")
    monkeys[i] = monkeys[i].split(" ")
    for j in range(len(monkeys[i])):
        try:
            if "old" in monkeys[i][j]:
                monkeys[i][j] = 2
                if "*" in monkeys[i][j-1]:
                    monkeys[i][j-1] = "**"
                elif "+" in monkeys[i][j-1]:
                    monkeys[i][j-1] = "*"
            monkeys[i][j] = int(monkeys[i][j])
        except:
            pass

class Monkey:
    def __init__(self):
        self.index = int
        self.items = []
        self.operation = []
        self.divider = []
        self.throw = []
        self.inspected = 0
    
    def __str__(self):
        return (f"Monkey {self.index}:\n"
                f"Items held: {self.items}\n"
                f"Operation: new = old {self.operation[0]} {self.operation[1]}\n"
                f"Test: divisible by {self.divider}\n"
                f"If true: throw to monkey {self.throw[0]}\n"
                f"If false: throw to monkey {self.throw[1]}\n"
                f"Currently inspected {self.inspected} objects")
    
    def __int__(self):
        return self.inspected

    def inspect(self, relax = True):
        for i in range(len(self.items)):
            for j in range(count):
                exec(f"self.items[0][j] {self.operation[0]}= {self.operation[1]}")
                if relax == False:
                    exec(f"self.items[0][j] %= {self.divider[j]}")
            if relax == True:
                for n in range(count):
                    self.items[0][n] = int(self.items[0][n]/3)
            div = iszero(self.items[0][self.index] % self.divider[self.index])
            exec(f"monkey{self.throw[div]}.items.append(self.items[0])")
            self.items.pop(0)
            self.inspected += 1

def iszero(x):
    if x == 0:
        return 1
    else:
        return 0

for i in range(count):
    var = "monkey"+str(i)
    vars()[var] = Monkey()
    vars()[var].index = i
    vars()[var].items.extend(monkeys[7*i+1])
    for n in range(len(vars()[var].items)):
        item = vars()[var].items[n]
        vars()[var].items[n] = []
        for m in range(count):
            vars()[var].items[n].append(item)
    vars()[var].operation.extend(monkeys[7*i+2])
    for j in range(count):
        vars()[var].divider.extend(monkeys[7*j+3])
    vars()[var].throw.extend(monkeys[7*i+5])
    vars()[var].throw.extend(monkeys[7*i+4])

for i in range(20):
    for j in range(count):
        exec("monkey%d.inspect()" % (j))

relaxed = []

for i in range(count):
    relaxed.append(vars()["monkey"+str(i)].inspected)

relaxed = sorted(relaxed, reverse = True)
mb_relax = relaxed[0]*relaxed[1]

# Part two - hard mode, long simulation

for i in range(count):
    var = "monkey"+str(i)
    vars()[var].items = []
    vars()[var].items.extend(monkeys[7*i+1])
    for n in range(len(vars()[var].items)):
        item = vars()[var].items[n]
        vars()[var].items[n] = []
        for m in range(count):
            vars()[var].items[n].append(item)
    vars()[var].inspected = 0

for i in range(10000):
    print(f"Round {i+1}")
    for j in range(count):
        exec("monkey%d.inspect(False)" % (j))

stressed = []

for i in range(count):
    stressed.append(vars()["monkey"+str(i)].inspected)

stressed = sorted(stressed, reverse = True)
mb_stress = stressed[0]*stressed[1]

# Print results

print("Monkey business after 20 rounds of keep away:", mb_relax)
print("Monkey business after 10 000 rounds of keep away:", mb_stress)