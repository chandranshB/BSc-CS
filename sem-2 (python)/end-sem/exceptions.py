def zero_division_handler():
    try:
        x = 10/0
    except ZeroDivisionError:
        print("Error: Zero se divide nahi hota!")


def name_error_handler():
    try:
        print(undefined_var)
    except NameError:
        print("Error: Variable define nahi hai!")


def key_error_handler():
    try:
        d = {}
        print(d['k'])
    except KeyError:
        print("Error: Key dictionary me nahi hai!")


def index_error_handler():
    try:
        l = [1,2]
        print(l[5])
    except IndexError:
        print("Error: Index out of range hai!")


def value_error_handler():
    try:
        int('abc')
    except ValueError:
        print("Error: Value convert nahi hui!")


def attribute_error_handler():
    try:
        x = 5
        x.append(1)
    except AttributeError:
        print("Error: Is object me attribute nahi hai!")


def file_not_found_handler():
    try:
        open('nofile.txt')
    except FileNotFoundError:
        print("Error: File nahi mila!")


def module_not_found_handler():
    try:
        import nomodule
    except ModuleNotFoundError:
        print("Error: Module install nahi hai!")


def general_error_handler():
    try:
        # sab type ke errors
        x = 10/0
    except Exception as e:
        print(f"General Error: {e}")

if __name__ == '__main__':
    zero_division_handler()
    name_error_handler()
    key_error_handler()
    index_error_handler()
    value_error_handler()
    attribute_error_handler()
    file_not_found_handler()
    module_not_found_handler()
    general_error_handler()