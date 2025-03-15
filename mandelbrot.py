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

    row1 = np.arange(top_left.real, bottom_right.real, step)
    col1 = np.arange(top_left.imag, bottom_right.imag, -step)
    col1 = col1.reshape(-1, 1)
    ar = row1 + col1 * 1j
    return ar

def get_julia_color_arr(grid: np.ndarray, c: complex, max_iter: int) -> np.ndarray:
    """
    Compute the escape times for the filled Julia set of the given complex number c.

    Parameters:
        grid (np.ndarray): 2D array of complex numbers representing the complex plane.
        c (complex): The constant c defining the Julia set.
        max_iter (int): Maximum number of iterations before declaring a point inside the set.

    Returns:
        np.ndarray: 2D array representing escape times, used for coloring the Julia set.
    """
    # Initialize escape times to zero
    escape_data = np.zeros(grid.shape, dtype=int)

    # Create a mutable copy of grid to perform iteration updates
    z = np.copy(grid)

    # NumPy's seterr suppresses warnings (e.g., overflow warnings)
    with np.errstate(over='ignore', invalid='ignore'):
        for i in range(max_iter):
            # Perform Julia set iteration: z_n+1 = z_n^2 + c
            z = z ** 2 + c

            # magnitude > 2
            escaped = np.abs(z) > 2

            # Assign escape iteration
            escape_data[escaped & (escape_data == 0)] = i
            z[escaped] = np.nan

    return escape_data