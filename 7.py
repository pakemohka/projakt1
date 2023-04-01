try:
    print("start code")
    print(10/0)
    print("No errors")
except (NameError, ZeroDivisionError):
    print("We have an Error")

print("code after capsule")