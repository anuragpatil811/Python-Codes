import argparse
parser = argparse.ArgumentParser(description='this program displays the square value of given number')
parser.add_argument("num", type=int, help="Please input integer type number.")
args = parser.parse_args()
result = args.num**2
print("Square value=", result)