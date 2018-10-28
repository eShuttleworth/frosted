#  https://people.sc.fsu.edu/~jburkardt/py_src/hilbert_curve/hilbert_curve.py
#  Though, modified for performance and readibility

# import platform
# from time import perf_counter


def d2xy(m, d):
    """
    #
    ## D2XY converts a 1D Hilbert coordinate to a 2D Cartesian coordinate.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 January 2016
    #
    #  Parameters:
    #
    #    Input, integer M, the index of the Hilbert curve.
    #    The number of cells is N=2^M.
    #    0 < M.
    #
    #    Input, integer D, the Hilbert coordinate of the cell.
    #    0 <= D < N * N.
    #
    #    Output, integer X, Y, the Cartesian coordinates of the cell.
    #    0 <= X, Y < N.
    """

    n = 2 ** m

    x = 0
    y = 0
    t = d
    s = 1

    while s < n:

        rx = (t // 2) % 2
        if (rx == 0):
            ry = t % 2
        else:
            ry = (t ^ rx) % 2
        x, y = rot(s, x, y, rx, ry)
        x = x + s * rx
        y = y + s * ry
        t = t // 4

        s = s * 2
    return x, y

def xy2d (m, x, y):

    """
    ## XY2D converts a 2D Cartesian coordinate to a 1D Hilbert coordinate.
    #
    #  Discussion:
    #
    #    It is assumed that a square has been divided into an NxN array of cells,
    #    where N is a power of 2.
    #
    #    Cell (0,0) is in the lower left corner, and (N-1,N-1) in the upper 
    #    right corner.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license. 
    #
    #  Modified:
    #
    #    03 January 2016
    #
    #  Parameters:
    #
    #    Input, integer M, the index of the Hilbert curve.
    #    The number of cells is N=2^M.
    #    0 < M.
    #
    #    Input, integer X, Y, the Cartesian coordinates of a cell.
    #    0 <= X, Y < N.
    #
    #    Output, integer D, the Hilbert coordinate of the cell.
    #    0 <= D < N * N.
    """

    xcopy = x
    ycopy = y

    d = 0
    n = 2 ** m

    s = n // 2

    while  0 < s:
        if 0 < (abs(xcopy) & s):
            rx = 1
        else:
            rx = 0

        if 0 < (abs(ycopy) & s):
            ry = 1
        else:
            ry = 0

        d = d + s * s * ((3 * rx) ^ ry)
        xcopy, ycopy = rot(s, xcopy, ycopy, rx, ry)
        s = s // 2
    return d


# Mostly the original, paired down somewhat (slightly faster, easier to read)
def rot(n, x, y, rx, ry):
    if not ry:
        if rx:
            x = n - 1 - x
            y = n - 1 - y

        x, y = y, x

    return x, y
