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

        print '%(num_added)s %(name)ss have been added to the machine' % locals()
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
        print "Great. Now lets add some Beverages. Give me a name, the number of calories, and the price"
        bev_name = raw_input()
        bev_cals = raw_input()
        bev_price = raw_input()
        bev = Beverage(bev_name, bev_cals, bev_price)
        my_machine.beverages.append(bev)

        print "To restock more than one beverage at a time type 'restock'."
        interact = raw_input()

        if interact == "restock":
            print "Would you like to restock your previous drink or a new drink? Prev/New"
            answer = raw_input().lower()
            if answer == "prev":
                print "Great! How many?"
                num = int(raw_input())
                my_machine.restock([bev_name, bev_cals, bev_price], num)

if __name__ == '__main__':
    Machine.start()