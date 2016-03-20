from beverage import Beverage
class Machine(object):

    def __init__(self):
        self.beverages = []
        self.name = 'Delicious Drinks'

    def get_number_of_bev(self, drink):
        count = 0
        for x in self.beverages:
            if x.name == drink:
                count += 1

        return count

    def restock(self, drink, num):
        name    = drink[0]
        cals    = drink[1]
        price   = drink[2]
        pre_num = len(self.beverages)

        for x in range(num):
            bev = Beverage(name, cals, price)
            self.beverages.append(bev)

        num_added = len(self.beverages) - pre_num
        return '%(num_added)s %(name)ss have been added to the machine' % locals()

    @staticmethod
    def check_payment(money):
        if type(money) == int or float:
            return True



    @staticmethod
    def start():
        print "To start making a Soda Machine, first give it a name."
        name = raw_input()
        my_machine = Machine()
        my_machine.name = name
        print "Great."


if __name__ == '__main__':
    Machine.start()