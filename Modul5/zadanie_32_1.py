# sposób 1
result = []
sumval = 0

with open('transakcje.csv', newline='') as bank_account:
    for line in bank_account:
        value = int(line.strip().split(',')[2])
        if value > 0:
            result.append(line)
            sumval += value

with open('przychody.csv', 'w') as incomes:
    # for i in result:
    #    incomes.write(f'{i}\n')
    incomes.writelines(result)
    incomes.write(f'Suma przychodów {sumval}')

# sposób 2
# from csv import reader, writer
#
# result=[]
# sum_val = 0
# with open('transakcje.csv') as bank_account:
#     content = reader(bank_account, delimiter=',')
#     for line in content:
#         created_at, desc, value = line
#         if int(value) > 0:
#             result.append(line)
#             sum_val += int(value)
#
# with open('przychody2.csv', 'w') as incomes:
#     content2 = writer(incomes, delimiter=',')
#     for line in result:
#         content2.writerow(line)
#     incomes.write(f'Suma przychodów {sum_val}')