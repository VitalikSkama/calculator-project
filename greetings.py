import datetime

with open("data/names.txt", "r") as file:
    names = file.read().splitlines()

now = datetime.datetime.now().strftime("%H:%M:%S")

for name in names:
    print(f"Привіт, {name}! Час зараз: {now}")
