with open("../fitxer1.txt", "r") as f:
    count = 0
    for row in f.readlines():
        count += 1
        #print(f"{count}: {row.strip()}") ".strip" corta los espacios a los lados de la cadena
        #print(f"{count}: {row.strip(.upper}") ".upper" lo convierte todo a mayusculas
        #print(f"{count}: {row.strip(.capitalice}") ".capitalice" hace que la primera letra de la linea sea mayuscula
        #print(f"{count}: {row.strip(.title}") ".title" hace que la primera letra de cada palabra de la linea sea mayuscula
        print(f"{count}: {row.strip().upper()}") #una manera de imprimir aplicando el formato con la "f" al principio
        #print("Line {}: {}".format(count, row).upper().strip()) imprimiendo con ".format" en el que los {} hacen referencia a las varia bles dentro de ".format"
"""
age = 18
person = "Adult" if age >= 18 else "Child"
print(f"Edad: {age} Estado: {person}")
"""
age = 13
if age <= 12:
    print("Child")
elif 18 > age > 12:
    print("Teenager")
elif age >= 18:
    print("Adult")


