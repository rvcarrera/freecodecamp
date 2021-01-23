class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def get_balance(self):
        return sum([item['amount'] for item in self.ledger])
    def check_funds(self, amount):
        return amount <= self.get_balance()
    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })
        return True
    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({
            'amount': -amount,
            'description': description
        })
        return True
    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to {}'.format(other.name))
            other.deposit(amount, 'Transfer from {}'.format(self.name))
            return True
        return False
    def __str__(self):
        string = self.name.center(30, '*')
        for item in self.ledger:
            amount_str = '{:.2f}'.format(item['amount'])
            if len(item['description']) <= 23:
                new_line = '\n' + item['description']
                new_line += ' ' * (30 - len(item['description']) - len(amount_str))
                new_line += amount_str
                string += new_line
            else:
                new_line = '\n' + item['description'][:23]
                new_line += ' ' * (7 - len(amount_str))
                new_line += amount_str
                string += new_line
        string += '\nTotal: {:.2f}'.format(self.get_balance())
        return string


def create_spend_chart(categories):
    if len(categories) > 4:
        return False
    spend = {}
    total = 0
    string = 'Percentage spent by category\n'
    for item in categories:
        name, amount = item.name, 0
        for transaction in item.ledger:
            if transaction['amount'] < 0:
                amount -= transaction['amount']
        spend[name] = round(amount)
        total += round(amount)
    for item in categories:
        spend[item.name] = round((spend[item.name] * 100) / total)
    for i in range(100, -10, -10):
        line = str(i).rjust(3, ' ') + '|'
        for item in categories:
            if spend[item.name] >= i:
                line += ' o '
            else:
                line += '   '
        string += line + ' \n'
    string += '    ' + ('---' * len(categories)) + '-\n'
    names = []
    max_name = 0
    for k in spend.keys():
        names.append(k)
        if len(k) > max_name:
            max_name = len(k)
    for i in range(max_name):
        line = '    '
        for item in names:
            try:
                line += ' ' + item[i] + ' '
            except:
                line += '   '
        string+= line + ' \n'
    
    return string[:-1]
  

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([business, food, entertainment]))