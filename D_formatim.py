def format_numrin(vlera: float, shifra: int = 2, monedha: str = "Lek") -> str:
    if not (0 <= shifra <= 4):
        return "-1"
    format_str = f"{{:,.{shifra}f}} {monedha}"
    return format_str.format(vlera)

# Testim
while True:
    try:
        vlera = float(input("Shuma: "))
        shifra_input = input("Shifra decimale (Enter për parazgjedhje): ")
        monedha_input = input("Monedha (Enter për Lek): ")

        shifra = int(shifra_input) if shifra_input else 2
        monedha = monedha_input if monedha_input else "Lek"

        rezultati = format_numrin(vlera, shifra, monedha)
        if rezultati == "-1":
            print("Gabim")
        else:
            print(rezultati)
    except ValueError:
        print("Shkruaj vlera të vlefshme!")
