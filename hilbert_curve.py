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

    while (s < n):

        rx = ((t // 2) % 2)
        if (rx == 0):
            ry = (t % 2)
        else:
            ry = ((t ^ rx) % 2)
        x, y = rot(s, x, y, rx, ry)
        x = x + s * rx
        y = y + s * ry
        t = (t // 4)

        s = s * 2

    return x, y


# Mostly the original, paired down somewhat (slightly faster, easier to read)
def rot(n, x, y, rx, ry):
    if ry == 0:
        if rx == 1:
            x = n - 1 - x
            y = n - 1 - y

        x, y = y, x

    return x, y