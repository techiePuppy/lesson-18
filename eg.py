try:
    num1=int(input("enter num1"))
    num2 =int(input("enter num2"))
    result=num1/num2 
    print("result is ",result)
except ZeroDivisionError:
    print("Division by zero is error!!")
except SyntaxError:
    print("comma is missing ")
except:
    print ("wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")