from package_one.module_one import IntegerAdder

class SimpleClass(object):
    def __init__(self):
        self.name = None
        self.adder = None

    def get_input(self):
        self.name = input('Enter thy holy name: ')
        first_num = int(input("Enter first number: "))
        second_num = int(input("Enter second number: "))
        self.adder = IntegerAdder(first_num, second_num)

    def print_result(self):
        print("Hello {}. The result is {}.".format(self.name, self.adder.add()))
