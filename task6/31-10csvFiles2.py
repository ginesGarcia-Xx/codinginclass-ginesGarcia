import csv

apps = [
    ["id", "AppName", "MinAge", "MaxAge", "Features"],
    ["1", "ChatMate", "13", "99", "messaging;stickers;voice calls"],
    ["2", "FitTrack", "12", "70", "fitness tracking;calorie counter;sleep monitor"],
    ["3", "BrainBoost", "7", "60", "puzzles;memory games;daily challenges"],
    ["4", "SafeBank", "18", "99", "secure login;fund transfers;budget analytics"],
    ["5", "HealthHub", "10", "80", "heart rate monitor;AI coach;diet tracking"],
    ["6", "LearnX", "6", "18", "interactive lessons;quizzes;progress tracking"],
    ["7", "EcoDrive", "16", "70", "eco tips;fuel monitor;route optimization"],
    ["8", "PhotoFix", "13", "99", "photo filters;AI enhancement;background remover"],
    ["9", "Budgetly", "18", "99", "expense tracker;reports;savings goals"],
    ["10", "MindEase", "10", "80", "meditation;sleep sounds;stress relief"]
]

#create csv file from the list of lists

filename = "mobile_apps_dataset2.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(apps)
print("Archivo CSV creado correctamente")

#read csv file from the filename
"""
filename = "mobile_apps_dataset2.csv"
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
"""
#part 3
"""
filename = "mobile_apps_dataset2.csv"
updated_rows = []
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if row[1] == "FitTrack":
            row[2] = 15
        updated_rows.append(row)
print(updated_rows)
#rewrite the file with updated info
with open(filename, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows([header] + updated_rows)
"""

#delete some info in csv file
filename = "mobile_apps_dataset2.csv"
kept_rows = []
with open(filename, "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    kept_rows.append(header)
    for row in reader:
        if row[1] != "PhotoFix":
            kept_rows.append(row)
print(kept_rows)