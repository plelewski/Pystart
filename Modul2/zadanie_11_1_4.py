sentence = "12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek"

sent_list = sentence.split()
weight = 0

for i in sent_list:
    if i.isnumeric():
        weight += int(i)

print(weight)
