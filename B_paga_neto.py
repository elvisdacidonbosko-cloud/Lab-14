def paga_neto(bruto: float, tatim: float = 13.0, sigurime: float = 9.5) -> float:
    if bruto < 0 or not (0 <= tatim <= 100) or not (0 <= sigurime <= 100):
        return -1
    return bruto * (1 - tatim / 100) * (1 - sigurime / 100)

# Testim
while True:
    try:
        bruto = float(input("Bruto: "))
        tatim_input = input("Tatim (%): ")
        sigurime_input = input("Sigurime (%): ")

        tatim = float(tatim_input) if tatim_input else 13.0
        sigurime = float(sigurime_input) if sigurime_input else 9.5

        neto = paga_neto(bruto, tatim, sigurime)
        if neto == -1:
            print("Të dhëna të pavlefshme")
        else:
            print(f"Neto: {neto:.2f}")
    except ValueError:
        print("Shkruaj vlera numerike!")
