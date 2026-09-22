try:
    num=int(input("Enter a number:"))
    result=10/num
except ValueError:
    print("Error:Please enter a valid integer.")
except ZeroDivisionError:
    print("Error:Cannot divide by zero.")
else:
    print("Sucess!Result=",result)
finally:
    print("Execution finished(cleaned here).")
