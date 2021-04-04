import pprint

sentence = "Zdanie, które ma być poddane analizie znaków"
sent_dict = {}

for i in sentence:
    if i not in sent_dict.keys():
        sent_dict[i] = 0
    sent_dict[i] += 1

print(sent_dict)

# lepszy sposób
sent_dict2 = {}

for character in sentence:
    sent_dict2.setdefault(character, 0)
    sent_dict2[character] += 1

pprint.pprint(sent_dict2)
