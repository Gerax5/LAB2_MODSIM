import numpy as np

def newton_raphson(f, df, x0, tol=1e-6, maxIter=100, prt=0):
    z = [x0]
    fz = [f(x0)]
    iters = 0
    conv = 0
    errx = None
    erry = None

    while iters < maxIter:
        fx = fz[-1]
        dfx = df(z[-1])
        if dfx == 0:
            raise ZeroDivisionError("Derivada cero en Newton-Raphson")

        x1 = z[-1] - fx / dfx
        f1 = f(x1)

        z.append(x1)
        fz.append(f1)

        errx = np.abs(z[-1] - z[-2])
        erry = np.abs(fz[-1] - fz[-2])

        if prt:
            print(f"iter={iters}, x={x1}, f(x)={f1}, errx={errx}")

        # Condición de parada
        if errx < tol or abs(f1) < tol:
            conv = 1
            break

        iters += 1

    return x1, f1, z, errx, erry, iters, conv
