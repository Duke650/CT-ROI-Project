#     -------- INCOME ---------- 
# Based on a $200,000 Home
# 2 units / each unit is $1000 / month = (Total Monthly Income) $2000 / mlth 



#       ------- Expenses --------
# Total Monthy Expenses = $1610

#         ------ Cash Flow ------
# Income ($2000) - Monthly Expenses ($1610) = $390


#       ----- Cash on Cash ROI -------
# Total Investment = $50,000
#  Down Payment 
# Closing Costs
# etc...
# Annual Cash Flow = Monthly Cash Flow ($390 * 12 = $4680
# ROI = Annual Cash Flow ($4680) / Total Investment ($50,000) = 9.36%

# class Cart():
#     def __init__(self):
#         self.cart = {}
    
#     def addItem(self):
#         itemToAdd = input("What do you want to add?").lower()
#         quantityToAdd = int(input("How many would you like to add?"))
#         if itemToAdd in self.cart:
#             self.cart[itemToAdd] += quantityToAdd
#         else:
#             self.cart[itemToAdd] = quantityToAdd
#         print(f"You have added {quantityToAdd} {itemToAdd} to your cart")

#     def removeItem(self):
#         itemToRemove = input("What do you want to remove?").lower()
#         quantityToRemove = input("How many would you like to remove? Type 'all' to delete this item")
#         if quantityToRemove == "all":
#             del self.cart[itemToRemove]
#             print(f"You have deleted {itemToRemove} from your cart")
#         else:
#             self.cart[itemToRemove] -= int(quantityToRemove)
#             print(f"You have removed {quantityToRemove} {itemToRemove} from your cart")
#             print(f"you now have {self.cart[itemToRemove]} {itemToRemove} in your cart")


#     def showCart(self):
#         for key, value in self.cart.items():
#             print(f"You have {value} {key} in your cart") 

# def createCart():
#     myCart = Cart()
#     while True:
#         userInput = input("Type add, remove, show, or quit").lower()
#         if userInput == "add":
#             myCart.addItem()
#         elif userInput == "remove":
#             myCart.removeItem()
#         elif userInput == "show":
#             myCart.showCart()
#         elif userInput == "quit":
#             print("Thank you for shopping with us")
#             break
#         else:
#             print("Please enter a valid input. ('add', 'remove', 'show', 'quit')")
# print(createCart())


class Home():
    def __init__(self):
        self.expenses = {}
        self.incomes = {}
        self.totalInvestment = {}

    def addIncome(self):
        income = input("What type of income?")
        amount = int(input("How much income will this provide?"))
        if income not in self.incomes:
            self.incomes[income] = amount
            print(f"You've set your {income} to {amount}")
        else: 
            print(f"You already have {income} saved at the amount ${self.incomes[income]}")

    def editIncome(self):
        income = input("What would you like to remove?")
        amount = input("How much does this income provide? If you want to delete this income type 'remove'")
        if amount == "remove" and income in self.incomes: del self.incomes[income]
        if income in self.incomes: 
            self.incomes[income] = int(amount)
        else: print(f"Please enter a valid income")
    
    def showIncome(self):
        for key, value in self.incomes.items():
            print(f"---Income---\n{key}: ${value}")

        
    def addExpense(self):
        expense = input("add an expense")
        amount = int(input("How much will this cost?"))
        if expense not in self.expenses:
            self.expenses[expense] = amount
            print(f"You have added {expense} costing you {amount} to your expenses")
        else:
            print(f"You already have {expense} saved at the cost of ${self.expenses[expense]}")

    def editExpense(self):
            expense = input("what expense do you want to adjust?")
            amount = input("How much does this expense now cost? If you want to delete this expense type 'remove'")
            if amount == "remove" and expense in self.expenses: 
                del self.expenses[expense]
                print(f"You have successfully deleted {expense} from your expenses")
            if expense in self.expenses:
                self.expenses[expense] = int(amount)
            else: print(f"{expense} is not a current expense")

    def showExpenses(self):
        for key, value in self.expenses.items():
            print(f"---Expenses---\n{key}: ${value}")
    
    def addInvestment(self):
        investment = input("Add an investment?")
        amount = int(input("How much was this investment?"))
        if investment not in self.totalInvestment:
            self.totalInvestment[investment] = amount
            print(f"You've set your {investment} amount to {amount}")
        else: 
            print(f"You already have {investment} saved at the cost of ${self.totalInvestment[investment]}")

    def editInvestment(self):
        investment = input("What investment would you like to edit?")
        amount = input("How much does this investment now provide? If you want to delete this investment type 'remove'")
        if amount == "remove" and investment in self.totalInvestment: del self.totalInvestment[investment]
        if investment in self.totalInvestment: 
            self.totalInvestment[investment] = int(amount)
        else: print(f"Please enter a valid investment")
    
    def showInvestments(self):
        for key, value in self.totalInvestment.items():
            print(f"---Investments---\n{key}: ${value}")
    

    


def createROI():
    myHome = Home()
    try:
        while True:
            typeInput = input("What would you like to do? (Type: 'add', 'edit', 'show')").lower()
            if typeInput == "add":
                sectionInput = input("What would you like to add? Type: 'income', 'expense, 'investment'").lower()
                if sectionInput == "income": myHome.addIncome()
                if sectionInput == "expense": myHome.addExpense()
                if sectionInput == "investment": myHome.addInvestment()
            if typeInput == "edit":
                sectionInput = input("What would you like to edit? Type: 'income', 'expense, 'investment'").lower()
                if sectionInput == "income": myHome.editIncome()
                if sectionInput == "expense": myHome.editExpense()
                if sectionInput == "investment": myHome.editInvestment()
            if typeInput == "show":
                sectionInput = input("What would you like to show? Type: 'income', 'expense, 'investment'").lower()
                if sectionInput == "income": myHome.showIncome()
                if sectionInput == "expense": myHome.showExpenses()
                if sectionInput == "investment": myHome.showInvestments()                
    except:
        print("Invalid Input. Try Again")

print(createROI())


    