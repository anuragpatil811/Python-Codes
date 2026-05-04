#Write a function which will tell the inputed number is an armstrong number
def armstrong(num):
    digits = len(str(num)) #3
    summation = 0
    for i in str(num):
        summation = summation + int(i)**digits
    if summation == num:
        return 'the inputed number is an armstrong number'
    else:
        return 'this is not armstrong'
print(armstrong(24))
