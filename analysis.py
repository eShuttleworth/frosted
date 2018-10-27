import matplotlib.pyplot as plt
from pprint import pprint
import numpy as np
import digraph
from math import ceil

def byte_stain(hex_arr):
    color_arr = []

    for i in range(0, len(hex_arr), 2):  # each entry is a nibble
        if i <= len(hex_arr):
            sub = int('{}{}'.format(*hex_arr[i:i+2]).encode(), base=16)

            r = (sub & 7) * 32
            g = ((sub & 56) >> 3) * 32
            b = ((sub & 192) >> 5) * 64

            # print(r, g, b)
            color_arr.append((r, b, g, 255))
            
    return color_arr

def bytify(hex_arr):
    byte_arr = []
    for i in range(0, len(hex_arr), 2):
        if i <= len(hex_arr):
            byte_arr.append(int('{}{}'.format(*hex_arr[i:i+2]).encode(), base=16))
    return byte_arr


def scrolly_digraph(hex_arr):
    byte_arr = bytify(hex_arr)

    X = np.zeros((256, 256, ceil(len(byte_arr) / 1048)), dtype=int)
    for depth in range(0, len(byte_arr), 1048):
        # next_slice = np.zeros((256, 256), dtype=int)
        for i in range(1048):
            index = depth + i
            if index + 1 >= len(byte_arr):
                break
            print(byte_arr[index], byte_arr[index+1], depth/1048)
            X[byte_arr[index], byte_arr[index+1], int(depth/1048)] = 1
            # next_slice[byte_arr[i], byte_arr[i+1]] += 1
        # X.append(next_slice)

    fig, ax = plt.subplots(1, 1)
    print(ax, type(ax))
    sd = digraph.ScrollyDigraph(ax, X)

        
    fig.canvas.mpl_connect('scroll_event', sd.onscroll)
    plt.show()