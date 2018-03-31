class Calculator(object):
    
        

    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return float(a / b)
   
   

Calculator = Calculator()
n1 = float(raw_input("Enter the first number: "))
n2 = float(raw_input("Enter the second number: "))
operation = raw_input("What would you like to do?(Addition, Subtraction, Multiplication, or Division): ")
if operation == "Addition":
    print(Calculator.add(n1,n2))
elif operation == "Subtraction":
    print(Calculator.subtract(n1,n2))
elif operation == "Multiplication":
    print(Calculator.multiply(n1,n2))
elif operation == "Division":
    print(Calculator.divide(n1,n2))
else:
    print("Error")