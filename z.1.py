wynik=int(input("Podaj liczbę punktów"))
if wynik >= 80:
    print("Egzamin zaliczony w terminie")
elif wynik < 80 and wynik >50:
    print("Możesz poprawić egzamin")
else:
    print("Egzamin niezaliczony")