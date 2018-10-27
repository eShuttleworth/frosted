import numpy as np
from math import log, ceil
import vis


def get_hex_file(fileloc):
    with open(fileloc, 'rb') as f:
        hex_file = f.read().hex()
    return hex_file


# https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
def entropy(labels, base=2):
    """ Computes entropy of label distribution. """

    n_labels = len(labels)

    if n_labels <= 1:
        return 0

    value, counts = np.unique(labels, return_counts=True)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)

    if n_classes <= 1:
        return 0

    ent = 0.

    # Compute entropy
    for i in probs:
        ent -= i * log(i, base)

    return ent


def file_entropy(hex_arr, block_size=16, byte_chunks=1):
    entropy_arr = []
    for i in range(0, len(hex_arr), block_size):
        if i > len(hex_arr):
            sub = hex_arr[i:]
        else:
            sub = hex_arr[i:i + block_size]
        entropy_arr.append(entropy(sub))

    max_w = 255 / max(entropy_arr)

    color_arr = []
    for i in entropy_arr:
        # , color_arr[i], color_arr[i], 255
        color_arr.append((ceil(i * max_w), ceil(i * max_w), ceil(i * max_w), 255))


    return color_arr


def main():
    hf = get_hex_file('./tests/test')
    file_entropy_array = file_entropy(list(hf), block_size=16)
    # print(file_entropy_array)
    vis.export_to_png(file_entropy_array, './out/test_out.png')


if __name__ == '__main__':
    main()
