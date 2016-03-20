import unittest
from machine import Machine
from beverage import Beverage


class MachineTests(unittest.TestCase):

    def test_machine_has_a_name(self):
        my_machine = Machine()
        self.assertTrue(hasattr(my_machine, 'name'))

    def test_set_machine_name(self):
        my_machine = Machine()
        setattr(my_machine, 'name', "Different Name")

        self.assertEqual(my_machine.name, "Different Name")

    def test_machine_has_beverages(self):
        my_machine = Machine()
        self.assertTrue(hasattr(my_machine, 'beverages'))

    def test_set_machine_beverages(self):
        my_machine = Machine()
        bevs = []
        new_bev = Beverage("Coke", 150, 1.00)
        new_bev2 = Beverage("Pepsi", 150, 1.50)
        bevs.append(new_bev)
        bevs.append(new_bev2)
        setattr(my_machine, 'beverages', bevs)

        self.assertEqual(2, len(my_machine.beverages))

    def test_count_bevs_of_one_name(self):
        my_machine = Machine()
        bevs = []
        new_bev = Beverage('Coke', 150, 1.00)
        new_bev2 = Beverage('Coke', 150, 1.00)
        new_bev3 = Beverage('Pepsi', 150, 1.50)
        bevs.append(new_bev)
        bevs.append(new_bev2)
        bevs.append(new_bev3)
        my_machine.beverages = bevs

        self.assertEqual(2, my_machine.get_number_of_bev('Coke'))

    def test_restock_bevs_in_machine(self):
        bev = ['Coke', 150, 1.00]
        my_machine = Machine()

        self.assertEqual('10 Cokes have been added to the machine', my_machine.restock(bev, 10))

    def test_math_is_right_on_restock(self):
        bev1 = Beverage('Coke', 150, 1.00)
        bev = ['Coke', 150, 1.00]

        my_machine = Machine()
        my_machine.beverages.append((bev1))

        self.assertEqual('9 Cokes have been added to the machine', my_machine.restock(bev, 9))

    def test_accept_valid_payment(self):
        my_machine = Machine()
        self.assertEqual(True, my_machine.check_payment(1.00))

if __name__ == '__main__':
    unittest.main()
