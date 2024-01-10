#addition
def add(n1,n2):
  return n1+n2
#subtraction
def sub(n1,n2):
  return n1-n2
#multiplication
def multiply(n1,n2):
  return n1*n2
#division
def divide(n1,n2):
  return n1/n2

operations = {"+": add,"-": sub,"*": multiply,"/": divide}

num1 = int(input("Enter the first number: "))
for symbol in operations:
  print(symbol)
operations_symbol = input("Pick an operation from the above line :")
num2 = int(input("Enter the second number: "))

calculated = operations[operations_symbol]
result = calculated(num1,num2)
print(f"{num1} {operations_symbol} {num2} = {result}")