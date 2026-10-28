with open("notowania giełdowe.txt." , "a") as plik:
    plik.write("ALR,113")
with open("notowania giełdowe.txt.", "r") as plik:
    for line in plik:
        print(line)