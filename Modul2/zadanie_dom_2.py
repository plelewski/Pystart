# to bin
value1 = 173
list = []

while True:
    value1, rest = divmod(value1, 2)
    list.append(rest)
    if value1 == 0:
        break

for i in list[::-1]:
    print(i, end='')
print()

# to dec
dec_str = "10101101"
dec_value = 0

for a in range(len(dec_str)):
    dec_value += int(dec_str[a]) * 2 ** (len(dec_str) - a - 1)

print(dec_value)
