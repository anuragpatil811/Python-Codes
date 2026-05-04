import sys
n = len(sys.argv)
args = sys.argv
print('No. of command line arguments=', n)
print('The arguments are:', args)
print('The args one by one:')
for a in args:
    print(a)
    