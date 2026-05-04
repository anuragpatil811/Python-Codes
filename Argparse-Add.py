import argparse
parser = argparse.ArgumentParser(description="This program calculates sum of two given numbers")
parser.add_argument("n1", type=float, help="Input first number")
parser.add_argument("n2", type=float, help="Input second number")
args = parser.parse_args()
result = float(args.n1) + float(args.n2)
print("Sum of two=", result)
