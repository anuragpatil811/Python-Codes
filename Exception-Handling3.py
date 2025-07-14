a = 6
b = 3
def div(a, b):
    try:
        print("In Try block")
        print(a/b)
        return "No Error"
    except Exception as e:
        print("In Exception block")
        print("Error", f"{e}")
        return "Error"
    finally:
        print("Done")
div(a, b)