def main():
    with open("astronauts.csv") as asztronotakfalyl:
        asztronotak = asztronotakfalyl.readlines()
    honapok = []
    for line in asztronotak:
        honapok.append(line.split(",")[4].split("/")[0])
    del honapok[0]
    kalkulalosdi_es_nyomtatosdi(honapok)


def kalkulalosdi_es_nyomtatosdi(honapok):
    x, szuletesek = 1, []
    while x != 13:
        y = [honapok.count(str(x)), x, round(honapok.count(str(x)) / len(honapok) * 100, 1)]
        szuletesek.append(y)
        x += 1
    print("százalék  hónap_száma")
    print(sorted(szuletesek)[-1][2], sorted(szuletesek)[-1][1])
    print(sorted(szuletesek)[-2][2], sorted(szuletesek)[-2][1])
    print(sorted(szuletesek)[-3][2], sorted(szuletesek)[-3][1])


main()
