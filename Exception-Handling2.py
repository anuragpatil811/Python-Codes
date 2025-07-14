a = 6
b = 2
try:
    print("In Try block")
    print(a/b)
    
#except ZeroDivisionError:
#    print("Can't divide by zero")
#except TypeError:
#    print("Enter Numbers")
except Exception as e:
    print("In Exception block")
    print("Error", f"{e}")
finally:
    print("Done")