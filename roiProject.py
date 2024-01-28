
class Home():
    def __init__(self):
        self.expenses = {}
        self.incomes = {}
        self.totalInvestment = {}

    def addIncome(self):
        income = input("What type of income?").lower()
        while True:
            try:
                amount = int(input("How much income will this provide?"))
                break
            except:
                print("Invalid entry. please enter a digit")

        if income not in self.incomes:
            self.incomes[income] = amount
            print(f"You've set your {income} income to {amount}")
        else: 
            print(f"You already have {income} saved at the amount ${self.incomes[income]}")

    def editIncome(self):
        income = input("What would you like to remove?").lower()
        amount = input("How much does this income provide? If you want to delete this income type 'remove'")
        if income not in self.incomes: print(f"Please enter a valid income")
        if amount == "remove" and income in self.incomes: del self.incomes[income]
        if income in self.incomes: 
            self.incomes[income] = int(amount)
    
    def showIncome(self):
        print(f"---Income---")
        for key, value in self.incomes.items():
            print(f"{key}: ${value}")

        
    def addExpense(self):
        expense = input("What expense would you like to add?").lower()
        try:
            amount = int(input("How much will this cost?"))
        except:
            print("Invalid entry. please enter a digit")
        if expense not in self.expenses:
            self.expenses[expense] = amount
            print(f"You have added {expense} costing you {amount} to your expenses")
        else:
            print(f"You already have {expense} saved at the cost of ${self.expenses[expense]}")

    def editExpense(self):
            expense = input("what expense do you want to adjust?").lower()
            amount = input("How much does this expense now cost? If you want to delete this expense type 'remove'")
            if amount == "remove" and expense in self.expenses: 
                del self.expenses[expense]
                print(f"You have successfully deleted {expense} from your expenses")
            if expense in self.expenses:
                self.expenses[expense] = int(amount)
            else: print(f"{expense} is not a current expense")

    def showExpenses(self):
        print(f"---Expenses---")
        for key, value in self.expenses.items():
            print(f"{key}: ${value}")
    
    def addInvestment(self):
        investment = input("Add an investment?").lower()
        try:
            amount = int(input("How much was this investment?"))
        except:
            print("Invalid entry. please enter a digit")
        if investment not in self.totalInvestment:
            self.totalInvestment[investment] = amount
            print(f"You've set your {investment} amount to {amount}")
        else: 
            print(f"You already have {investment} saved at the cost of ${self.totalInvestment[investment]}")

    def editInvestment(self):
        investment = input("What investment would you like to edit?").lower()
        amount = input("How much does this investment now provide? If you want to delete this investment type 'remove'")
        if amount == "remove" and investment in self.totalInvestment: del self.totalInvestment[investment]
        if investment in self.totalInvestment: 
            self.totalInvestment[investment] = int(amount)
        else: print(f"Please enter a valid investment")
    
    def showInvestments(self):
        print(f"---Investments---")
        for key, value in self.totalInvestment.items():
            print(f"{key}: ${value}")
    


def createROI():
    myHome = Home()
    
    while True:
        try:
            typeInput = input("What would you like to do? (Type: 'add', 'edit', 'show', 'finish')").lower()
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
            if typeInput == "finish":
                totalIncome = sum(myHome.incomes.values())
                totalExpenses = sum(myHome.expenses.values())
                totalInvestments = sum(myHome.totalInvestment.values())
                annualCashFlow = (totalIncome - totalExpenses) * 12
                roi = (annualCashFlow / totalInvestments) * 100
                return f" Your ROI is {roi:.2f}%"
        except ZeroDivisionError:
                print("Please add an investment")
        except:
                print("Invalid Action. Try Again")
        

print(createROI())


    