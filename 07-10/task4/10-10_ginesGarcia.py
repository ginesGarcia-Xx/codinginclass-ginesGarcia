#2.1 Count how many lines contain the word "APP".
"""
with open("mobile_apps-research.txt", "r") as f:
    count = 0
    for line in f.readlines():
        if line.__contains__("APP"):
            count += 1
print(f"Total number of lines containing the word APP: {count}")
"""
#2.2 Find how many times "data" appears in the entire file (case insensitive).
"""
with open("mobile_apps-research.txt", "r") as f:
    count = 0
    for line in f.readlines():
        if line.lower().__contains__("data"):
            count += 1
print(f"Total number of times 'data' appears in the file: {count}")
"""
#2.3Print the longest line.
"""with open("mobile_apps-research.txt", "r") as f:
    masLarga = ""
    for line in f.readlines():
        if len(masLarga) < len(line):
            masLarga = line
print(masLarga)"""
#2.4 Print the shortest line
"""with open("mobile_apps-research.txt", "r") as f:
    masCorta = f.readline()
    for line in f.readlines():
        if len(line) < len(masCorta):
            masCorta = line
print(masCorta)"""
#2.5 Count how many lines end with an exclamation mark !.
"""with open("mobile_apps-research.txt", "r") as f:
    count = 0
    for line in f.readlines():
        if line.strip().endswith("!"):
            print(line)
            count += 1
    print(f"Total number of lines ending with an exclamation mark: {count}")
"""
#2.6Find and print all lines that contain numbers.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        if any(ch.isdigit() for ch in line):
            print(line)"""
#2.7Extract all digits from each line and print them.
"""with open("mobile_apps-research.txt", "r") as f:
    numeros = []
    for line in f.readlines():
        for ch in line:
            if ch.isdigit():
                numeros.append(ch)
print(numeros)"""
