import calendar
from math import factorial
from random import randrange


class EasyTasks:
    welcome_msg = 'You choose a easy task section!'
    task_list = '1. Write a program to print "Hello, World!" to the console.\n' \
                '2. Write a program to print the numbers from 1 to 10.\n' \
                '3. Write a program to check if a number is even or odd.\n' \
                '4. Write a program to calculate the factorial of a number.\n' \
                '5. Write a program to check if a given string is a palindrome.\n' \
                '6. Write a program to find the largest number in a list.\n' \
                '7. Write a program to remove duplicates from a list.\n' \
                '8. Write a program to reverse a string.\n' \
                '9. Write a program to find the sum of all numbers in a list.\n' \
                '10. Write a program to check if a given year is a leap year.\n' \
                '11. Write a program to generate a random number between 1 and 10.\n' \
                '12. Write a program to convert Celsius to Fahrenheit.\n' \
                '13. Write a program to convert kilometers to miles.\n' \
                '14. Write a program to find the length of a string.\n' \
                '15. Write a program to sort a list of numbers in ascending order.\n' \
                '16. Write a program to count the number of vowels in a string.\n' \
                '17. Write a program to find the second largest number in a list.\n' \
                '18. Write a program to check if a given number is prime.\n' \
                '19. Write a program to find the GCD of two numbers.\n' \
                '20. Write a program to print the Fibonacci series up to a given number.'

    @staticmethod
    def print_hi(name):
        return f'Hi, {name}'

    @staticmethod
    def count_to_ten(self):
        for i in range(10):
            print(i + 1)

    @staticmethod
    def odd_or_even(self, number):
        return "even" if number % 2 == 0 else "odd"

    @staticmethod
    def calculate_factorial(self, number):
        if number < 2:
            return 1
        else:
            return number * factorial(number - 1)

    @staticmethod
    def is_palindrome(self, string):
        return f'{string} is a palindrome' if string[::-1] == string else f'{string} is not a palindrome'

    @staticmethod
    def find_largest_in_list(self, data_list):
        if not (all(isinstance(item, (int, float)) for item in data_list)):
            return 'only Int or Float allowed'
        return max(data_list)

    @staticmethod
    def uniqualize_list(self, data_list):
        return set(data_list)

    @staticmethod
    def reverse_string(self, string):
        return string[::-1]

    @staticmethod
    def sum_list_items(self, data_list):
        return sum(data_list)

    @staticmethod
    def is_leap_year(self, year: int):
        return {
            "v1": f'{year} is leap' if 4 != 0 or 100 == 0 and 400 != 0 else f'{year} is not leap',
            "v2": f'{year} is leap' if calendar.isleap(year) else f'{year} is not leap',
        }

    @staticmethod
    def get_rand_number(self):
        return randrange(10)

    @staticmethod
    def c_to_f(self, c: int):
        return f'{c} C is {round(c * 1.8 + 32, 2)} F'

    @staticmethod
    def km_to_miles(self, km):
        return f'{km} km is {round(km * (1 / 1.609344), 3)} miles'

    @staticmethod
    def strlen(self, string):
        return f'length of "{string}" is {len(string)} symbols'

    @staticmethod
    def asc_sort_list(self, data_list, reverse=False):
        return sorted(data_list, reverse=reverse)

    @staticmethod
    def vowels_count(self, string):
        vowels_en = ['a', 'e', 'i', 'o', 'u', 'y']
        return sum(string.lower().count(letter) for letter in vowels_en)

    @staticmethod
    def second_largest_in_list(self, data_list):
        if not (all(isinstance(item, (int, float)) for item in data_list)):
            return 'only Int or Float allowed'
        if len(data_list) < 2:
            return 'List must contain at least two numbers'
        unique_nums = set(data_list)
        return max(unique_nums) if len(unique_nums) == 1 else sorted(unique_nums)[-2]

    @staticmethod
    def is_prime_number(self, number):
        return number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))

    @staticmethod
    def find_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def find_fibonacci(self, number):
        a, b, res = 0, 1, ""
        while a <= number:
            res += f'{a} '
            a, b = b, a + b
        return res

    def __init__(self):
        print(self.welcome_msg)
        print('(type \'tasks\' to see task list)')
        try:
            task = input('Select task: ')
            if not task == 'exit':
                if task == 'tasks':
                    print(self.task_list)
                    EasyTasks()
                else:
                    task = int(task)
                    if task == 1:
                        print(self.print_hi(input('whats ur name:')))
                    elif task == 2:
                        self.count_to_ten(self)
                    elif task == 3:
                        print(self.odd_or_even(self, int(input('number:'))))
                    elif task == 4:
                        print(self.calculate_factorial(self, int(input('number:'))))
                    elif task == 5:
                        print(self.is_palindrome(self, input('word:')))
                    elif task == 6:
                        print('list = [1, 2, 3, 21, 3, 5]')
                        print(self.find_largest_in_list(self, [1, 2, 3, 21, 3, 5]))
                    elif task == 7:
                        print('list = [1, 2, 2, 2, 3, 4, 5, 7, 8, 9, 9, 0]')
                        print(self.uniqualize_list(self, [1, 2, 2, 2, 3, 4, 5, 7, 8, 9, 9, 0]))
                    elif task == 8:
                        print(self.reverse_string(self, input('string to reverse:')))
                    elif task == 9:
                        print('list = [1, 2, 3, 4, 5]')
                        print(self.sum_list_items(self, [1, 2, 3, 4, 5]))
                    elif task == 10:
                        print(self.is_leap_year(self, int(input('year:'))))
                    elif task == 11:
                        print('rand num is => ' + str(self.get_rand_number(self)))
                    elif task == 12:
                        print(self.c_to_f(self, int(input('temp in C:'))))
                    elif task == 13:
                        print(self.km_to_miles(self, int(input('km to mile:'))))
                    elif task == 14:
                        print(self.strlen(self, input('string:')))
                    elif task == 15:
                        print('list = [5, 3, 2, 1]')
                        print(self.asc_sort_list(self, [5, 3, 2, 1]))
                    elif task == 16:
                        print(self.vowels_count(self, input('string:')))
                    elif task == 17:
                        print('list = [1, 2, 3, 22, 21, 5]')
                        print(self.second_largest_in_list(self, [1, 2, 3, 22, 21, 5]))
                    elif task == 18:
                        print(self.is_prime_number(self, int(input('num:'))))
                    elif task == 19:
                        print(self.find_gcd(self, int(input('first num:')), int(input('second num:'))))
                    elif task == 20:
                        print(self.find_fibonacci(self, int(input('number:'))))
                    else:
                        print('Not found!')
                    EasyTasks()
            else:
                MainController()

        except ValueError:
            print('Err!')
            EasyTasks()


class MediumTasks:

    def __init__(self):
        print('m tasks!')


class HardTasks:

    def __init__(self):
        print('hard tasks!')


class MainController(EasyTasks, MediumTasks, HardTasks):

    def __init__(self):
        try:
            category = input("Choose 0 (Easy), 1 (Medium), 2 (Hard) category (type 'exit' to quit): ")
            if not category == 'exit':
                category = int(category)
                if category == 0:
                    EasyTasks()
                elif category == 1:
                    MediumTasks()
                elif category == 2:
                    HardTasks()
                else:
                    print("Not found!")
            else:
                return

        except ValueError:
            print('Err!')


MainController()
