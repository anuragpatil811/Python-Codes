id = 10
name = 'Shankar'
sal = 19500.75
str = '{}, {}, {}'.format(id, name, sal)
print(str)
str1 = '{}-{}-{}'.format(id, name, sal)
print(str1)
str2 = 'Id={}\nName={}\nSalary={}'.format(id, name, sal)
print(str2)
str3 = 'Id = {0}\tName= {1}\t Salary = {2}'.format(id, name, sal)
print(str3)
str4 = 'Id= {2}\tName= {0}\tSalary= {1}'.format(id, name, sal)
print(str4)
str5 = 'Id= {one}, Name= {two}, Salary= {three}'.format(one=id, two=name, three=sal)
print(str5)
num = 5000
print('{:*^15d}'.format(num))
n1 = 1000
print('Hexadecimal= {:.>15X}\nBinary= {:.<15b}'.format(n1, n1))
print('Hexadecimal= {:.>#15X}\nBinary= {:.<#15b}'.format(n1, n1))