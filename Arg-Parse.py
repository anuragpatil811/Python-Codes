import argparse
#parser = argparse.ArgumentParser(description='This program displays the square value of given number')
parser = argparse.ArgumentParser()
parser.add_argument("num", type=int, help="Please input integer type number.")
args = parser.parse_args()
