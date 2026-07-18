from numpy import * 
m = matrix('1 2 3; 4 5 6; 7 8 9')
print(m)
t = m.transpose()
print("TRanspose Matrx:", t)
t1 = m.getT()
print("Find the transpose matrix:", t1)