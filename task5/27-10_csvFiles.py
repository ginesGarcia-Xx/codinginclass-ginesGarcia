# create a CSV file from a table (list of lists) with data

#lista de listas
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
"""
with open("mobile_apps_research.csv", "w", encoding="utf-8") as f:
    for app in apps:
        line = ",".join(app)
        f.write(line + "\n")
    print("mobile_apps_dataset.csv created correctly")
"""
"""
with open("mobile_apps_dataset.csv", "r") as f:
    for line in f.readlines():
        print(line.strip())
"""
#read the csv file but as a table, row by row
tableR = []
with open("mobile_apps_dataset.csv", "r") as f:
    lines = f.readlines()
    for line in lines:
        row = line.strip().split(",")
        tableR.append(row)

#ex 1
#show just the id and the features separated by a space instead of ,
# and a dot instead of ;
"""
with open("mobile_apps_dataset.csv", "r") as f:
    for row in tableR:
        print(row[0], row[4].replace(";", "."))
"""
#ex 2
# show just the mobile apps for adults only
with open("mobile_apps_dataset.csv", "r") as f:
    for row in tableR[1:]:
        if int(row[2]) >= 18:
            print(row)