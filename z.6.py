def sprawdz_wielkosc_litery():
    wejscie = input("Wprowadź pojedynczą literę: ")
    if len(wejscie) != 1 or not wejscie.isalpha():
        print("Błąd: Musisz wprowadzić dokładnie jedną literę!")
        return
    if wejscie.isupper():
        print(f"Litera '{wejscie}' jest DUŻA.")
    elif wejscie.islower():
        print(f"Litera '{wejscie}' jest mała.")


sprawdz_wielkosc_litery()
