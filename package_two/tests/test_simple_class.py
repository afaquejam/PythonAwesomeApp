from package_two.module_two import SimpleClass

# capsys is a fixture that helps in capturing output from Stdout.
def test_simple_class(capsys):
    simple_class = SimpleClass()
    simple_class.name = "Punk"
    simple_class.operand_one = 1
    simple_class.operand_two = 2
    simple_class.print_result()
    stdout_result = capsys.readouterr().out
    assert stdout_result == "Hello Punk. The result is 3.\n"
