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

def get_escape_time_color_arr(
    c_arr: np.ndarray,
    max_iterations: int
) -> np.ndarray:
    """
    Computes a numpy array of the color values for the given values. 
    The color values, ranging from 0 to 1(inclusive) are determined based on the escape time of each c-value.

    Parameters
    ----------
    c_arr: np.ndarray
        The array of values that will be used to find the color values
        
    Returns
    -------
    array, an array of the same shape as c_arr, with corresponding color values
    
    """
    
    escape_times_arr = np.zeros(c_arr.shape) #array of the escape times that is same shape as c_arr, but filled with zeroes initially
    color_arr = np.zeros(c_arr.shape) #creates an array that has the calculated color values using their escape times
    
    for i in range(escape_times_arr.shape[0]): #iterates through each value in escape times array
        for j in range(escape_times_arr.shape[1]):
            escape_time = get_escape_time(c_arr[i, j], max_iterations) #calls on get_escape_time to get number of iterations
            if escape_time is None:
                escape_times_arr[i, j] = max_iterations + 1 #will calculate an escape time of zero using formula
            else:
                escape_times_arr[i, j] = escape_time #assigns escape time value to the max iterations value returned
    
    for i in range(escape_times_arr.shape[0]): #iterates through each value in escape times array
        for j in range(escape_times_arr.shape[1]):
            escape_time = escape_times_arr[i, j] #gets the escape time values from the escape_times_arr
            color_arr[i, j] = (max_iterations - escape_time + 1) / (max_iterations + 1) #calculates the color value and adds it to the color array
    
    return color_arr

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
