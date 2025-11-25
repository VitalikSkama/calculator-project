import datetime

name = input("Введіть ваше ім'я: ")
now = datetime.datetime.now().strftime("%H:%M:%S")

print(f"Привіт, {name}!")
print(f"Поточний час: {now}")
