import binwalk


def byte_stain(hex_arr):
    pass


def binwalk_analysis(file_in):
    bw = binwalk.scan('--signature', file_in)
    for module in bw:
        for result in module.results:
            print(result.description, result.file)
