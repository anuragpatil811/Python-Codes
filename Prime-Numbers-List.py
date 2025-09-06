#This quick demonstration shows you how powerful Python's filter() function can be!
nums = range(1, 1000)
def is_prime(num):
    for x in range(2, num):
        if(num%x)==0:
            return False
        return True
#primes = filter(is_prime, nums)
primes = list(filter(is_prime, nums))
print(primes)