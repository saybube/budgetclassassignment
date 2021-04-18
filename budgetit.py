
class Budget_cat:

    def __init__(self, name):
        self.name = name
        print('Category: ', self.name)

    def fund_dep(self):
        print("Deposit into selected category")

    def fund_withdraw(self):
        print("Withdraw from selected category")

    def cat_bal(self):
        print("Category balance")

    def bal_transfer(self):
        print("Transfer successful")


food = Budget_cat('Food')
food.fund_dep()
food.fund_withdraw()
food.cat_bal()
food.bal_transfer()

clothing = Budget_cat('Clothing')
clothing.fund_dep()
clothing.fund_withdraw()
clothing.cat_bal()
clothing.bal_transfer()

entment = Budget_cat('Entertainment')
entment.fund_dep()
entment.fund_withdraw()
entment.cat_bal()
entment.bal_transfer()
