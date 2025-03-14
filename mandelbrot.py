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
                escape_times_arr[i, j] = 0 #escape time of zero
            else:
                escape_times_arr[i, j] = escape_time
    
    for i in range(escape_times_arr.shape[0]): #iterates through each value in escape times array
        for j in range(escape_times_arr.shape[1]):
            if escape_times_arr[i, j] == 0: #if escape time is zero, then color value is zero
                color_arr[i, j] = 0
            else:
                color_arr[i, j] = 1/(escape_times_arr[i, j]+1) #calculates what color time will be using escape time value found earlier
    
    return color_arr
                
