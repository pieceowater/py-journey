import calendar
from math import factorial
from random import randrange


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

    @staticmethod
    def uniqualize_list(data_list):
        return set(data_list)

    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def sum_list_items(data_list):
        return sum(data_list)

    @staticmethod
    def is_leap_year(year: int):
        return {
            "v1": f'{year} is leap' if 4 != 0 or 100 == 0 and 400 != 0 else f'{year} is not leap',
            "v2": f'{year} is leap' if calendar.isleap(year) else f'{year} is not leap',
        }

    @staticmethod
    def get_rand_number():
        return randrange(10)

    @staticmethod
    def c_to_f(c: int):
        return f'{c} C is {round(c * 1.8 + 32, 2)} F'

    @staticmethod
    def km_to_miles(km):
        return f'{km} km is { round(km * (1 / 1.609344), 3) } miles'

    def __init__(self):
        print(
            f'{self.print_hi("Jhon")}\n'
            + f'{self.write_hw()}\n'
            + f'{self.count_to_ten()}\n'
            + f'{self.odd_or_even(12)}\n{self.odd_or_even(21)}\n'
            + f'{self.calculate_factorial(4)}\n'
            + f'{self.is_palindrome("tenet")}\n{self.is_palindrome("apple")}\n'
            + f'{self.find_largest_in_list([1, 2, 3, 21, 3, 5])}\n'
            + f'{self.uniqualize_list([1, 2, 2, 2, 3, 4, 5, 7, 8, 9, 9, 0])}\n'
            + f'{self.reverse_string("desrever si gnirts siht")}\n'
            + f'{self.sum_list_items([1, 2, 3, 4, 5])}\n'
            + f'{self.is_leap_year(2020)}\n{self.is_leap_year(2023)}\n'
            + f'{self.get_rand_number()}\n'
            + f'{self.c_to_f(21)}\n'
            + f'{self.km_to_miles(21)}\n'
        )


EasyTasks()
