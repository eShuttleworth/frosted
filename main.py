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
    p.add_argument('-b', action='store_true', required=False, help='Do binwalk analysis on the file')
    # p.add_argument('')
    return p.parse_args()


# dd if=mystery.ubi of=mystery_subset obs=1MB seek=54
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
    if (args.b):
        analysis.binwalk_analysis(args.i)
    else:
        f = entropy.get_hex_file(args.i)
        print('File read')
        arr = entropy.file_entropy(list(f), block_size=64)
        print('Entropy Calculated')
        vis.export(arr, args.o, encoding='h')


if __name__ == '__main__':
    args = parse_term()
    main(args)
