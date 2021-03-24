# pole trójkąta o podanych wierzchołkach na osi liczbowej

vertices = []
for i in range(1,4):
    xy = [int(j) for j in input(f'Podaj dane {i} wierzchołka ').split(',')]
    vertices.append(xy)

# sposób 1
field = (abs((vertices[1][0] - vertices[0][0]) *
            (vertices[2][1] - vertices[0][1]) -
            (vertices[1][1] - vertices[0][1]) *
            (vertices[2][0] - vertices[0][0]))) / 2

# sposób 2
# min_x = min(vertices[0][0], vertices[1][0], vertices[2][0])
# max_x = max(vertices[0][0], vertices[1][0], vertices[2][0])
# min_y = min(vertices[0][1], vertices[1][1], vertices[2][1])
# max_y = max(vertices[0][1], vertices[1][1], vertices[2][1])
# rect_field = (max_x - min_x) * (max_y - min_y)
#
# triangle_field_1 = (abs(vertices[0][0] - vertices[1][0]) * abs(vertices[0][1] - vertices[1][1])) / 2
# triangle_field_2 = (abs(vertices[1][0] - vertices[2][0]) * abs(vertices[1][1] - vertices[2][1])) / 2
# triangle_field_3 = (abs(vertices[2][0] - vertices[0][0]) * abs(vertices[2][1] - vertices[0][1])) / 2
#
# field = rect_field - triangle_field_1 - triangle_field_2 - triangle_field_3

print(f'Pole trójkąta wynosi {field} cm2')
