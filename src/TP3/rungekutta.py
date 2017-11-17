def runge_kutta(x, y, step, final_x, fun):
    xi = x
    yi = y
    while xi < final_x:
        xi += step
        yi = runge_kutta_step(xi, yi, step, fun)
    return yi


def runge_kutta_step(x, y, h, fun):
    k1 = fun(x, y)
    k2 = fun(x + 1 / 2 * h, y + 1 / 2 * h * k1)
    k3 = fun(x + 1 / 2 * h, y + 1 / 2 * h * k2)
    k4 = fun(x + h, y + k3 * h)

    return y + 1/6 * h * (k1 + 2*k2 + 2*k3 + k4)
