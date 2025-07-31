# code is made by ayush ///
 # making  a  bisic calculator
 
num1=int(input("enter num 1 :::")) # int coz to convert data type //
sign=input("enter sign like +,-,*,/:::")
num2=int(input("enter num 2 :::"))
# if//elif//eles
if sign=="+":
    print(f"sum of numbers {num1 + num2}")
elif sign=="-":
     print(f"subtraction of numbers {num1 - num2}")
elif sign=="*":
      print(f"multipliction of numbers {num1 * num2}")
elif sign=="/":
      print(f"div of numbers {num1 / num2}")
else:
     print("invlid sign /////")
