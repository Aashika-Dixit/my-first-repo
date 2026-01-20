try:
 number1=int(input("enter first number: "))
 number2=int(input("enter second number: "))
 operator=(input("enter operator: "))

 if operator =='+':                 # addition
    print((number1+number2))   
 elif operator =='-':               # subtraction
    print(number1-number2)
 elif operator =='*':               # multiplication
    print(number1*number2)
 elif operator =='/':              # float division
   if number2 ==0:
    print("Error: division by zero is not allowed")
   else: 
    print(number1/number2)
 elif operator =='//':              # floor division
    if number2 ==0:
     print("Error: division by zero is not allowed")
    else:
     print(number1//number2)
 elif operator =='%':               # modulas
    if number2 ==0:
     print("Error: modulo by zero is not allowed")
    else:
     print(number1%number2)
 elif operator =='^':               # bitwise XOR
    print(number1^number2)
 elif operator =='&':              # bitwise and
    print(number1&number2)
 elif operator =='|':              #bitwise or
    print(number1|number2)
 else:
    print("invalid operator")
except ValueError:
  print("error: please enter valid integer values")        
