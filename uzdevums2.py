atzimes_skaidrojums = {
10:"Izcili",
9:"Teicami",
8:"Ļoti labi",
7:"Labi",
6:"Gandrīz labi",
5:"Viduvēji",
4:"Gandrīz viduvēji",
3:"Nesekmīgs",
2:"Nesekmīgs",
1:"Nesekmīgs"
}
#ievada veselu skaitli no 1 līdz 10
while True:
    try:
        n = int(input("Ievadiet veselu skaitli no 1 līdz 10 "))
        if 1 <= n <= 10:
            break
        else:
            print("Ievadītais skaitlis nav no 1 līdz 10. Lūdzu ievadiet pareizu skaitli.")
    except ValueError:
        print("Ievadītajam vērtējumam jābūt veselam skaitlim.")

#izvada skaidrojumu
skaidrojums = atzimes_skaidrojums[n]
print(f"Vārdiskais skaidrojums ievadītajam vērtējumam {n} ir: {skaidrojums}" )