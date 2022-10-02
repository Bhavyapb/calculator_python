from art import logo

def add(num1,num2):
  return num1+num2
def subtract(num1,num2):
  return num1-num2
def multiply(num1,num2):
  return num1*num2
def divide(num1,num2):
  return num1/num2

def calculator():
  print(logo)
  num1  = int(input("What's the first number?: "))
  #store opaerators and associated functions
  operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
  }
  #loop through the dictionary 
  for key in operations:
    print(key)
  
  should_continue = True
  while should_continue:
    operation_symbol = input("choose an operator from  above: ")
  
    num2 = int(input("What's the second number?: "))
  
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    #if the user wish to continue calculation...
    if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculator: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()
#now modifiying this to work if user wish to continue fresh...
#this is done by creating a recursive function

#lets begin!!!
calculator()