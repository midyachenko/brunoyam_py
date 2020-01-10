class BankClient():
    min_life=15*12
    def __init__(self, name='John', age=18, inc=400, status='citizen'):
        self.name = name
        self.age=age
        self.inc=inc
        self.status=status

    def get_month_inc(self):
        return self.inc/12

    def accept_credit(self,value):
        pay_time=70-self.age
        if self.inc - value/pay_time-self.min_life >0 and pay_time>0:
            return True
        else:
            False


max=BankClient('Макс',15,1000,'student')
bax=BankClient()
print(max.age)
print(max.get_month_inc())
print(max.accept_credit())
print(bax.age)
print(bax.get_month_inc())
print(bax.accept_credit())


