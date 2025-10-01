def llogarit_perqindjen(pjesa: float, teresia: float) -> float:
    if teresia <= 0 or pjesa < 0:
        return -1
    return (pjesa / teresia) * 100

# Testim
while True:
    try:
        pjesa = float(input("Pjesa: "))
        teresia = float(input("Teresia: "))
        perqindja = llogarit_perqindjen(pjesa, teresia)
        if perqindja == -1:
            print("Të dhëna të pavlefshme")
        else:
            print(f"Perqindja: {perqindja:.2f}%")
    except ValueError:
        print("Shkruaj vlera numerike!")
