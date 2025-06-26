def loguj(tresc, plik_logu='log.txt'):
    """
    Zapisuje podaną treść do pliku logu

    :param tresc: Tekst do zapisania w logu
    :param plik_logu: Nazwa pliku logu (domyślnie 'log.txt')
    """
    import datetime

    # Pobierz aktualną datę i czas
    teraz = datetime.datetime.now()
    timestamp = teraz.strftime("%Y-%m-%d %H:%M:%S")

    # Format wpisu w logu: [TIMESTAMP] TRESC
    wpis = f"[{timestamp}] {tresc}"

    # Otwórz plik w trybie dopisywania (append)
    with open(plik_logu, 'a', encoding='utf-8') as f:
        f.write(wpis + "\n")