

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

