from typing import List, Tuple

# Define hotel and flight data
hotel: List[Tuple[str, int, int, int, int, int]] = [
    ("Abadan", 1136000, 0, 2274000, 607300, 0),
    ("Abadeh", 0, 0, 0, 566000, 515000),
    ("Arak", 824000, 0, 1957000, 0, 1339000),
    ("Ardabil", 580000, 0, 3770000, 327000, 1635000),
    ("Ardakan", 0, 0, 0, 797000, 741600),
    ("Esfahan", 780000, 2100000, 3660000, 417000, 773000),
    ("Ahvaz", 741600, 2950000, 2873700, 978000, 0),
    ("Bandar Abbas", 2276000, 2718000, 2900000, 1485000, 0),
    ("Bandar Anzali", 1275000, 2750000, 0, 618000, 1545000),
    ("Bojnurd", 830000, 1405000, 0, 0, 0),
    ("Birjand", 1263600, 1093000, 0, 520000, 0),
    ("Babol", 0, 0, 0, 742000, 0),
    ("Tabriz", 853000, 2142400, 2595000, 1479000, 1030000),
    ("Tehran", 1267000, 3090000, 3420000, 430000, 1030000),
    ("Jiroft", 927000, 0, 0, 0, 0),
    ("Kerman", 824000, 2260000, 2171000, 592000, 927000),
    ("Kermanshah", 0, 1610000, 1720000, 1166000, 1312200),
    ("Kashan", 1564000, 0, 0, 813000, 510000),
    ("Qazvin", 1905000, 1500000, 0, 310000, 1854000),
    ("Mashhad", 826000, 1744000, 2300000, 1072000, 1410000),
    ("Shiraz", 794000, 1152000, 1855000, 288000, 536000),
    ("Yazd", 325000, 1348000, 2110000, 380000, 310000),
    ("Qom", 1312000, 927000, 0, 713000, 445000),
    ("Sanandaj", 2120000, 1826000, 0, 0, 418000),
    ("Sari", 1045000, 824000, 0, 721000, 2400000),
    ("Hamedan", 918000, 1590000, 0, 650000, 577000),
    ("Gorgan", 1345000, 1500000, 2100000, 618000, 927000),
    ("Rasht", 1900000, 3250000, 2377000, 1236000, 412000),
    ("Zanjan", 709000, 3100000, 0, 578000, 1442000),
    ("Urmia", 1228000, 766000, 4400000, 1260000, 0),
    ("Qeshm", 721000, 1700000, 4220000, 650000, 618000),
    ("Sabzevar", 900000, 0, 0, 870000, 0),
    ("Nishapur", 0, 1820000, 0, 735000, 1545000),
    ("Kazerun", 0, 0, 0, 0, 0),
    ("Kish", 740000, 860000, 1854000, 834000, 0),
    ("Ilam", 1770000, 0, 0, 0, 0),
    ("Bushehr", 1300000, 0, 3368000, 740000, 780000),
    ("Bam", 0, 1761300, 0, 934000, 0),
    ("Bandar Lengeh", 0, 0, 0, 0, 0),
    ("Zabol", 0, 0, 0, 515000, 0),
    ("Karaj", 1800000, 0, 0, 810000, 1030000),
    ("Khorramabad", 1340000, 0, 0, 0, 1854000),
    ("Shahr-e Kord", 1300000, 2140000, 0, 470000, 0),
    ("Yasuj", 1567000, 1528000, 0, 0, 1140000),
    ("Ramsar", 1630000, 3400000, 0, 0, 722000),
    ("Najafabad", 0, 1820000, 0, 1130000, 1546000),
    ("Zarand", 1100000, 1875000, 0, 700000, 0),
    ("Maku", 0, 0, 0, 556000, 0),
    ("Dezful", 1340000, 0, 0, 1400000, 0),
    ("Mahabad", 800000, 0, 0, 0, 970000),
    ("Gonbad Kavus", 0, 0, 0, 566000, 1610000),
    ("Quchan", 0, 0, 0, 0, 0),
    ("Khoy", 1244000, 0, 0, 1020000, 0),
    ("Kashmar", 0, 0, 0, 0, 0),
    ("Lahijan", 1370000, 1920000, 2200000, 1140000, 2780000),
    ("Malayer", 0, 0, 0, 740000, 0),
    ("Maragheh", 0, 0, 0, 862000, 773000),
    ("Minab", 0, 0, 0, 1120000, 0),
    ("Nahavand", 0, 0, 0, 0, 0),
    ("Saveh", 0, 1100000, 0, 544000, 0),
    ("Shushtar", 773000, 0, 0, 741600, 700000),
    ("Susa", 0, 0, 0, 0, 0),
    ("Varamin", 785000, 0, 0, 0, 1468000)

]

