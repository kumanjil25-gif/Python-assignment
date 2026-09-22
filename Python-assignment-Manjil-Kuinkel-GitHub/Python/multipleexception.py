try:
    num=int(input("Enter a number:"))
    result=10/num
    print(result)
except(ValueError,ZeroDivisionError)as e:
    print("Caught an exception:",type(e).__name__)
