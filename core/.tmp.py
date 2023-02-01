dt = 3

motion = [[11, 12], [2, 2], [3, 0]]

integrate = lambda const, degree : (const/degree)*dt**degree
for derivative_order_1, quantity_2 in enumerate(motion):
    for derivative_order_2, quantity_2 in enumerate(motion):
        if derivative_order_2 <= derivative_order_1:
            continue
        const_x, const_y = quantity_2
        relative_degree = derivative_order_2 - derivative_order_1
        index = derivative_order_1
        motion[index][0] += integrate(const_x, relative_degree)
        motion[index][1] += integrate(const_y, relative_degree)

print(motion)