havapeyma: List[Tuple[str, str, int]] = [
    ("Abadan", "Esfahan", 2110000), ("Abadan", "Mashhad", 1450000), ("Abadan", "Shiraz", 2100000),
    ("Abadan", "Kerman", 0), ("Abadan", "Kermanshah", 2350000), ("Abadan", "Bandar Abbas", 2800000),
    ("Abadan", "Tehran", 1500000), ("Arak", "Mashhad", 1900000), ("Arak", "Tehran", 850000),
    ("Ardabil", "Tehran", 2100000), ("Ardabil", "Mashhad", 2700000), ("Esfahan", "Tabriz", 2250000),
    ("Esfahan", "Mashhad", 2900000), ("Esfahan", "Bandar Abbas", 2700000), ("Esfahan", "Ahvaz", 2500000),
    ("Esfahan", "Gorgan", 2000000), ("Esfahan", "Kerman", 2400000), ("Esfahan", "Kermanshah", 2300000),
    ("Esfahan", "Kish", 3900000), ("Esfahan", "Rasht", 2400000), ("Esfahan", "Shiraz", 2100000),
    ("Esfahan", "Tehran", 2200000), ("Esfahan", "Zahedan", 2600000), ("Esfahan", "Abadan", 2110000),
    ("Esfahan", "Ramsar", 2500000), ("Esfahan", "Qeshm", 2700000), ("Esfahan", "Sari", 2100000),
    ("Esfahan", "Yazd", 1800000), ("Ahvaz", "Esfahan", 2500000), ("Ahvaz", "Yazd", 1900000),
    ("Ahvaz", "Shiraz", 2120000), ("Ahvaz", "Rasht", 3570000), ("Ahvaz", "Tabriz", 3125000),
    ("Ahvaz", "Mashhad", 2800000), ("Ahvaz", "Kish", 2000000), ("Ahvaz", "Kermanshah", 2350000),
    ("Ahvaz", "Bandar Abbas", 3570000), ("Ahvaz", "Sari", 2600000), ("Ahvaz", "Tehran", 2400000),
    ("Bandar Abbas", "Tehran", 3250000), ("Bandar Abbas", "Shiraz", 2200000), ("Bandar Abbas", "Esfahan", 2700000),
    ("Bandar Abbas", "Tabriz", 3600000), ("Bandar Abbas", "Yazd", 1950000), ("Bandar Abbas", "Rasht", 3520000),
    ("Bandar Abbas", "Abadan", 2800000), ("Bandar Abbas", "Kermanshah", 2500000), ("Bandar Abbas", "Ahvaz", 3100000),
    ("Bandar Abbas", "Mashhad", 2500000), ("Bandar Abbas", "Sari", 3300000), ("Bandar Abbas", "Bushehr", 2000000),
    ("Bandar Abbas", "Kish", 2000000), ("Bandar Abbas", "Gorgan", 2700000), ("Bojnurd", "Tehran", 2500000),
    ("Birjand", "Tehran", 2800000), ("Birjand", "Mashhad", 1800000), ("Tabriz", "Tehran", 2400000),
    ("Tabriz", "Mashhad", 3000000), ("Tabriz", "Esfahan", 2700000), ("Tabriz", "Shiraz", 3300000),
    ("Tabriz", "Ahvaz", 3120000), ("Tabriz", "Bandar Abbas", 3600000), ("Tabriz", "Kish", 3200000),
    ("Tabriz", "Qeshm", 2800000), ("Tabriz", "Rasht", 2500000), ("Tabriz", "Sari", 2500000),
    ("Tabriz", "Kermanshah", 2300000), ("Tehran", "Mashhad", 2500000), ("Tehran", "Bandar Abbas", 3300000),
    ("Tehran", "Khorramabad", 2000000), ("Tehran", "Tabriz", 2400000), ("Tehran", "Kish", 3300000),
    ("Tehran", "Qeshm", 3200000), ("Tehran", "Abadan", 2560000), ("Tehran", "Chabahar", 3200000),
    ("Tehran", "Ahvaz", 2400000), ("Tehran", "Shiraz", 2600000), ("Tehran", "Sirjan", 2800000),
    ("Tehran", "Sanandaj", 2100000), ("Tehran", "Esfahan", 2000000), ("Tehran", "Birjand", 2800000),
    ("Tehran", "Bojnurd", 2500000), ("Tehran", "Zahedan", 3300000), ("Tehran", "Yazd", 2300000),
    ("Tehran", "Ilam", 2300000), ("Tehran", "Kerman", 2800000), ("Tehran", "Ardabil", 2100000),
    ("Tehran", "Gorgan", 2000000), ("Tehran", "Kermanshah", 2100000), ("Tehran", "Urmia", 2500000),
    ("Tehran", "Dezful", 2200000), ("Tehran", "Jahrom", 2700000), ("Tehran", "Bandar Lengeh", 2500000),
    ("Tehran", "Rasht", 2000000), ("Tehran", "Yasuj", 2400000), ("Tehran", "Bushehr", 2500000),
    ("Tehran", "Arak", 850000), ("Tehran", "Nowshahr", 1900000), ("Tehran", "Ramsar", 2000000),
    ("Tehran", "Sari", 770000), ("Tehran", "Shahrekord", 1900000), ("Tehran", "Maragheh", 2300000),
    ("Tehran", "Jiroft", 3100000), ("Tehran", "Zabol", 3150000), ("Tehran", "Sabzevar", 2500000),
    ("Tehran", "Rafsanjan", 2450000), ("Tehran", "Khoy", 2560000), ("Tehran", "Hamedan", 1850000),
    ("Tehran", "Karaj", 1200000), ("Tehran", "Zanjan", 1950000), ("Zanjan", "Mashhad", 2600000),
    ("Zanjan", "Kish", 2400000), ("Urmia", "Tehran", 2500000), ("Urmia", "Mashhad", 2600000),
    ("Urmia", "Kish", 2600000), ("Qeshm", "Tehran", 3200000), ("Qeshm", "Mashhad", 2800000),
    ("Qeshm", "Shiraz", 2500000), ("Qeshm", "Esfahan", 2700000), ("Qeshm", "Gorgan", 2500000),
    ("Qeshm", "Tabriz", 3000000), ("Qeshm", "Kermanshah", 2800000), ("Sabzevar", "Tehran", 2500000),
    ("Kish", "Tehran", 3300000), ("Kish", "Shiraz", 2400000), ("Kish", "Mashhad", 2700000),
    ("Kish", "Esfahan", 2500000), ("Kish", "Bandar Abbas", 2200000), ("Kish", "Kerman", 2900000),
    ("Kish", "Ahvaz", 2200000), ("Kish", "Tabriz", 3200000), ("Kish", "Yazd", 2300000),
    ("Kish", "Hamedan", 2600000), ("Kish", "Bushehr", 2500000), ("Kish", "Rasht", 2600000),
    ("Kish", "Kermanshah", 2800000), ("Kish", "Sari", 2700000), ("Kish", "Kashan", 2000000),
    ("Kish", "Gorgan", 2500000), ("Kish", "Urmia", 2600000), ("Kish", "Sanandaj", 2800000),
    ("Kish", "Nowshahr", 2400000), ("Ilam", "Tehran", 2300000), ("Ilam", "Mashhad", 2500000),
    ("Bushehr", "Tehran", 2500000), ("Bushehr", "Esfahan", 2100000), ("Bushehr", "Mashhad", 2000000),
    ("Bushehr", "Kish", 2000000), ("Bushehr", "Ahvaz", 2300000), ("Bushehr", "Shiraz", 2000000),
    ("Bam", "Tehran", 3000000), ("Bandar Lengeh", "Shiraz", 2400000), ("Bandar Lengeh", "Tehran", 2800000),
    ("Zabol", "Tehran", 2500000), ("Zabol", "Mashhad", 2600000), ("Karaj", "Kish", 1900000),
    ("Karaj", "Ahvaz", 1800000), ("Karaj", "Mashhad", 1700000), ("Karaj", "Yazd", 1900000),
    ("Khorramabad", "Tehran", 2000000), ("Khorramabad", "Mashhad", 2200000), ("Shahr-e Kord", "Tehran", 1900000),
    ("Shahr-e Kord", "Mashhad", 2200000), ("Yasuj", "Tehran", 2400000), ("Ramsar", "Tehran", 2000000),
    ("Ramsar", "Mashhad", 2300000), ("Ramsar", "Esfahan", 2400000)
]

