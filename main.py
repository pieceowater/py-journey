from math import factorial


class EasyTasks:

    @staticmethod
    def print_hi(name):
        return f'Hi, {name}'

    @staticmethod
    def write_hw():
        return 'Hello, World!'

    @staticmethod
    def count_to_ten():
        for i in range(10):
            print(i + 1)

    @staticmethod
    def odd_or_even(number):
        return "even" if number % 2 == 0 else "odd"

    @staticmethod
    def calculate_factorial(number):
        if number < 2:
            return 1
        else:
            return number * factorial(number - 1)

    @staticmethod
    def is_palindrome(string):
        return f'{string} is a palindrome' if string[::-1] == string else f'{string} is not a palindrome'

    @staticmethod
    def find_largest_in_list(data_list):
        if not (all(isinstance(item, (int, float)) for item in data_list)):
            return 'only Int or Float allowed'
        return max(data_list)

    def __init__(self):
        print(self.print_hi('Jhon'))
        print(self.write_hw())
        self.count_to_ten()
        print(self.odd_or_even(12))
        print(self.odd_or_even(21))
        print(self.calculate_factorial(4))
        print(self.is_palindrome('tenet'))
        print(self.is_palindrome('apple'))
        print(self.find_largest_in_list([1, 2, 3, 21, 3, 5]))


EasyTasks()
