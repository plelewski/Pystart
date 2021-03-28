liquid = int(input("Ile płynu przyjechało z fabryki "))
liquid_in_bottle = round(330 - 330 * 0.12, 2)

print("Płynu w każdej butelce" + str(liquid_in_bottle))
print("Pracownik zabierze " + str(liquid % liquid_in_bottle))
