from mpl_toolkits.mplot3d import Axes3D  

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pprint import pprint
import numpy as np
import digraph
import trigraph
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
        for i in range(1048):
            index = depth + i
            if index + 1 >= len(byte_arr):
                break
            X[byte_arr[index], byte_arr[index+1], int(depth/1048)] = 1

    fig, ax = plt.subplots(1, 1)
    sd = digraph.ScrollyDigraph(ax, X)

    fig.canvas.mpl_connect('scroll_event', sd.onscroll)

    fmt = ticker.FuncFormatter(lambda x, _: '{:X}'.format(int(x)))
    axes = plt.gca()
    axes.get_xaxis().set_major_locator(ticker.MultipleLocator(64))
    axes.get_xaxis().set_major_formatter(fmt)
    axes.get_yaxis().set_major_locator(ticker.MultipleLocator(64))
    axes.get_yaxis().set_major_formatter(fmt)

    plt.show()

def scrolly_trigraph(hex_arr):
    byte_arr = bytify(hex_arr)

    X = []
    for depth in range(0, len(byte_arr), 1048):
        X.append([[], [], []])
        for i in range(1048):
            index = depth + i
            if index + 2 >= len(byte_arr):
                break
            X[int(depth/1048)][0].append(byte_arr[index])
            X[int(depth/1048)][1].append(byte_arr[index+1])
            X[int(depth/1048)][2].append(byte_arr[index+2])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d') 
    st = trigraph.ScrollyTrigraph(ax, X)

    fig.canvas.mpl_connect('scroll_event', st.onscroll)

    fmt = ticker.FuncFormatter(lambda x, _: '{:X}'.format(int(x)))
    axes = fig.gca()
    axes.get_xaxis().set_major_locator(ticker.MultipleLocator(64))
    axes.get_xaxis().set_major_formatter(fmt)
    axes.get_yaxis().set_major_locator(ticker.MultipleLocator(64))
    axes.get_yaxis().set_major_formatter(fmt)
    # axes.get_zaxis().set_major_locator(ticker.MultipleLocator(64))
    # axes.get_zaxis().set_major_formatter(fmt)

    fig.show()