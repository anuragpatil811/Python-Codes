a = 2
b = "Mohit"
try:
    print(a+b)
#except Exception:
#    print("Can't add string with Number")

#OR
except Exception as e:
    print("Can't add string with Number", f"{e}")

print("Bye")
