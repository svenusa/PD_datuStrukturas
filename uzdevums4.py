import csv

with open ("antidopings.csv", encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    csv1 = csv.reader(file)#izveido csv objektu
    saraksts = list(csv1)
    print("Izdruka ir: ", saraksts, "\n")#izvada csv datus masīvā

        #masīva garums
    garums=len(saraksts)
    print("Masīva garums", garums, "\n")

        #pedejie 3 elementi
    pedejais = saraksts[-1], saraksts[-2], saraksts[-3]
    print("Saraksta pedejie 3 elementi ir:", pedejais)

    print("Datnes nosaukums ir: ", file.name, "\n")

    pirmais = saraksts[1]
    print("Pirmais elements sarkstā ir", pirmais)

   