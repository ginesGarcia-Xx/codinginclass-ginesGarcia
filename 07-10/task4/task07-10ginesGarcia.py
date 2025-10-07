# 1.1 Print each line as it appears.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        print(line.strip())"""
# 1.2 Print line numbers along with each line.
"""
with open("mobile_apps-research.txt") as f:
    count = 0
    for line in f.readlines():
        count += 1
        print(f"{count}: {line.strip()}")
"""
# 1.3 Print lines which doesn t end with a dot
"""
with open("mobile_apps-research.txt") as f:
    for line in f.readlines():
        if not line.strip().endswith("."):
            print(line)
"""
# 1.4 Count and print the total number of lines.
"""with open("mobile_apps-research.txt", "r") as f:
    count = 0
    for line in f.readlines():
        count += 1
    print(f"Total number of lines: {count}")"""
# 1.5 Display only lines that start with a digit.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        if line.strip()[0].isdigit():
            print(line)"""
# 1.6 Display only lines that contain the word "mobile".
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        if line.__contains__("mobile"):
            print(line)"""
# 1.7 Convert each line to uppercase before printing.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        print(line.strip().upper())"""
# 1.8 Convert each line to lowercase before printing.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        print(line.strip().lower())"""
# 1.9 Print only the first 10 lines.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in range(10):
        print(f.readline().strip())"""
# 1.10 Print lines that contain the character @.
"""with open("mobile_apps-research.txt", "r") as f:
    for line in f.readlines():
        if line.__contains__("@"):
            print(line.strip())"""