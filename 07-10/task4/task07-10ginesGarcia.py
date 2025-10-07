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

# 1.5 Display only lines that start with a digit.
# 1.6 Display only lines that contain the word "mobile".
# 1.7 Convert each line to uppercase before printing.
# 1.8 Convert each line to lowercase before printing.
# 1.9 Print only the first 10 lines.
# 1.10 Print lines that contain the character @.