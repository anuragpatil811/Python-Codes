sample = lambda a, b, c, v, d: [a*b, b*c, c*v, v*d]
#print(sample(10, 20, 30, 40, 50))

#create a simple lambda function which will take 3 inputs and gives multiplication and addition in output
exp = lambda a, b, c: (a*b*c, a+b+c)
print(exp(10, 20, 30))