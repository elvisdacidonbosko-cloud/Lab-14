def llogarit_noten(p1: float, p2: float, provim: float) -> tuple:
    if not (0 <= p1 <= 10) or not (0 <= p2 <= 10) or not (0 <= provim <= 10):
        return (-1, "Jashtë intervalit")
    mes = round(p1 * 0.3 + p2 * 0.3 + provim * 0.4, 2)
    if mes < 5:
        etiketa = "Dobët"
    elif mes < 7:
        etiketa = "Mjaftueshëm"
    elif mes < 9:
        etiketa = "Mirë"
    else:
        etiketa = "Shkëlqyeshëm"
    return (mes, etiketa)

# Testim
while True:
    try:
        p1 = float(input("p1: "))
        p2 = float(input("p2: "))
        provim = float(input("Provim: "))
        mes, etiketa = llogarit_noten(p1, p2, provim)
        if mes == -1:
            print("Të dhëna jashtë intervalit")
        else:
            print(f"Mes: {mes}")
            print(f"Etiketa: {etiketa}")
    except ValueError:
        print("Shkruaj vlera numerike!")
