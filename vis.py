from PIL import Image, ImageDraw
from math import sqrt, ceil, log, floor
import hilbert_curve as hc
import matplotlib.pyplot as plt


def export_to_png_H(color_arr, file_out):
    if file_out[-4:] != '.png':
        file_out += '.png'

    d = ceil(log(len(color_arr), 2))
    dim = ceil(sqrt(2**d))

    img = Image.new('RGBA', (dim, dim), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)

    max_x, max_y = 0, 0
    for i in range(len(color_arr)):
        x, y = hc.d2xy(d, i)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

        draw.point((x, y), fill=(color_arr[i][0], color_arr[i][1], color_arr[i][2], color_arr[i][3]))

    if max_x < dim or max_y < dim:
        img = img.crop(box=(0, 0, min(max_x, dim), min(max_y, dim)))

    print('Saving {}'.format(file_out))
    img.save(file_out, 'PNG')


def export_to_png(weight_arr, file_out, dim=None):
    max_w = 255 / max(weight_arr)
    if not dim:
        dim = ceil(sqrt(len(weight_arr)))

    img = Image.new('RGBA', (dim, dim), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)

    for y in range(0, dim):
        if y % 100 == 0:
            print('y-level: {} done'.format(y))
        for x in range(0, dim):
            i = (y * dim) + x
            if i < len(weight_arr):
                instant_w = ceil(weight_arr[i] * max_w)
                draw.point((x, y), fill=(instant_w, instant_w, instant_w, 255))

    print('saving file')
    img.save(file_out, 'PNG')


#  encoding defaults to 'h'ilbert, can also be 'l'inear
def export(weight_arr, file_out, encoding='h'):
    if not file_out:
        file_out = './out/test_out.png'
    if encoding == 'h':
        export_to_png_H(weight_arr, file_out)
    elif encoding == 'l':
        export_to_png(weight_arr, file_out)
    else:
        print('Unexpected encoding encountered; exiting')
        raise Exception()


def export_plt(color_arr):
    d = ceil(log(len(color_arr), 2))
    dim = ceil(sqrt(2**d))

    img = Image.new('RGBA', (dim, dim), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)

    max_x, max_y = 0, 0
    for i in range(len(color_arr)):
        x, y = hc.d2xy(d, i)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

        draw.point((x, y), fill=tuple(*color_arr[i]))

    if max_x < dim or max_y < dim:
        img = img.crop(box=(0, 0, min(max_x, dim), min(max_y, dim)))

    fig, ax = plt.subplots(1, 1)
    im = ax.imshow(img)

    def onclick(event):
        try:
            print('Offset: {:X}'.format(hc.xy2d(d, floor(event.xdata), floor(event.ydata))))
        except TypeError:
            pass  # silently disregard typerrors (caused by clicking outside plot)

    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    plt.show()
    plt.disconnect(cid)
    del(im)


def export_plt(color_arr, block_size=64):
    d = ceil(log(len(color_arr), 2))
    dim = ceil(sqrt(2**d))

    img = Image.new('RGBA', (dim, dim), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)

    max_x, max_y = 0, 0
    for i in range(len(color_arr)):
        x, y = hc.d2xy(d, i)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

        draw.point((x, y), fill=tuple(color_arr[i]))

    if max_x < dim or max_y < dim:
        img = img.crop(box=(0, 0, min(max_x, dim), min(max_y, dim)))

    fig, ax = plt.subplots(1, 1)
    im = ax.imshow(img)

    def onclick(event):
        try:
            print('Offset: {:X}'.format(hc.xy2d(d, floor(event.xdata), floor(event.ydata))))
        except TypeError:
            pass  # silently disregard typerrors (caused by clicking outside plot)

    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    plt.show()
    plt.disconnect(cid)
    del(im)
