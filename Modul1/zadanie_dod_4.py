from math import sqrt

vertices = []

for i in range(1,3):
    while len(vertices) < i:
        xy = [int(j) for j in input(f'Podaj dane {i} wierzchołka ').split(',')]
        try:
            complex(xy[0]) and complex(xy[1])
        except ValueError:
            print('Podaj wartości liczbowe')
            continue

        if len(xy) == 2:
            vertices.append(xy)
        else:
            print('Ilość podanych wartości jest różna od 2. Podaj prawidłowe dane.')

length_a = abs(vertices[0][0] - vertices[1][0])
length_b = abs(vertices[0][1] - vertices[1][1])

length_c = round(sqrt(length_a ** 2 + length_b ** 2),3)
print(f"Długość odcinka to {length_c}")

if vertices[0][0] < vertices[1][0]:
    middle_x = vertices[0][0] + length_c / 2
else:
    middle_x = vertices[0][0] - length_c / 2

if vertices[0][1] < vertices[1][1]:
    middle_y = vertices[0][1] + (abs(vertices[0][1]) + abs(vertices[1][1])) / 2
else:
    middle_y = vertices[0][1] - (abs(vertices[0][1]) + abs(vertices[1][1])) / 2

print(f"Środek odcinka to x: {middle_x:.4} a y: {middle_y:.4}")
