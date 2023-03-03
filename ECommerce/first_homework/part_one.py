def hello_world():
    print("Hello, world!")

def add_numbers(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")

def even_numbers():
    evens = [num for num in range(1, 11) if num % 2 == 0]
    print(evens)

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    print(f"The factorial of {num} is {result}.")

def find_largest(numbers):
    largest = max(numbers)
    print(f"The largest number in {numbers} is {largest}.")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

hello_world()                          
add_numbers(3, 5)                     
celsius_to_fahrenheit(25)              
even_numbers()                         
factorial(5)                           
find_largest([5, 2, 9, 10, 1])          
print(f" 7 is a prime {is_prime(7)}")                     
