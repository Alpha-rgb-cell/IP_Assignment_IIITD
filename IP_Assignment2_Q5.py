def create_matrix(coordinates):
    matrix = []
    for x, y in coordinates:
        matrix.append([x, y, 1])
    return matrix

def scale_shape(coordinates, cx, cy):
    shape_matrix = create_matrix(coordinates)
    scaling_matrix = [[cx, 0, 0], [0, cy, 0], [0, 0, 1]]
    new_matrix = []
    for i in range(len(shape_matrix)):
        new_matrix.append([0, 0, 0])
        for j in range(3):
            for k in range(3):
                new_matrix[i][j] += shape_matrix[i][k] * scaling_matrix[k][j]
    new_coordinates = []
    for x, y, _ in new_matrix:
        new_coordinates.append((x, y))
    return new_coordinates

coordinates = [(1, 2), (3, 4), (5, 6)]
cx = 2
cy = 3
scaled_coordinates = scale_shape(coordinates, cx, cy)
print(scaled_coordinates)
