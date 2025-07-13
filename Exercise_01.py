#Write a program that takes comma separated string from user, add generate a list and a tuple of these separated values
#a = input("Enter Comma Seperated Values:")
#print(a)

#Program for Arithmetic Progression and Geometeric Progression
a = int(input("Enter Starting Point of Sequence:"))
#temp = a
d = int(input("Enter Difference of AP:"))
r = int(input("Enter Common Ratio of GP:"))
#ap = [a]
#gp = [a]
#for i in range(temp, temp+10):
#    temp = temp+d
#    ap.append(temp)
#print("AP", ap)
#    print(i)
#temp = a
#for i in range(temp, temp+10):
#    temp = temp*r
#    gp.append(temp)
#print("GP", gp)   
def aps(a, d):
    ap = [a]  # Correctly initializing AP list
    for _ in range(9):  # Generate 9 more terms (total 10 terms)
        a += d
        ap.append(a)
    return ap

def gps(a, r):
    gp = [a]  # Correctly initializing GP list
    for _ in range(9):  # Generate 9 more terms (total 10 terms)
        a *= r
        gp.append(a)
    return gp

print("AP:", aps(a, d))
print("GP:", gps(a, r))