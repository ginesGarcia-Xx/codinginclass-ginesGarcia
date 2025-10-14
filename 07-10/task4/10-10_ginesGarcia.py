import re
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
#2.8Count how many total characters are in the file.
"""with open("mobile_apps-research.txt", "r") as f:
    count = 0
    for line.strip() in f.readlines():
        for ch in line:
            count += 1
print(f"Total number of characters: {count}")"""
#2.9Count how many total words are in the file.
"""with open("mobile_apps-research.txt", "r") as f:
    count = 0
    for line in f.readlines():
        count += len(line.strip().split())
print(f"Total number of words: {count}")"""
#2.10 Print lines with more than 10 words.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        if len(line.split()) > 10:
            print(line.strip())"""
#3.1Replace "APP" with "APPLICATION" in every line and print the result.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        print(line.replace("APP", "APPLICATION").strip())"""
#3.2Replace special characters like @, &, —, and ↔ with spaces.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        nuevaLinea = line.replace("@", " ").replace("&", " ").replace("—", " ").replace("↔", " ").strip()
        print(nuevaLinea)"""

"""import re

with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        nuevaLinea = re.sub(r"[@&—↔]", "", line)
        print(nuevaLinea.strip())"""
#3.3Reverse each line’s text.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        print(line.strip()[::2])"""  #el [::-1] indica que se imprima del reves. si pusiera [::2] imprimiria un caracter de cada 2. si pongo "hola" imprimiria "hl"
#3.4Capitalize only the first word of each line.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        print(line.capitalize())"""
#3.5Print each line but highlight (uppercase) the word "security".
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        print(line.lower().replace("security", "SECURITY").strip())"""
#3.6Remove all numbers from the lines.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        print(re.sub(r"\d", "")) #el 'r"d"' reemplaza todos los digitos. y los sustituye por "" """
#3.7Replace all occurrences of "mobile" with "MOBILE".
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        print(line.replace("mobile", "MOBILE").strip())"""
#3.8Print each line without punctuation.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        if not line.strip().endswith("."):
            print(line)"""
#3.9Print only the words that are longer than 5 letters.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        for word in line.strip().split():
            if len(word) > 5:
                print(word)"""
#3.10 Print lines with words sorted alphabetically.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        print(sorted(line.strip().split()))"""