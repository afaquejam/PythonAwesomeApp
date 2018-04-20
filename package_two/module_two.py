from package_one.module_one import IntegerAdder

class SimpleClass(object):
    def __init__(self):
        self.name = None
        self.operand_one = None
        self.operand_two = None
        self.adder = IntegerAdder()

    def get_input(self):
        self.name = input('Enter thy holy name: ')
        self.operand_one = int(input("Enter first number: "))
        self.operand_two = int(input("Enter second number: "))

    def print_result(self):
        print(
            "Hello {}. The result is {}.".format(
                self.name,
                self.adder.add(self.operand_one, self.operand_two)
            )
        )
