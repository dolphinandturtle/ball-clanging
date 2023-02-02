dt = 0.1

X, Y = 0, 1

spacial = [[11, 12], [2, 2], [3, 0]]

for i in range(10):
    primitive = lambda const, degree : (const/degree)*dt**degree
    for degree, _ in enumerate(spacial):
        for __degree, __const in enumerate(spacial):
            if __degree <= degree:
                continue
            relative_degree = __degree - degree
            spacial[degree][X] += primitive(__const[X], relative_degree)
            spacial[degree][Y] += primitive(__const[Y], relative_degree)
    print(spacial)
