print("Hello, Git")

def przywitaj(imie):
    print(f"Witaj, {imie}!")

przywitaj("Michal")

from utils import loguj

# Przykładowe użycie
loguj("Aplikacja została uruchomiona")
loguj("Wykonano ważną operację", "moj_log.log")