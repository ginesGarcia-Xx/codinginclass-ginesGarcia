apps = [
    {
        "id": 1,
        "appName": "ChatMate",
        "minAge": 13,
        "maxAge": 99,
        "features": "messaging;stickers;voice calls"
    },
    {
        "id": 2,
        "appName": "FitTrack",
        "minAge": 12,
        "maxAge": 70,
        "features": "fitness tracking;calorie counter;sleep monitor"
    }
]
print(apps[0].keys())
headers = apps[0].keys()
with open("mobile_apps_dataset_dictionary.csv", "w") as f:
    f.write(",".join(headers) + "\n")

    #write each app data
    for app in apps:
        row = [str(app[key]) for key in headers]
        f.write(",".join(row) + "\n")