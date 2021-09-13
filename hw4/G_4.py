import sys


class Account:
    def __init__(self, deposit):
        self.deposit = deposit


class Bank:
    def __init__(self):
        self.customers = {}

    def balance(self, customer, out=sys.stdout, test=False):
        if customer in self.customers:
            if not test:
                print(int(self.customers[customer].deposit))
            else:
                out.write(str(int(self.customers[customer].deposit)))
        else:
            if not test:
                print("ERROR")
            else:
                out.write("ERROR")
        return out

    def deposit(self, customer, deposit):
        if customer in self.customers:
            self.customers[customer].deposit += deposit
        else:
            self.customers[customer] = Account(deposit)

    def withdraw(self, customer, withdraw):
        if customer in self.customers:
            self.customers[customer].deposit -= withdraw
        else:
            self.customers[customer] = Account(-withdraw)

    def transfer(self, customer1, customer2, sum_of_transaction):
        if customer1 in self.customers:
            self.customers[customer1].deposit -= sum_of_transaction
        else:
            self.customers[customer1] = Account(-sum_of_transaction)
        if customer2 in self.customers:
            self.customers[customer2].deposit += sum_of_transaction
        else:
            self.customers[customer2] = Account(sum_of_transaction)

    def income(self, percent):
        percent = 1 + percent / 100
        for customer in self.customers:
            if self.customers[customer].deposit > 0:
                self.customers[customer].deposit = int(self.customers[customer].deposit * percent)


def main():
    bank = Bank()
    for line in sys.stdin:
        line = line.split()
        method, args = line[0].lower(), [(int(x) if x.isnumeric() else x) for x in line[1:]]
        func = getattr(bank, method)
        func(*args)


if __name__ == "__main__":
    main()


