import argparse
parser = argparse.ArgumentParser()
parser.add_argument('nums', nargs=2)
args = parser.parse_args()
print('Number=', args.nums[0])
print('Its power=', args.nums[1])
result = float(args.nums[0])**float(args.nums[1])
print('Result=', result)
