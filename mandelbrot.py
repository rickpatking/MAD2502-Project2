import numpy as np

def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """
    Calculates the number of iterations that have passed before
    the escape time of a complex number in the Mandelbrot set.
    Uses the sequence of z_n to calculate a z_k, and when the absolute value
    of z_k is greater than 2 the point will escape.


    :param c: complex number to test
    :param max_iterations: max number of iterations
    :return: returns how many iterations have passed before the point escaped,
    if it never escaped it will return None
    """
    z = c
    for i in range(max_iterations):
        if abs(z) > 2:
            return i
        z = ((z)**2) + c
    if abs(z) > 2:
        return max_iterations
    return None

def get_complex_grid(
    top_left: complex,
    bottom_right: complex,
    step: float
) -> np.ndarray:
    """
    Computes a numpy array of complex numbers that are evenly spaced between top_left and bottom_right
    Increases row by 1 will increase

    :param top_left:
    :param bottom_right:
    :param step:
    :return:
    """
    rows = int((abs(top_left.imag - bottom_right.imag) // step) + 1)
    cols = int((abs(top_left.real - bottom_right.real) // step) + 1)
    ar = np.zeros((rows, cols), dtype=complex)
    if top_left.real < bottom_right.real:
        row1 = np.arange(top_left.real, bottom_right.real)
    else:
        row1 = np.arange(top_left.real*-1, bottom_right.real*-1)
        row1 = row1[::-1]
    if top_left.imag < bottom_right.imag:
        col1 = np.arange(top_left.imag, bottom_right.imag)
    else:
        col1 = np.arange(top_left.imag*-1, bottom_right.imag*-1)
        col1 = col1[::-1]
    ar.real = row1
    ar.imag = col1.reshape(-1, 1)
    return ar

print(get_complex_grid(+1-1j, -1.1+1.1j, 1))