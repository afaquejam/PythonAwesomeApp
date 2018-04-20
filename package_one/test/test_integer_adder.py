import pytest
from package_one.module_one import IntegerAdder

@pytest.fixture
def adder():
    print("Test set-up!")
    yield IntegerAdder()
    print("Test tear-down")

def test_integer_adder(adder):
    assert adder.add(1, 2) == 3

"""
In case you'd like to declare a fixture that executes only once per module, then declare a fixture like this:
@pytest.fixture(scope="module")
"""

@pytest.mark.parametrize(
    "operand_one, operand_two, expected_result",
    [
        (1, 2, 3),
        (10, 20, 30),
        (-5, -10, -15)
    ]
)

def test_integer_adder_complex(
        adder, operand_one, operand_two, expected_result
    ):
    assert adder.add(operand_one, operand_two) == expected_result
