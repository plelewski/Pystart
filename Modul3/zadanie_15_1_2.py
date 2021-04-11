numbers = []
# done = False
# last_num = None
#
# while not done:
#     current_num = int(input('Podaj cyfrę - jeśli to druga i kolejna, musi być większa od poprzedniej: '))
#     if last_num is None:
#         last_num = current_num
#         numbers.append(current_num)
#         continue
#     if current_num < last_num:
#         done = True
#         continue
#
#     numbers.append(current_num)
#     last_num = current_num
#
# print('Średnia', sum(numbers) / len(numbers))

while True:
    numbers.append(float(input('Podaj liczbę większą od poprzedniej:\t')))
    if len(numbers) > 1 and numbers[-1] < numbers[-2]:
        break
