# Exercise 1 : Built-In Functions

def myfunc():
    """'myfunc' documentation:
    'abs() bult-in'
    'int() bult-in'
    'input() bult-in'    
    """
    
    number = -20

    absolute_number = abs(number)
    print(absolute_number)
    
    result = int(9.9)
    print('int(9.9):', result)

    print('Enter your name:')
    x = input()
    print('Hello, ' + x)

print(myfunc.__doc__)

# 🌟 Exercise 2: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self) -> str:
        if self.amount > 1:
            return f'{self.amount} {self.currency}s'
        else:    
            return f'{self.amount} {self.currency}'

    def __int__(self) -> None:
        return self.amount

    def __repr__(self) -> str:
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if type(other) == int:
            return (self.amount + other)
        elif type(other) == Currency:
            return (self.amount + other.amount)
        else:
            raise TypeError('Argentina 3campeon')

    def __iadd__(self, other):
        try:
            if type(other) == int:
                return Currency(f'{self.currency}', self.amount + other)             
            elif type(other) == Currency:            
                return Currency(f'{self.currency}', self.amount + other.amount)
            else:
                raise TypeError('Argentina 3campeon')
        except:
            print('fallo')
        

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1+5)
print(c1+c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)