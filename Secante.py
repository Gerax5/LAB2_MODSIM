import numpy as np

def secante(f, x0, x1, tol=1e-6, maxIter=100, prt=0):
    z = [x0, x1]
    fz = [f(x0), f(x1)]
    iters = 0
    conv = 0
    errx = None
    erry = None

    while iters < maxIter:
        f0 = fz[-2]
        f1 = fz[-1]
        if (f1 - f0) == 0:
            raise ZeroDivisionError("División por cero en método de la secante")

        x2 = z[-1] - f1 * (z[-1] - z[-2]) / (f1 - f0)
        f2 = f(x2)

        z.append(x2)
        fz.append(f2)

        errx = np.abs(z[-1] - z[-2])
        erry = np.abs(fz[-1] - fz[-2])

        if prt:
            print(f"iter={iters}, x={x2}, f(x)={f2}, errx={errx}")

        if errx < tol or abs(f2) < tol:
            conv = 1
            break

        iters += 1

    return x2, f2, z, errx, erry, iters, conv
