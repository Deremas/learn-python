# 
import os

os.chdir(r'C:\Users\home\Pictures\Screenshots')

# print(os.listdir())

for f in os.listdir():
    splitted = os.path.splitext(f)

    if f == "desktop.ini" or splitted[1] == ".ini":
        continue

    print(splitted)
