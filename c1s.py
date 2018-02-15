#  BANK ACCOUNT MODEL
#  one Solution

balance = 0

# to deposit money
def deposit(amount):
    global balance
    balance += amount
    return balance

# to withdraw money
def withdraw(amount):
    global balance
    balance -= amount
    return balance

print(balance)
deposit(100)
print(balance)
withdraw(50)
print(balance)

#  Another way to solve it
#  using the dictionary local variable

def makeAccount():
    return { 'balance': 0 }

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

a = makeAccount()
b = makeAccount()

print(deposit(a,500))
print(deposit(b,300))
