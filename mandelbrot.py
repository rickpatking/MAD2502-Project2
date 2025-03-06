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
    Increases in row by 1 will decrease the imaginary part by 1 step
    Increases in column by 1 will increase the imaginary part by 1 step

    :param top_left: Complex number for the top_left of the grid
    :param bottom_right: Complex number for the bottom_right of the grid
    :param step: Spacing between grid points
    :return: A 2d numpy array of complex numbers
    """

    if bottom_right.real < top_left.real or bottom_right.imag > top_left.imag:
        return np.array([])

    rows = int((abs(top_left.imag - bottom_right.imag) // step) + 1)
    cols = int((abs(top_left.real - bottom_right.real) // step) + 1)
    ar = np.zeros((rows, cols), dtype=complex)
    row1 = np.arange(top_left.real, bottom_right.real, step)
    col1 = np.arange(top_left.imag, bottom_right.imag, -step)
    ar.real = row1
    ar.imag = col1.reshape(-1, 1)
    return ar

print(get_complex_grid(-1+1j, 1.1-1.1j, 1))