sentence = "Pies to najlepszy przyjaciel człowieka, ale nie każdy pies o tym wie"

licznik = 0
for word in sentence.split():
    if word.lower() == "pies":
        licznik += 1

print(f"Wyraz pies wystąpił {licznik} razy")

# znacznie krócej
print(sentence.lower().count('pies'))
