
import streamlit as st


st.title("Our Open Dataset")

dataset = {
    1: '''def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]

    Note:
    Your algorithm should run in O(n) time and O(1) space.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], i]
        num_to_index[num] = i
    return []''',
    2:'''def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) <= n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence''',
    3: '''num = 7
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
''',
    4: '''year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
''',
    5: '''a = 5
b = 10
a, b = b, a
print("After swapping: a =", a, "b =", b)
''',
    6:'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("Factorial of 5 is", result)
''',
    7:'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 11
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
''',
    8:'''def reverse_string(s):
    return s[::-1]

original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print("Original:", original_string)
print("Reversed:", reversed_string)
''',
    9:'''def count_vowels_consonants(s):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

input_string = "Hello, World!"
vowels, consonants = count_vowels_consonants(input_string)
print("Vowels:", vowels)
print("Consonants:", consonants)
''',
    10:'''def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

text = "A man a plan a canal Panama"
if is_palindrome(text):
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')
''',
    11: '''def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

weight = 70  # in kilograms
height = 1.75  # in meters
bmi = calculate_bmi(weight, height)
print("BMI:", bmi)
''',
    12:'''import random

random_number = random.randint(1, 100)
print("Random Number:", random_number)
''',
    13:'''base = 2
exponent = 5
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result}")
''',
    14:'''def count_digits(n):
    return len(str(n))

number = 12345
digit_count = count_digits(number)
print(f"The number {number} has {digit_count} digits.")
''',
    15:'''def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

number = 12345
digit_sum = sum_of_digits(number)
print(f"The sum of digits in {number} is {digit_sum}.")
''',
    16:'''def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return n == total

number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
''',
    17: '''def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

number = 28
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
''',
    18: '''def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

principal_amount = 1000
rate_of_interest = 5
time_period = 2
simple_interest = calculate_simple_interest(principal_amount, rate_of_interest, time_period)
print(f"The simple interest is {simple_interest}.")
''',
    19:'''import cmath

def solve_quadratic(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return root1, root2

a = 1
b = -3
c = 2
root1, root2 = solve_quadratic(a, b, c)
print(f"The roots of the quadratic equation are {root1} and {root2}")
''',
    20:'''import math

num1 = 12
num2 = 18
lcm = (num1 * num2) // math.gcd(num1, num2)
gcd = math.gcd(num1, num2)

print(f"The LCM of {num1} and {num2} is {lcm}")
print(f"The GCD of {num1} and {num2} is {gcd}")
''',
    21: '''def generate_primes(n):
    primes = []
    for num in range(2, n+1):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes

n = 30
prime_numbers = generate_primes(n)
print("Prime numbers up to", n, "are", prime_numbers)
''',
    22:'''def find_path(maze, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in maze:
        return None
    for neighbor in maze[start]:
        if neighbor not in path:
            new_path = find_path(maze, neighbor, end, path)
            if new_path:
                return new_path
    return None''',
    23:'''#Generate combinations
def generate_combinations(arr, k, current=[]):
    if k == 0:
        print(current)
        return
    if not arr:
        return
    generate_combinations(arr[1:], k - 1, current + [arr[0]])
    generate_combinations(arr[1:], k, current)''',
    24:'''# Count digits
def count_digits(num):
    if num == 0:
        return 0
    return 1 + count_digits(num // 10)

# Array Sum
def array_sum(arr):
    if not arr:
        return 0
    return arr[0] + array_sum(arr[1:])''',
    25:'''s'''

}

x = 1
for value in dataset.values():
    st.write(f"Item {x}")
    x+=1
    st.code(body = value, language="python", line_numbers=False)

