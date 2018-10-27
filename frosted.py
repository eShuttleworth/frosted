import entropy
import vis
import functools
import time
import argparse
import analysis


def parse_term():
    p = argparse.ArgumentParser(description='Frosted file analytics tool.')
    p.add_argument('i', metavar='Input', type=str)
    p.add_argument('-o', metavar='Output', type=str, required=False, help='Output file')
    p.add_argument('-s', metavar='block_size', default=64, help='Number of bytes to read in a block (default 64)', required=False)
    p.add_argument('-b', action='store_true', required=False, help='Do binwalk analysis on the file')
    p.add_argument('-y', action='store_true', required=False, help='Byte-stain file')
    p.add_argument('-e', action='store_true', required=False, help='Perform entropy analysis')
    return p.parse_args()


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        val = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('Finished in {} seconds'.format(run_time))
        return val

    return wrapper_timer


@timer
def main(args):
    f = None
    arr = None
    # if (args.b):
    #     analysis.binwalk_analysis(args.i)
    if args.y:
        if not f:
            f = entropy.get_hex_file(args.i)
            print('File read')
        arr = analysis.byte_stain(list(f))
        print('Bytes Stained')
        vis.export(arr, args.o, encoding='h')
    if args.e:
        if not f:
            f = entropy.get_hex_file(args.i)
            print('File read')
        arr = entropy.file_entropy(list(f), block_size=int(args.s))
        print('Entropy Calculated')
        vis.export(arr, args.o, encoding='h')


if __name__ == '__main__':
    args = parse_term()
    main(args)
