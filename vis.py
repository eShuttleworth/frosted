from PIL import Image, ImageDraw
from math import sqrt, ceil, log
import hilbert_curve as hc


def export_to_png_H(weight_arr, file_out):
    if file_out[-4:] != '.png':
        file_out += '.png'

    max_w = 255 / max(weight_arr)
    d = ceil(log(len(weight_arr), 2))
    dim = ceil(sqrt(2**d))

    img = Image.new('RGBA', (dim, dim), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)

    max_x, max_y = 0, 0
    for i in range(len(weight_arr)):
        x, y = hc.d2xy(d, i)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        if i % 25 == 0:
            print(max_x, max_y, dim)
        instant_w = ceil(weight_arr[i] * max_w)
        draw.point((x, y), fill=(instant_w, instant_w, instant_w, 255))

    if max_x < dim or max_y < dim:
        img = img.crop(box=(0, 0, min(max_x, dim), min(max_y, dim)))

    print('saving file')
    img.save(file_out, 'PNG')
    img.show()


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
        # weight_arr, d = hilbertify(weight_arr)
        # export_to_png(weight_arr, dim=ceil(sqrt(2**d)))
        export_to_png_H(weight_arr, file_out)
    elif encoding == 'l':
        export_to_png(weight_arr, file_out)
    else:
        print('Unexpected encoding encountered; exiting')
        raise Exception()
