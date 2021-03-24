# pole trójkąta o podanych wierzchołkach na osi liczbowej

vertices = []

for i in range(1,4):
    while len(vertices) < i:
        try:
            xy = [int(j) for j in input(f'Podaj dane {i} wierzchołka ').split(',')]
        except ValueError:
            print('Podaj wartości całkowite')
            continue

        if len(xy) == 2:
            vertices.append(xy)
        else:
            print('Ilość podanych wartości jest różna od 2. Podaj prawidłowe dane.')

area = (abs((vertices[1][0] - vertices[0][0]) *
            (vertices[2][1] - vertices[0][1]) -
            (vertices[1][1] - vertices[0][1]) *
            (vertices[2][0] - vertices[0][0]))) / 2

print(f'Pole trójkąta wynosi {area} cm2')
