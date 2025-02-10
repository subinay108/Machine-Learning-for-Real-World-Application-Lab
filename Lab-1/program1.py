# Write a menu driven python program using class to build a calculator which can perform these operations:-
# 1) Addition 2) Substraction 3) Multiply 4) Divide 5) Exponentiation 6) Integer Division

class Calculator:
    def __init__(self):
        self.running = False

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def substract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Can't divide by 0"
        return a / b
    
    @staticmethod
    def exponentiation(a, b):
        return a ** b
    
    @staticmethod
    def int_divide(a, b):
        if b == 0:
            return "Can't divide by 0"
        return int(a // b)

    def start(self):
        self.running = True
        while self.running:
            # show menu
            print('''
Calculator
Choose options:-
1. Addition
2. Substraction
3. Multiply
4. Divide
5. Exponentiation
6. Integer Division
7. Quit
''')
            # take choice
            choice = int(input('Enter a choice: '))

            if choice not in (1, 2, 3, 4, 5, 6, 7):
                print('Invalid choice')
                continue

            if choice == 7:
                self.running = False
                continue
            
            # take inputs
            a = float(input('Enter first operand: '))
            b = float(input('Enter second operand: '))

            # calculate results
            if choice == 1:
                res = self.add(a, b)
            elif choice == 2:
                res = self.substract(a, b)
            elif choice == 3:
                res = self.multiply(a, b)
            elif choice == 4:
                res = self.divide(a, b)
            elif choice == 5:
                res = self.exponentiation(a, b)
            elif choice == 6:
                res = self.int_divide(a, b)

            # show results
            print('Result:', res)

if __name__ == '__main__':
    calculator = Calculator()
    calculator.start()