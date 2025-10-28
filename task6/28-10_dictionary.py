d = {1: "Modulos", 2: "FEMPO", 3: "Estudiantes, Profesores"}
"""
for key, value in d.items():
    print("Key:", key, "Value:", value)

for key in d.keys():
    print(key)

for value in d.values():
    print(value)
"""
"""
d2 = {1: "IFC32A", 2: {"0484": "BBDD", "0483": "Programación"}}
print(d2)

print("Código del Módulo:", d2[2]["0484"])
print("Código del Módulo:", d2[2]["0483"])

d2 = {"course": "IFC32A", "subjects": {"0484": "BBDD", "0483": "Programación"}}

print("Codigo del Modulo:", d2["subjects"]["0484"])
print("Codigo del Modulo:", d2["subjects"]["0483"])
"""
d3 = {"name": "Ginés", "surname": "Garcia", "job": "Technician"}
"""valueName = d3.get("name")
valueSurname = d3.get("surname")
valueJob = d3.get("job")
print(valueName, valueSurname, valueJob)
print(d3.keys())"""

#retrieve last element and remove it from the dictionary
"""d3.pop("name")
print(d3)"""

"""for key in d3.keys():
    print(key, d3[key])"""