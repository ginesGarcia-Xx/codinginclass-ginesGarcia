"""
file = open("fitxer1.txt", "r")


while contentFitxer:
    print(contentFitxer)
    contentFitxer = file.readline()
file.close()

while True:
    contentFitxer = file.readline()
    print(contentFitxer)
    if not contentFitxer:
        break
file.close()
"""
with open("fitxer1.txt" ,"r") as f:
    for line in f.readline():
        print(line)
f.close()