tup_list = [
    (1, 2, 3, 4, 5, 6, 7),
    (4,),
    (5, 6),
    (5, 6, 7)
]

print([tup_to for tup_to in tup_list if 1 < len(tup_to) < 6])
print([sum(tup_to) if len(tup_to) % 2 == 0 else sum(tup_to) / len(tup_to) for tup_to in tup_list if 1 < len(tup_to) < 6])
