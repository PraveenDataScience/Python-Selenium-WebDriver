from abc import ABC


class Loan(ABC):
    def getInterestRate(self):
        pass


class HomeLoan(Loan):
    def getInterestRate(self):
        return 8


class CarLoan(Loan):
    def getInterestRate(self):
        return 11

h=HomeLoan()
print(h.getInterestRate())

c=CarLoan()
print(c.getInterestRate())