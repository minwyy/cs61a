# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        global pre
        if self.value == 0:
            pre = self.value
            return Fib(1)
        else:
            nvalue, pre = self.value + pre, self.value
        return Fib(nvalue)

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock
        self.balance = 0
    
    def restock(self, resto):
        self.stock += resto
        return 'Current ' + self.name + ' stock: ' + str(self.stock)

    def deposit(self, money):
        if self.stock:
            self.balance += money
            return 'Current balance: $' + str(self.balance)
        else:
            return 'Machine is out of stock. Here is your $' + str(money) + '.'

    def vend(self):
        if not self.stock:
            return 'Machine is out of stock.'
        else:
            if self.balance < self.price:
                return 'You must deposit $' + str(self.price - self.balance) + ' more.'
            elif self.balance == self.price:
                self.stock -= 1
                self.balance = 0
                return 'Here is your ' + self.name +'.'
            else: 
                self.stock -= 1   
                change = self.balance - self.price
                self.balance = 0             
                return 'Here is your ' + self.name +' and $' + str(change) + ' change.'