# Define city lists for different trip types
mazhabi = [
    "Abadeh", "Arak", "Ardabil", "Ardakan", "Esfahan", "Ahvaz",
    "Bojnurd", "Birjand", "Tabriz", "Tehran", "Kerman", "Kermanshah",
    "Kashan", "Qazvin", "Mashhad", "Shiraz", "Yazd", "Qom", "Sanandaj",
    "Hamedan", "Zanjan", "Urmia", "Sabzevar", "Nishapur", "Kazerun",
    "Ilam", "Zabol", "Khorramabad", "Shahr-e Kord", "Yasuj",
    "Najafabad", "Zarand", "Maku", "Dezful", "Mahabad",
    "Gonbad Kavus", "Quchan", "Khoy", "Kashmar", "Malayer",
    "Maragheh", "Minab", "Nahavand", "Saveh", "Shushtar",
    "Susa", "Varamin"
]

tarikhi = [
    "Abadan", "Abadeh", "Arak", "Ardabil", "Ardakan", "Esfahan", "Ahvaz",
    "Bandar Abbas", "Bandar Anzali", "Bojnurd", "Birjand", "Babol",
    "Tabriz", "Tehran", "Jiroft", "Kerman", "Kermanshah", "Kashan",
    "Qazvin", "Mashhad", "Shiraz", "Yazd", "Qom", "Sanandaj", "Sari",
    "Hamedan", "Gorgan", "Rasht", "Zanjan", "Urmia", "Qeshm",
    "Sabzevar", "Nishapur", "Kazerun", "Kish", "Ilam", "Bushehr",
    "Bam", "Bandar Lengeh", "Zabol", "Karaj", "Khorramabad",
    "Shahr-e Kord", "Yasuj", "Ramsar", "Najafabad", "Zarand",
    "Maku", "Dezful", "Mahabad", "Gonbad Kavus", "Quchan", "Khoy",
    "Kashmar", "Lahijan", "Malayer", "Maragheh", "Minab", "Nahavand",
    "Saveh", "Shushtar", "Susa", "Varamin"
]

