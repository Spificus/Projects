'''I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project
if I am found in violation of this policy.'''

class cashBox():
    def __init__(self, credit, totalReceived):
        self.credit = credit
        self.totalReceived = totalReceived

    def deposit(self, amount):
        self.credit += amount
        print(f"Depositing {amount} cents. You have {self.credit} cents credit.")

    def deduct(self, amount):
        self.credit -= amount

    def returnCoins(self):
        print ("Returning " + str(self.credit) + " cents")
        self.credit = 0

    def haveYou(self, amount):
        if amount <= self.credit:
            return True
        else:
            return False

    def total(self):
        return self.totalReceived

class product():
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def getPrice(self):
        return self.price

    def make(self):
        print("Making", self.name + ":")
        for ingredient in self.recipe:
            print( "\tDispensing", ingredient)

class selector():
    def __init__(self, cashBox, products):
        self.cashBox = cashBox
        self.products = products
        self.products = []
        p = product("black", 35, ["cup", "coffee", "water"])
        self.products.append(p)
        p = product("white", 35, ["cup", "coffee", "creamer", "water"])
        self.products.append(p)
        p = product("sweet", 35, ["cup", "coffee","sugar", "water"])
        self.products.append(p)
        p = product("whiteSweet", 35, ["cup", "coffee","sugar", "creamer", "water"])
        self.products.append(p)
        p = product("bouillon", 25, ["cup", "bouillon Powder", "water"])
        self.products.append(p)

    def select(self, choiceIndex):
        p = self.products[choiceIndex]
        price = p.getPrice()
        if self.cashBox.haveYou(price) == True:
            self.products[choiceIndex].make()
            self.cashBox.deduct(price)
            self.cashBox.totalReceived += price
            if self.cashBox.credit > 0:
                self.cashBox.returnCoins()
        else:
            print ("Error, not enough money")

class coffeeMachine():
    def __init__(self):
        self.cashBox = cashBox(0,0)
        self.selector = selector(self.cashBox,0)

    def oneAction(self):
        menu = "\tPRODUCT LIST: all 35 cents, except bouillon (25 cents) \n \t1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon \n \tSample commands: insert 35, select 1. Your command: \n "
        command = input(menu).split(" ")
        if command[0] == "insert" and int(command[1]) % 5 == 0:
            self.cashBox.deposit(int(command[1]))
        elif command[0] == "insert" and int(command[1]) % 5 != 0:
            print ("Pennies are not accepted")
        elif str(command[0]) == "select" and 0 <= int(command[1])-1 <= 4:
            self.selector.select(int(command[1])-1)
        elif str(command[0]) == "cancel":
            self.cashBox.returnCoins()
        elif str(command[0]) == "quit":
            return False
        else: 
            print ("Invalid input")
        return True

    def totalCash(self):
        return self.cashBox.total

def main():
    m = coffeeMachine()
    while m.oneAction():
        pass
    total = m.totalCash()
    print(f"Total cash: ${total()/100:.2f}")

if __name__ == "__main__":
    main()