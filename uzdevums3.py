with open("Cits kosmoss.txt", encoding="utf-8") as file:
    saturs = file.read()
    print(file.name) #datnes nosaukums
    print(saturs) #teksta saturs

    #izvada cik simboli ir tekstā
    numChar = len(saturs)
    print("Tekstā ir ", numChar, " simboli")

    #izvada vārdu skaitu tekstā
    WordCount = saturs.split() #split atgriež sadala vārdus skaitļu virknē
    print("Tekstā ir", len(WordCount), " vārdi.")

#izvada rindas teksta failā
with open("Cits kosmoss.txt", "r", encoding="utf-8") as file:
    numLines = len(file.readlines())
    print("Rindas teksta failā: ", numLines)
    print("\n")

       #izvada pirmos 20 simbolus
    divdesmit = saturs[0:20]
    print("Pirmie 20 simboli ir: ", divdesmit)

        #izvada pirmo simbolu
    pirmais = saturs[0]
    print("Pirmais simbols", pirmais)

        #izvada otro simbolu
    otrais = saturs[1]
    print("Otrais simbols ir ", otrais)

        #funkcija, kas izvada pirmo rindu
filename = "Cits kosmoss.txt"
def pirmarinda():
    file = open("Cits kosmoss.txt", "r", encoding="utf-8")
    rinda1=file.readlines(1)
    print("Pirmā rinda ir: ", rinda1)
pirmarinda()

file.close