tafrihi = [
    "Abadan", "Arak", "Ardabil", "Esfahan", "Ahvaz", "Bandar Abbas",
    "Bandar Anzali", "Bojnurd", "Birjand", "Babol", "Tabriz", "Tehran",
    "Kerman", "Kermanshah", "Kashan", "Qazvin", "Mashhad", "Shiraz",
    "Yazd", "Qom", "Sanandaj", "Sari", "Hamedan", "Gorgan", "Rasht",
    "Zanjan", "Urmia", "Ilam", "Bushehr", "Bandar Lengeh", "Karaj",
    "Khorramabad", "Shahr-e Kord", "Yasuj", "Ramsar", "Dezful",
    "Gonbad Kavus", "Lahijan", "Maragheh", "Saveh", "Shushtar",
    "Susa", "Varamin"
]

def process_travel_request(Noe_safar: str, Noe_haml: str, mabda: str, nafarat: int, nights: int, bodje: int) -> List[str]:
    results = []
    select_1: List[Tuple[str, str, int]] = []
    select_2: List[Tuple[str, int, int, int, int, int]] = []

    if Noe_safar == "Mazhabi":
        city_list = mazhabi
    elif Noe_safar == "Tarikhi":
        city_list = tarikhi
    elif Noe_safar == "Tafrihi":
        city_list = tafrihi
    else:
        return ["Invalid trip type"]

    if Noe_haml == "Havapeyma":
        for flight in havapeyma:
            manba, nazaar, price = flight
            new_price = 2 * (price * nafarat)

            if manba == mabda and nazaar in city_list:
                select_1.append((manba, nazaar, new_price))

        for chacked in select_1:
            _, magsad, never = chacked  # Changed this line to use magsad (destination) instead of manba (origin)

            for check_time in hotel:
                hel = check_time[0]
                if hel == magsad:  # Changed this line to compare with magsad
                    updated_check_time = tuple(
                        (x + never if x > 0 else x) for x in check_time[1:]
                    )
                    select_2.append((hel,) + updated_check_time)
                    break

        for i in range(len(select_2)):
            check_time = select_2[i]
            if nafarat > 2:
                updated_check_time = tuple(
                    ((x + (nafarat - 2) * 500000) * nights if x > 0 else x) 
                    for x in check_time[1:]
                )
            else:
                updated_check_time = tuple(x * nights for x in check_time[1:])
            select_2[i] = (check_time[0],) + updated_check_time

        for test in select_2:
            if all(x > 0 for x in test[1:]):
                if test[1] <= bodje:
                    results.append(f"{test[0]} 3 star")
                if test[2] <= bodje:
                    results.append(f"{test[0]} 4 star")
                if test[3] <= bodje:
                    results.append(f"{test[0]} 5 star")
                if test[4] <= bodje:
                    results.append(f"{test[0]} mehmankhone")
                if test[5] <= bodje:
                    results.append(f"{test[0]} egamatghah")

    elif Noe_haml == "Otobus":
        updated_hotel = [
            (check_time[0], *(x + 600000 if x > 0 else x for x in check_time[1:]))
            for check_time in hotel
            if any(x > 0 for x in check_time[1:])
        ]

        for i in range(len(updated_hotel)):
            price = updated_hotel[i]
            if nafarat > 2:
                updated_price = tuple(
                    ((x + (nafarat - 2) * 600000) * nights if x > 0 else x)
                    for x in price[1:]
                )
            else:
                updated_price = tuple(x * nights for x in price[1:])
            updated_hotel[i] = (price[0],) + updated_price

        for manba in city_list:
            for chacked in updated_hotel:
                if chacked[0] == manba and all(x > 0 for x in chacked[1:]):
                    if chacked[1] <= bodje:
                        results.append(f"{chacked[0]} 3 star")
                    if chacked[2] <= bodje:
                        results.append(f"{chacked[0]} 4 star")
                    if chacked[3] <= bodje:
                        results.append(f"{chacked[0]} 5 star")
                    if chacked[4] <= bodje:
                        results.append(f"{chacked[0]} mehmankhone")
                    if chacked[5] <= bodje:
                        results.append(f"{chacked[0]} egamatghah")
                    break

    elif Noe_haml == "KhodroSavari":
        updated_hotel = [
            (check_time[0], *(x + 500000 if x > 0 else x for x in check_time[1:]))
            for check_time in hotel
            if any(x > 0 for x in check_time[1:])
        ]

        for i in range(len(updated_hotel)):
            price = updated_hotel[i]
            if nafarat > 2:
                updated_price = tuple(
                    ((x + (nafarat - 2) * 500000) * nights if x > 0 else x)
                    for x in price[1:]
                )
            else:
                updated_price = tuple(x * nights for x in price[1:])
            updated_hotel[i] = (price[0],) + updated_price

        for manba in city_list:
            for chacked in updated_hotel:
                if chacked[0] == manba and all(x > 0 for x in chacked[1:]):
                    if chacked[1] <= bodje:
                        results.append(f"{chacked[0]} 3 star")
                    if chacked[2] <= bodje:
                        results.append(f"{chacked[0]} 4 star")
                    if chacked[3] <= bodje:
                        results.append(f"{chacked[0]} 5 star")
                    if chacked[4] <= bodje:
                        results.append(f"{chacked[0]} mehmankhone")
                    if chacked[5] <= bodje:
                        results.append(f"{chacked[0]} egamatghah")
                    break

    else:
        results.append("Invalid transport type")

    return results