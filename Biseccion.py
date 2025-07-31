def biseccion(f, a, b, tol=1e-6, maxIter=100, prt=0):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")

    z = []
    fz = []
    iters = 0
    conv = 0

    while iters < maxIter:
        x = (a + b) / 2
        fx = f(x)
        z.append(x)
        fz.append(fx)

        if prt:
            print(f"iter = {iters}, z = {x}, f(z) = {fx}")

        # Criterio de parada
        if abs(b - a) < tol or abs(fx) < tol:
            conv = 1
            break

        if f(a) * fx < 0:
            b = x
        else:
            a = x

        iters += 1

    return x, fx, z, iters, conv
