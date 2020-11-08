from itertools import permutations, combinations

zbior = set([13])
limit = 70

while True:
    pr = set()                          # zmianna do przechowywania permutacji elementów ze zbioru -> 13, 31
    stary_zbior = zbior.copy()          # kopia zbioró do porównania czy ilość elemtów się zwiększyła
    for el in zbior:                    # pętla po wszystkich elementach ze zbioru
        el = str(el)                    # zmiana na string, żeby można było zamieniać kolejnością znaków
        el_perm = permutations(el)      # tworzenie permutacji dla danego elementu ze zbioru
        for n in list(el_perm):         # obektu typu permutations nie można iterować dlatego zamiana na liste
            if len(n) < 2:              # jeżli element ze zbioru posiada mniej cyfr niż 2 to nie możemy go permutować
                pr.add(int(n[0]))       # przepisanie elemetu bez zmian
            else:
                pr.add(int(n[0]+n[1]))  # dodanie nowej permutacji do zbioru pr n[0]+n[1] łączy znaki, n nie jest liczbą

    pary = combinations(pr, 2)          # tworzenie wszystkich kobinacji par dwójek
    for k in list(pary):                # obiektu typu combinations nie można interować dlatego zamiana na liste
        k_sum = k[0]+k[1]               # obliczanie sumy dla danej pary
        if k_sum < limit:               # sprawdzanie czy suma nie przekracza założonego limitu
            zbior.add(k_sum)            # dodanie sumy do zbioru

    # sprawdzanie czy dodano nowe elementu to zbioru -> obliczenie różnicy zbioru z początku pętli while i z końca
    if len(zbior.difference(stary_zbior)) == 0:
        break                           # opuszczenie pętli break

print("Końcowy zbiór to: {}".format(zbior))
